__author__ = 'mike'
#encoding:utf-8
from django.http import HttpResponse
import sys,json
from pack.models import WaiterServe,OrderSku,Order,User
from django.views.decorators.csrf import csrf_exempt
import logging
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist
from pack.pack_push_2_user import pushAPN,pushMessageToSingle
import pytz

reload(sys)
sys.setdefaultencoding('utf8')

@csrf_exempt
def waiterServeGetOrderSkuList(request):
    logger = logging.getLogger('Pack.app')
    response = {}
    response['data'] = {}
    response['errorMsg'] = ""
    _waiterServeId = request.session.get('waiterServeId')
    if not _waiterServeId:
        response['code'] = 1
        response['errorMsg'] = '请先登录'
        return HttpResponse(json.dumps(response),content_type="application/json")
    ##################JUDGE############
    _lastLoginTime = request.session.get('lastLoginTime')
    if not _lastLoginTime:
        response['code'] = 1
        response['errorMsg'] = '请先登录'
        return HttpResponse(json.dumps(response),content_type="application/json")
    try:
        waiterServe = WaiterServe.select_related().objects.get(id = _waiterServeId)
    except ObjectDoesNotExist:
        response['code'] = 1
        response['errorMsg'] = '请先登录'
        return HttpResponse(json.dumps(response,ensure_ascii=False),content_type="application/json")
    if _lastLoginTime != waiterServe.lastLoginTime:
        response['code'] = 1
        response['errorMsg'] = '上次登录失效，请重新登录'
        return HttpResponse(json.dumps(response),content_type="application/json")
    ####################END#################

    _orderSkuId = request.REQUEST.get('0rderSkuId')
    _limit = request.REQUEST.get('limit',20)
    _limit = int(_limit)

    if _orderSkuId == None:
        response['code'] = -1
        response['errorMsg'] = '请输入订单id'
        return HttpResponse(json.dumps(response),content_type="application/json")
    _orderSkuId = int (_orderSkuId)
    if _orderSkuId == 0:
        orderSkuQuery = OrderSku.objects.select_related().filter(waiterServeId = _waiterServeId).filter(status = '1').order_by('id')
        orderSkus = orderSkuQuery.reverse()[0:0+_limit]
    else:
        orderSkuQuery = OrderSku.objects.select_related().filter(waiterServeId = _waiterServeId).filter(status = '1').filter(id__lt =
            _orderSkuId).order_by('id')
        orderSkus = orderSkuQuery.reverse()[0:0+_limit]
    orderSkuList = []
    for orderSku in orderSkus:
        _orderSku = {}
        _orderSku['skuId'] = orderSku.skuId
        _orderSku['skuName'] = orderSku.skuName
        _orderSku['skuPrice'] = orderSku.skuPrice
        _orderSku['skuSizeName'] = orderSku.skuSizeName
        _orderSku['skuQuantity'] = orderSku.skuQuantity
        orderSkuList.append(_orderSku)
    response['code'] = 0
    response['data'] = orderSkuList
    return HttpResponse(json.dumps(response),content_type="application/json")

@csrf_exempt
def waiterServeFinishOrderSku(request):
    logger = logging.getLogger('Pack.app')
    response = {}
    response['data'] = {}
    response['errorMsg'] = ""
    _waiterServeId = request.session.get('waiterServeId')
    if not _waiterServeId:
        response['code'] = 1
        response['errorMsg'] = '请先登录'
        return HttpResponse(json.dumps(response),content_type="application/json")
    ##################JUDGE############
    _lastLoginTime = request.session.get('lastLoginTime')
    if not _lastLoginTime:
        response['code'] = 1
        response['errorMsg'] = '请先登录'
        return HttpResponse(json.dumps(response),content_type="application/json")
    try:
        waiterServe = WaiterServe.select_related().objects.get(id = _waiterServeId)
    except ObjectDoesNotExist:
        response['code'] = 1
        response['errorMsg'] = '请先登录'
        return HttpResponse(json.dumps(response,ensure_ascii=False),content_type="application/json")
    if _lastLoginTime != waiterServe.lastLoginTime:
        response['code'] = 1
        response['errorMsg'] = '上次登录失效，请重新登录'
        return HttpResponse(json.dumps(response),content_type="application/json")
    ####################END#################

    _orderSkuId = request.REQUEST.get('0rderSkuId')

    if _orderSkuId == None or _orderSkuId == '':
        response['code'] = -1
        response['errorMsg'] = '请输入订单id'
        return HttpResponse(json.dumps(response),content_type="application/json")
    try:
        orderSku = OrderSku.objects.get(id = str(_orderSkuId))
    except ObjectDoesNotExist:
        response['code'] = -1
        response['errorMsg'] = '查询orderSku失败'
        return HttpResponse(json.dumps(response),content_type="application/json")
    if orderSku.status == '1':
        orderSku.status = '2'
        orderSku.save()
    elif orderSku.status == '2':
        response['code'] = 0
        return HttpResponse(json.dumps(response),content_type="application/json")
    else:
        response['code'] = -1
        response['errorMsg'] = 'orderSku状态错误'
        return HttpResponse(json.dumps(response),content_type="application/json")


