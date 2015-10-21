#encoding:utf-8
from django.http import HttpResponse
from pack.models import Order,User,OrderRecord
import json,sys,datetime
from django.views.decorators.csrf import csrf_exempt
import pingpp,logging
from django.core.exceptions import ObjectDoesNotExist
from pack.pack_push_2_saler import pushAPN,pushMessageToSingle

reload(sys)
sys.setdefaultencoding('utf8')

api_key = 'sk_live_SCyrjLjbX5i9fPinLSPiDuzH'

@csrf_exempt
def aliPay(request):
    logger = logging.getLogger('Pack.app')
    logger.info('----------------------------')
    response = {}
    response['data'] = {}
    response['errorMsg'] = ""
    _userId = request.session.get('userId')
    if not _userId:
        response['code'] = -1
        response['errorMsg'] = '请先登录'
        return HttpResponse(json.dumps(response,ensure_ascii=False),content_type="application/json")
    ##################JUDGE############
    _lastLoginTime = request.session.get('lastLoginTime')
    if not _lastLoginTime:
        response['code'] = -1
        response['errorMsg'] = '请先登录'
        return HttpResponse(json.dumps(response),content_type="application/json")
    try:
        user = User.objects.get(id = _userId)
    except ObjectDoesNotExist:
        response['code'] = -1
        response['errorMsg'] = '请先登录'
        return HttpResponse(json.dumps(response,ensure_ascii=False),content_type="application/json")
    if _lastLoginTime != user.lastLoginTime:
        response['code'] = -1
        response['errorMsg'] = '上次登录失效，请重新登录'
        return HttpResponse(json.dumps(response),content_type="application/json")
    ####################END#################

    _amount = request.REQUEST.get('priceTotal')
    if _amount == None or _amount == '':
        response['code'] = -1
        response['errorMessage'] = '请输入金额'
        return HttpResponse(json.dumps(response),content_type= "application/json")
    _amount = str(_amount)
    _amount = int(_amount)

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


    _order_no = str(order.id)
    _order_no = _order_no.zfill(20)
    pingpp.api_key = api_key
    extras=dict()
    ch = pingpp.Charge.create(
        order_no=_order_no,
        channel='alipay',
        amount=_amount,
        subject='快点餐',
        body='给商家付款',
        currency='cny',
        app=dict(id='app_5WzbnP08OyDCevLS'),
        client_ip='127.0.0.1'
    )
    order.thirdChargeNO = ch.id
    order.save()
    return HttpResponse(json.dumps(ch),content_type = "application/json")

@csrf_exempt
def getPayResult(request):
    response={}
    logger = logging.getLogger('Pack.app')
    logger.info('----------request--------------')
    logger.info(request.body)
    info = json.loads(request.body)
    logger.info(info)
    charge_succeeded = info['type']
    _chargeNO = info['data']['object']['id']
    if charge_succeeded == 'charge.succeeded':
        orderQuery = Order.objects.select_related().filter(thirdChargeNO = _chargeNO)
        if not orderQuery.exists():
            response['code'] = -1
            response['errorMessage'] = '获取chargeid失败'
            return HttpResponse(json.dumps(response),content_type="application/json")
        orderQuery.update(status = '1')
        saler = orderQuery[0].saler
        _deviceInfo = saler.deviceInfo
        if(len(_deviceInfo and "iOS") == 3):
            pushRst = pushAPN(saler.deviceToken,'0',str(orderQuery[0].id))
            logger.info(pushRst)
        elif(len(_deviceInfo and 'Android') == 7):
            pushRst = pushMessageToSingle(saler.clientID,'0',str(orderQuery[0].id))

        submitRecord = u'订单支付成功，请等待商家确认'
        record = OrderRecord(record = submitRecord,order=orderQuery[0],date = datetime.datetime.now())
        record.save()

        return HttpResponse('200')
    return HttpResponse('500')
