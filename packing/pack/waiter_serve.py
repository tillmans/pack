#encoding:utf-8
from django.http import HttpResponse
import sys,json
from pack.models import WaiterServe,WaiterServeFeedBack
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
import logging

reload(sys)
sys.setdefaultencoding('utf8')


@csrf_exempt
def waiterServeInfo(request):
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


        waiterServe.name = _name
        waiterServe.headImage = _headImage
        waiterServe.save()

        response['code'] = 0
        response_data = {}
        response_data['name'] = waiterServe.name.encode('utf-8')
        response_data['telephone'] = waiterServe.telephone
        response_data['headImage'] = waiterServe.headImage
        if waiterServe.saler == None:
            response_salerInfo = {}
            response_salerInfo['salerId'] = ''
            response_salerInfo['salerName'] = ''
            response_salerInfo['salertelephone'] = ''
            response_data['salerInfo'] = response_salerInfo
            response['data'] = response_data
            return HttpResponse(json.dumps(response),content_type="application/json")
        else:
            response_salerInfo = {}
            response_salerInfo['salerId'] = str(waiterServe.saler.id)
            response_salerInfo['salerName'] = str(waiterServe.saler.name)
            response_salerInfo['salertelephone'] = str(waiterServe.saler.telephone)
            response_data['salerInfo'] = response_salerInfo
            response['data'] = response_data
            return HttpResponse(json.dumps(response),content_type="application/json")
    else:
        response['code'] = 0
        response_data = {}
        response_data['name'] = waiterServe.name.encode('utf-8')
        response_data['telephone'] = waiterServe.telephone
        response_data['headImage'] = waiterServe.headImage
        if waiterServe.saler == None:
            response_salerInfo = {}
            response_salerInfo['salerId'] = ''
            response_salerInfo['salerName'] = ''
            response_salerInfo['salertelephone'] = ''
            response_data['salerInfo'] = response_salerInfo
            response['data'] = response_data
            return HttpResponse(json.dumps(response),content_type="application/json")
        else:
            response_salerInfo = {}
            response_salerInfo['salerId'] = str(waiterServe.saler.id)
            response_salerInfo['salerName'] = str(waiterServe.saler.name)
            response_salerInfo['salertelephone'] = str(waiterServe.saler.telephone)
            response_data['salerInfo'] = response_salerInfo
            response['data'] = response_data
            return HttpResponse(json.dumps(response),content_type="application/json")



@csrf_exempt
def waiterServeFeedback(request):
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
        waiterServe = WaiterServe.objects.get(id = _waiterServeId)
    except ObjectDoesNotExist:
        response['code'] = 1
        response['errorMsg'] = '请先登录'
        return HttpResponse(json.dumps(response,ensure_ascii=False),content_type="application/json")
    if _lastLoginTime != waiterServe.lastLoginTime:
        response['code'] = 1
        response['errorMsg'] = '上次登录失效，请重新登录'
        return HttpResponse(json.dumps(response),content_type="application/json")
    ####################END#################

    _msg = request.REQUEST.get('msg')
    if _msg == None or _msg == '':
        response['code'] = -1
        response['errorMsg'] = '请输入改进意见'
        return HttpResponse(json.dumps(response),content_type="application/json")
    waiterServeFeedback = WaiterServeFeedBack(waiterServe = waiterServe, msg = _msg)
    waiterServeFeedback.save()
    response['code'] = 0
    return HttpResponse(json.dumps(response),content_type="application/json")



@csrf_exempt
def waiterServeUpdateClientID(request):
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
        waiterServe = WaiterServe.objects.get(id = _waiterServeId)
    except ObjectDoesNotExist:
        response['code'] = 1
        response['errorMsg'] = '请先登录'
        return HttpResponse(json.dumps(response,ensure_ascii=False),content_type="application/json")
    if _lastLoginTime != waiterServe.lastLoginTime:
        response['code'] = 1
        response['errorMsg'] = '上次登录失效，请重新登录'
        return HttpResponse(json.dumps(response),content_type="application/json")
    ####################END#################


    _clientID = request.REQUEST.get('clientID')
    if _clientID == None or _clientID == '':
        response['code'] = -1
        response['errorMsg'] = '请上传clientID'
        return HttpResponse(json.dumps(response,ensure_ascii=False),content_type="application/json")

    if waiterServe.clientID != _clientID:
        waiterServe.clientID = _clientID
        waiterServe.save()
    response['code'] = 0
    response['data'] = {'clientID':_clientID}
    response['errorMsg'] = ''
    return HttpResponse(json.dumps(response),content_type="application/json")
