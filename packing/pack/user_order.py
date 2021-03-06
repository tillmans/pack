
#encoding:utf-8
from django.http import HttpResponse
import sys,json
from pack.models import User,OrderRecord,Order,OrderSku
from django.views.decorators.csrf import csrf_exempt
from pack.pack_push_2_shop import pushAPN,pushMessageToSingle
from pack.messageNotify import notify
import logging
from django.core.exceptions import ObjectDoesNotExist
from pack.tasks import sendMsg,tableTask
import pytz

reload(sys)
sys.setdefaultencoding('utf8')


@csrf_exempt
def PushAPNToShop(request):
    _deviceToken = request.REQUEST.get("deviceToken")
    _deviceToken = str(
        _deviceToken)
    print '2222'
    print _deviceToken
    pushAPN(_deviceToken,'0','350')
    return HttpResponse('yes')


@csrf_exempt
def getUserOrders(request):
    logger = logging.getLogger('Pack.app')
    logger.info('----------------------------')
    response = {}
    response_data = {}
    response['data'] = {}
    response['errorMsg'] = ""
    _userId = request.session.get('userId')
    if not _userId:
        response['code'] = 1
        response['errorMsg'] = '请先登录'
        return HttpResponse(json.dumps(response,ensure_ascii=False),content_type="application/json")
    ##################JUDGE############
    _lastLoginTime = request.session.get('lastLoginTime')
    if not _lastLoginTime:
        response['code'] = 1
        response['errorMsg'] = '请先登录'
        return HttpResponse(json.dumps(response),content_type="application/json")
    try:
        user = User.objects.get(id = _userId)
    except ObjectDoesNotExist:
        response['code'] = 1
        response['errorMsg'] = '请先登录'
        return HttpResponse(json.dumps(response,ensure_ascii=False),content_type="application/json")
    if _lastLoginTime != user.lastLoginTime:
        response['code'] = 1
        response['errorMsg'] = '上次登录失效，请重新登录'
        return HttpResponse(json.dumps(response),content_type="application/json")
    ####################END#################

    _orderId = request.REQUEST.get('orderId')
    if _orderId == None:
        response['code'] = -1
        response['errorMsg'] = '请输入订单id'
        return HttpResponse(json.dumps(response),content_type="application/json")
    _limit = request.REQUEST.get('limit',20)
    _limit = int(_limit)
    _orderId = int (_orderId)
    if _orderId == 0:
        orderQuery = Order.objects.select_related().filter(user__id = _userId).order_by('id')
    else:
        orderQuery = Order.objects.select_related().filter(user__id = _userId).filter(id__lt = _orderId).order_by('id')
    orders = orderQuery.reverse()[0:0+_limit]
    orderList = []
    for order in orders:
        _order = {}
        _order['orderId'] = order.id
        _priceTotal = float(order.priceTotal)
        _order['priceTotal'] = str(_priceTotal)
        _order['skuInfo'] = order.skuInfo
        shanghai_tz = pytz.timezone('Asia/Shanghai')
        _order['dateTime'] = order.date.astimezone(shanghai_tz).strftime('%Y/%m/%d %H:%M:%S')
        _order['status'] = order.status
        _shopInfo = {}
        _shopInfo['shopId'] = order.shop_id
        _shopInfo['shopName'] = order.shop.name
        _headImage = order.shop.headImage+"!100"
        _shopInfo['headImage'] = _headImage
        _order['shopInfo'] = _shopInfo
        orderList.append(_order)
    response_data['orders'] = orderList
    response['code'] = 0
    response['data'] = response_data
    return HttpResponse(json.dumps(response),content_type = "application/json")


