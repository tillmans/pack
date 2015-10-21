#encoding:utf-8
from django.http import HttpResponse
import sys,json,datetime
from pack.models import Shop,Order,OrderSku,Table,OrderRecord
from django.views.decorators.csrf import csrf_exempt
import logging
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist
from pack.pack_push_2_user import pushAPN,pushMessageToSingle
import pytz

reload(sys)
sys.setdefaultencoding('utf8')



@csrf_exempt
def PushAPN(request):
    _deviceToken = request.REQUEST.get("deviceToken")
    print '1111'
    pushAPN(_deviceToken,'1000','350')
    return HttpResponse('yes')

@csrf_exempt
def getShopOrderDetailWithTable(request):
    logger = logging.getLogger('Pack.app')
    logger.info('----------------------------')
    response = {}
    response['data'] = {}
    response['errorMsg'] = ""
    _shopId = request.session.get('shopId')
    if not _shopId:
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
        shop = Shop.objects.get(id = _shopId)
    except ObjectDoesNotExist:
        response['code'] = 1
        response['errorMsg'] = '请先登录'
        return HttpResponse(json.dumps(response,ensure_ascii=False),content_type="application/json")
    if _lastLoginTime != shop.lastLoginTime:
        response['code'] = 1
        response['errorMsg'] = '上次登录失效，请重新登录'
        return HttpResponse(json.dumps(response),content_type="application/json")
    ####################END#################

    _tableId = request.REQUEST.get('tableId')
    _orderId = request.REQUEST.get('orderId')
    _limit = request.REQUEST.get('limit',20)
    _limit = int(_limit)
    if _tableId == None or _tableId == '':
        response['code'] = -1
        response['errorMsg'] = '获取tableId失败'
        return HttpResponse(json.dumps(response),content_type="application/json")
    if _orderId == None or _orderId == '':
        response['code'] = -1
        response['errorMsg'] = '获取orderId失败'
        return HttpResponse(json.dumps(response),content_type="application/json")

    _tableId = str(_tableId)
    _orderId = str(_orderId)
    if _orderId == '0':
        orderQuery = Order.objects.filter(table__id =_tableId)
    else:
        orderQuery = Order.objects.filter(table__id =_tableId).filter(id__lt = _orderId)
    orders = orderQuery.reverse()[0:0+_limit]
    orderList = []
    for order in orders:
        _order = {}
        _order['orderId'] = order.id
        _order['tableNumber'] = order.tableNumber
        _priceTotal = float(order.priceTotal)
        _order['priceTotal'] = str(_priceTotal)
        shanghai_tz = pytz.timezone('Asia/Shanghai')
        _order['dateTime'] = order.date.astimezone(shanghai_tz).strftime('%Y/%m/%d %H:%M:%S')
        _order['status'] = order.status
        orderList.append(_order)
    response['code'] = 0
    response['data'] = orderList
    return HttpResponse(json.dumps(response),content_type = "application/json")


@csrf_exempt
def getShopOrderDetail(request):
    logger = logging.getLogger('Pack.app')
    logger.info('----------------------------')
    response = {}
    response['data'] = {}
    response['errorMsg'] = ""
    _shopId = request.session.get('shopId')
    if not _shopId:
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
        shop = Shop.objects.get(id = _shopId)
    except ObjectDoesNotExist:
        response['code'] = 1
        response['errorMsg'] = '请先登录'
        return HttpResponse(json.dumps(response,ensure_ascii=False),content_type="application/json")
    if _lastLoginTime != shop.lastLoginTime:
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
    # _orderInfo = {}
    _order['orderId'] = order.id
    _order['payStyle'] = order.payStyle
    _order['eatStyle'] = order.eatStyle
    _order['priceTotal'] = float(order.priceTotal)
    _order['status'] = order.status
    shanghai_tz = pytz.timezone('Asia/Shanghai')
    _order['dateTime'] = order.date.astimezone(shanghai_tz).strftime('%Y/%m/%d %H:%M:%S')

    # _order['orderInfo'] = _orderInfo
    _tableInfo = {}
    _tableInfo['tableId'] = order.id
    _tableInfo['tableNumber'] = order.tableNumber
    _order['tableInfo'] = _tableInfo
    _userInfo = {}
    _userInfo['userId'] = order.user_id
    _userInfo['nickName'] = order.user.nickName
    _userInfo['headImage'] = order.user.headImage
    _userInfo['telephone'] = order.user.telephone
    _order['userInfo'] = _userInfo
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
    response['data'] = _order
    response['code'] = 0
    return HttpResponse(json.dumps(response),content_type="application/json")
