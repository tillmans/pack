#encoding:utf-8
from django.http import HttpResponse
import sys,json
from pack.models import WaiterOrder,WaiterOrderFeedBack
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
import logging

reload(sys)
sys.setdefaultencoding('utf8')


@csrf_exempt
def waiterOrderInfo(request):
    logger = logging.getLogger('Pack.app')
    response = {}
    response['data'] = {}
    response['errorMsg'] = ""
    _waiterOrderId = request.session.get('waiterOrderId')
    if not _waiterOrderId:
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
        waiterOrder = WaiterOrder.select_related().objects.get(id = _waiterOrderId)
    except ObjectDoesNotExist:
        response['code'] = 1
        response['errorMsg'] = '请先登录'
        return HttpResponse(json.dumps(response,ensure_ascii=False),content_type="application/json")
    if _lastLoginTime != waiterOrder.lastLoginTime:
        response['code'] = 1
        response['errorMsg'] = '上次登录失效，请重新登录'
        return HttpResponse(json.dumps(response),content_type="application/json")
    ####################END#################


    _method = request.REQUEST.get('method')
    if _method == None or _method == '':
        response['code'] = -1
        response['errorMsg'] = '获取method失败'
        return HttpResponse(json.dumps(response,ensure_ascii=False),content_type="application/json")
    _method = str(_method)

    #if method = 1,update; method = 2, query
    if _method == '1':
        _name = request.REQUEST.get('name')
        _headImage = request.REQUEST.get('headImage')


        if _name == None or _name == '':
            response['code'] = -1
            response['errorMsg'] = '请输入店铺名字'
            return HttpResponse(json.dumps(response,ensure_ascii=False),content_type="application/json")
        if _headImage == None or _headImage == '':
            _headImage = 'http://meiyue.b0.upaiyun.com/head/1_head.jpg'


        waiterOrder.name = _name
        waiterOrder.headImage = _headImage
        waiterOrder.save()

        response['code'] = 0
        response_data = {}
        response_data['name'] = waiterOrder.name.encode('utf-8')
        response_data['telephone'] = waiterOrder.telephone
        response_data['headImage'] = waiterOrder.headImage
        if waiterOrder.saler == None:
            response_salerInfo = {}
            response_salerInfo['salerId'] = ''
            response_salerInfo['salerName'] = ''
            response_salerInfo['salertelephone'] = ''
            response_data['salerInfo'] = response_salerInfo
            response['data'] = response_data
            return HttpResponse(json.dumps(response),content_type="application/json")

        else:
            response_salerInfo = {}
            response_salerInfo['salerId'] = str(waiterOrder.saler.id)
            response_salerInfo['salerName'] = str(waiterOrder.saler.name)
            response_salerInfo['salertelephone'] = str(waiterOrder.saler.telephone)
            response_data['salerInfo'] = response_salerInfo
            response['data'] = response_data
            return HttpResponse(json.dumps(response),content_type="application/json")
    else:
        response['code'] = 0
        response_data = {}
        response_data['name'] = waiterOrder.name.encode('utf-8')
        response_data['telephone'] = waiterOrder.telephone
        response_data['headImage'] = waiterOrder.headImage
        response_salerInfo = {}
        response_salerInfo['salerId'] = str(waiterOrder.saler.id)
        response_salerInfo['salerName'] = str(waiterOrder.saler.name)
        response_salerInfo['salertelephone'] = str(waiterOrder.saler.telephone)
        response_data['salerInfo'] = response_salerInfo
        response['data'] = response_data
        return HttpResponse(json.dumps(response),content_type="application/json")



@csrf_exempt
def waiterOrderFeedback(request):
    response = {}
    response['data'] = {}
    response['errorMsg'] = ""
    _waiterOrderId = request.session.get('waiterOrderId')
    if not _waiterOrderId:
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
        waiterOrder = WaiterOrder.objects.get(id = _waiterOrderId)
    except ObjectDoesNotExist:
        response['code'] = 1
        response['errorMsg'] = '请先登录'
        return HttpResponse(json.dumps(response,ensure_ascii=False),content_type="application/json")
    if _lastLoginTime != waiterOrder.lastLoginTime:
        response['code'] = 1
        response['errorMsg'] = '上次登录失效，请重新登录'
        return HttpResponse(json.dumps(response),content_type="application/json")
    ####################END#################

    _msg = request.REQUEST.get('msg')
    if _msg == None or _msg == '':
        response['code'] = -1
        response['errorMsg'] = '请输入改进意见'
        return HttpResponse(json.dumps(response),content_type="application/json")
    waiterOrderFeedback = WaiterOrderFeedBack(waiterOrder = waiterOrder, msg = _msg)
    waiterOrderFeedback.save()
    response['code'] = 0
    return HttpResponse(json.dumps(response),content_type="application/json")



@csrf_exempt
def waiterOrderUpdateClientID(request):
    response = {}
    response['data'] = {}
    response['errorMsg'] = ""
    _waiterOrderId = request.session.get('waiterOrderId')
    if not _waiterOrderId:
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
        waiterOrder = WaiterOrder.objects.get(id = _waiterOrderId)
    except ObjectDoesNotExist:
        response['code'] = 1
        response['errorMsg'] = '请先登录'
        return HttpResponse(json.dumps(response,ensure_ascii=False),content_type="application/json")
    if _lastLoginTime != waiterOrder.lastLoginTime:
        response['code'] = 1
        response['errorMsg'] = '上次登录失效，请重新登录'
        return HttpResponse(json.dumps(response),content_type="application/json")
    ####################END#################


    _clientID = request.REQUEST.get('clientID')
    if _clientID == None or _clientID == '':
        response['code'] = -1
        response['errorMsg'] = '请上传clientID'
        return HttpResponse(json.dumps(response,ensure_ascii=False),content_type="application/json")

    if waiterOrder.clientID != _clientID:
        waiterOrder.clientID = _clientID
        waiterOrder.save()
    response['code'] = 0
    response['data'] = {'clientID':_clientID}
    response['errorMsg'] = ''
    return HttpResponse(json.dumps(response),content_type="application/json")