@csrf_exempt
def getUserOrderDetail(request):
    logger = logging.getLogger('Pack.app')
    logger.info('----------------------------')
    response = {}
    response['data'] = {}
    response['errorMsg'] = ""
    _userId = request.session.get('userId')
    if not _userId:
        response['code'] = 1
        response['errorMsg'] = '请先登录'
        return HttpResponse(json.dumps(response,ensure_ascii=False),content_type="application/json")
    ##################JUDGE############
    _lastLoginTime = request.session.get('lastLoginTime')
    if not _lastLoginTime:
        response['code'] = 1
        response['errorMsg'] = '请先登录'
        return HttpResponse(json.dumps(response),content_type="application/json")
    try:
        user = User.objects.get(id = _userId)
    except ObjectDoesNotExist:
        response['code'] = 1
        response['errorMsg'] = '请先登录'
        return HttpResponse(json.dumps(response,ensure_ascii=False),content_type="application/json")
    if _lastLoginTime != user.lastLoginTime:
        response['code'] = 1
        response['errorMsg'] = '上次登录失效，请重新登录'
        return HttpResponse(json.dumps(response),content_type="application/json")
    ####################END#################

    _orderId = request.REQUEST.get('orderId')
    if _orderId == None or _orderId == '':
        response['code'] = -1
        response['errorMsg'] = '获取订单详情失败'
        return HttpResponse(json.dumps(response,ensure_ascii=False),content_type="application/json")
    try:
        order = Order.objects.select_related().get(id = _orderId)
    except ObjectDoesNotExist:
        response['code'] = -1
        response['errorMsg'] = '获取订单详情失败'
        return HttpResponse(json.dumps(response,ensure_ascii=False),content_type="application/json")

    _order = {}
    _order['orderId'] = order.id
    _order['priceTotal'] = float(order.priceTotal)
    _order['status'] = order.status
    shanghai_tz = pytz.timezone('Asia/Shanghai')
    date = order.date.astimezone(shanghai_tz)
    _order['dateTime'] = date.strftime('%Y/%m/%d %H:%M:%S')

    _tableInfo = {}
    _tableInfo['tableNumber'] = order.tableNumber
    _order['tableInfo'] = _tableInfo
    _shopInfo = {}
    _shopInfo['shopId'] = order.shop_id
    _shopInfo['shopName'] = order.shop.name
    _shopInfo['shopHeadImage'] = order.shop.headImage
    _shopInfo['shopTelephone'] = order.shop.telephone
    _shopInfo['province'] = order.shop.province
    _shopInfo['city'] = order.shop.city
    _shopInfo['district'] = order.shop.district
    _shopInfo['addressDetail'] = order.shop.addressDetail
    _order['shopInfo'] = _shopInfo
    _skuList = []
    orderSKUQuery = OrderSku.objects.filter(order__id = order.id)
    for orderSKU in orderSKUQuery:
        _sku = {}
        _sku['orderSKUId'] = orderSKU.id
        _sku['skuName'] = orderSKU.name.encode('utf-8')
        _sku['skuStatus'] = orderSKU.status
        _sku['oriPrice'] = float(orderSKU.unitPrice)
        _sku['weightInfo'] = orderSKU.weightInfo.encode('utf-8')
        _sku['skuQuantity'] = float(orderSKU.number)
        _skuList.append(_sku)
    _order['skuList'] = _skuList
    _orderRecordList = []
    orderRecordList = OrderRecord.objects.filter(order__id = _orderId).order_by('-id')
    for orderRecord in  orderRecordList:
        _orderRecord = {}
        _orderRecord['record'] = orderRecord.record
        shanghai_tz = pytz.timezone('Asia/Shanghai')
        date = orderRecord.date.astimezone(shanghai_tz)
        _orderRecord['date'] = date.strftime('%Y/%m/%d %H:%M:%S')
        _orderRecordList.append(_orderRecord)
    _order['orderRecord'] = _orderRecordList
    response['data'] = _order
    response['code'] = 0
    return HttpResponse(json.dumps(response,ensure_ascii=False),content_type="application/json")

def test(request):
    '''response = pushMessageToSingle('25b5663a72b19311b3fdef7db65b4ff3',0)
    print response
    rst = response['result']
    if rst == 'ok':
        return HttpResponse('11')

    return HttpResponse('11')

    params = urllib.urlencode({'orderId':'1'})
    url_req = "http://127.0.0.1:8000/getShopOrderDetail"
    sms_req = urllib2.Request(url = url_req, data = params)
    sms_response = urllib2.urlopen(sms_req)
    sms_response=sms_response.read()
    return HttpResponse(sms_response)
'''
    response = notify('18201637776','2')
    print response
    return HttpResponse('yes')