@csrf_exempt
def getShopOrderDetailWithTable(request):
    logger = logging.getLogger('Pack.app')
    response = {}
    response['data'] = {}
    response['errorMsg'] = ""
    _waiterServeId = request.session.get('waiterServeId')
    if not _waiterServeId:
        response['code'] = 1
        response['errorMsg'] = '请先登录'
        return HttpResponse(json.dumps(response),content_type="application/json")
    ##################JUDGE############
    _lastLoginTime = request.session.get('lastLoginTime')
    if not _lastLoginTime:
        response['code'] = 1
        response['errorMsg'] = '请先登录'
        return HttpResponse(json.dumps(response),content_type="application/json")
    try:
        waiterServe = WaiterServe.select_related().objects.get(id = _waiterServeId)
    except ObjectDoesNotExist:
        response['code'] = 1
        response['errorMsg'] = '请先登录'
        return HttpResponse(json.dumps(response,ensure_ascii=False),content_type="application/json")
    if _lastLoginTime != waiterServe.lastLoginTime:
        response['code'] = 1
        response['errorMsg'] = '上次登录失效，请重新登录'
        return HttpResponse(json.dumps(response),content_type="application/json")
    ####################END#################

    _tableId = request.REQUEST.get('tableId')
    if _tableId == None or _tableId == '':
        response['code'] = -1
        response['errorMsg'] = '获取tableId失败'
        return HttpResponse(json.dumps(response),content_type="application/json")
    _tableId = str(_tableId)
    try:
        order = Order.objects.filter(table__id =_tableId).filter(Q(status = '0') | Q (status = '2')).last()
    except IndexError:
        response['code'] = -1
        response['errorMsg'] = '获取订单失败'
        return HttpResponse(json.dumps(response),content_type="application/json")
    _order = {}
    _order['orderId'] = str(order.id)
    _order['tableId'] = str(order.tableId)
    _order['tableNumber'] = str(order.tableNumber)
    _order['priceTotal'] = float(order.priceTotal)
    _order['status'] = order.status
    shanghai_tz = pytz.timezone('Asia/Shanghai')
    _order['dateTime'] = order.date.astimezone(shanghai_tz).strftime('%Y/%m/%d %H:%M:%S')

    if order.userId =='':
        _order['userInfo'] = ''
    else:
        try:
            user = User.objects.get(id = order.userId)
        except ObjectDoesNotExist:
            response['code'] = -1
            response['errorMsg'] = '获取用户消息失败'
            return HttpResponse(json.dumps(response),content_type="application/json")
        _userInfo = {}
        _userInfo['userId'] = str(user.id)
        _userInfo['userName'] = user.name
        _userInfo['userHeadImage'] = user.headImage
        _userInfo['userTelephone'] = user.telephone
        _order['userInfo'] = _userInfo
    _skuList = []
    orderSkuQuery = OrderSku.objects.filter(order__id = order.id)
    for orderSku in orderSkuQuery:
        _sku = {}
        _sku['orderSkuId'] = orderSku.id
        _sku['skuId'] = orderSku.skuId
        _sku['skuName'] = orderSku.name.encode('utf-8')
        _sku['skuPrice'] = float(orderSku.skuPrice)
        _sku['skuSizeName'] = str(orderSku.skuSizeName)
        _sku['skuQuantity'] = float(orderSku.skuQuantity)
        _sku['skuStatus'] = orderSku.status
        _skuList.append(_sku)
    _order['skuList'] = _skuList
    response['data'] = _order
    response['code'] = 0
    return HttpResponse(json.dumps(response),content_type = "application/json")

