#encoding:utf-8
from django.http import HttpResponse
import sys,json,re,logging
from pack.models import Shop,Table,WaiterOrder,Cook,WaiterServe
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django.core.cache import cache

reload(sys)
sys.setdefaultencoding('utf8')


@csrf_exempt
def getShopWaiterOrderList(request):
    response = {}
    response['data'] = {}
    response['errorMsg'] = ""
    _shopId = request.session.get('shopId')
    if not _shopId:
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
    waiterOrderList = shop.waiterOrder_set.all()

    _waiterOrderList = []
    for waiterOrder in waiterOrderList:
        _waiterOrder = {}
        _waiterOrder['waiterOrderId'] = waiterOrder.id
        _waiterOrder['waiterOrderName'] = waiterOrder.name
        _waiterOrder['waiterOrderTelephone'] = waiterOrder.telephone
        _waiterOrderList.append(_waiterOrder)
    response['code'] = 0
    response['data'] = _waiterOrderList
    return HttpResponse(json.dumps(response,ensure_ascii=False),content_type="application/json")

@csrf_exempt
def getShopCookList(request):
    response = {}
    response['data'] = {}
    response['errorMsg'] = ""
    _shopId = request.session.get('shopId')
    if not _shopId:
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
    cookList = shop.cook_set.all()

    _cookList = []
    for cook in cookList:
        _cook = {}
        _cook['waiterOrderId'] = cook.id
        _cook['waiterOrderName'] = cook.name
        _cook['waiterOrderTelephone'] = cook.telephone
        _cookList.append(_cook)
    response['code'] = 0
    response['data'] = _cookList
    return HttpResponse(json.dumps(response,ensure_ascii=False),content_type="application/json")


@csrf_exempt
def getShopWaiterServeList(request):
    response = {}
    response['data'] = {}
    response['errorMsg'] = ""
    _shopId = request.session.get('shopId')
    if not _shopId:
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
    waiterServeList = shop.waiterServe_set.all()

    _waiterServeList = []
    for waiterServe in waiterServeList:
        _waiterServe = {}
        _waiterServe['waiterServeId'] = waiterServe.id
        _waiterServe['waiterServeName'] = waiterServe.name
        _waiterServe['waiterServeTelephone'] = waiterServe.telephone
        _waiterServeList.append(_waiterServe)
    response['code'] = 0
    response['data'] = _waiterServeList
    return HttpResponse(json.dumps(response,ensure_ascii=False),content_type="application/json")


@csrf_exempt
def verifyWaiterOrder(request):
    response = {}
    response['data'] = {}
    response['errorMsg'] = ""
    _shopId = request.session.get('shopId')
    if not _shopId:
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

    _telephone = request.REQUEST.get('telephone',18201637776)
    _verify_code = request.REQUEST.get('verifyCode',8888)
    cache.set(str(_telephone),str(_verify_code),1800)
    if _telephone == None or _telephone == '':
        response['code'] = -1
        response['errorMsg'] = u'请输入手机号'
        return HttpResponse(json.dumps(response,ensure_ascii=False),content_type="application/json")
    if  _verify_code == None or _verify_code == '':
        response['code'] = -1
        response['errorMsg'] = u'请输入验证码'
        return HttpResponse(json.dumps(response,ensure_ascii=False),content_type="application/json")

    _telephone = str(_telephone)
    _verify_code = str(_verify_code)
    if len(_telephone) != 11:
        response['code'] = -1
        response['errorMsg'] = '请输入11位手机号'
        return HttpResponse(json.dumps(response,ensure_ascii=False),content_type="application/json")
    if _telephone.isdigit() == False:
        response['code'] = -1
        response['errorMsg'] = '请输入有效的手机号'
        return HttpResponse(json.dumps(response,ensure_ascii=False),content_type="application/json")
    CM_prog = re.compile(r"^1(34[0-8]|(3[5-9]|5[017-9]|8[278])\d)\d{7}$")
    CU_prog = re.compile(r"^1(3[0-2]|5[256]|8[56])\d{8}$")
    CT_prog = re.compile(r"^1((33|53|8[09])[0-9]|349)\d{7}$")
    telephone_match_CM = CM_prog.match(_telephone)
    telephone_match_CU = CU_prog.match(_telephone)
    telephone_match_CT = CT_prog.match(_telephone)

    if not telephone_match_CM and not telephone_match_CT and not telephone_match_CU:
        response['code'] =  -1
        response['errorMsg'] = '请输入有效的手机号'
        return HttpResponse(json.dumps(response,ensure_ascii=False),content_type="application/json")
    saved_verify_code = cache.get(_telephone)
    if not saved_verify_code:
        response['code'] = -1
        response['errorMsg'] = '请重新发送验证码'
        return HttpResponse(json.dumps(response,ensure_ascii=False),content_type="application/json")
    if saved_verify_code != _verify_code:
        response['code'] = -1
        response['errorMsg'] = '验证码错误，请重新输入'
        return HttpResponse(json.dumps(response,ensure_ascii=False),content_type="application/json")
    query_wait_order = WaiterOrder.objects.filter(telephone = _telephone)
    if not query_wait_order.exists():
        _name = '****'+_telephone[7:11]
        _headImage = 'http://meiyue.b0.upaiyun.com/head/1_head.jpg'
        waiterOrder = WaiterOrder(telephone = _telephone, name = _name, headImage = _headImage,shop = shop)
        waiterOrder.save()
        response['code'] = 0
        response_data = {}
        response_data['waiterOrderId'] = waiterOrder.id
        response_data['waiterOrderName'] = waiterOrder.name
        response_data['waiterOrderTelepohone'] = waiterOrder.telephone
        response['data'] = response_data
        return HttpResponse(json.dumps(response,ensure_ascii=False),content_type="application/json")
    waiterOrder = query_wait_order[0]
    waiterOrder.shop = shop
    waiterOrder.save()
    response['code'] = 0
    response_data = {}
    response_data['waiterOrderId'] = waiterOrder.id
    response_data['waiterOrderName'] = waiterOrder.name
    response_data['waiterOrderTelepohone'] = waiterOrder.telephone
    response['data'] = response_data
    return HttpResponse(json.dumps(response,ensure_ascii=False),content_type="application/json")


@csrf_exempt
def verifyCook(request):
    response = {}
    response['data'] = {}
    response['errorMsg'] = ""
    _shopId = request.session.get('shopId')
    if not _shopId:
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

    _telephone = request.REQUEST.get('telephone',18201637776)
    _verify_code = request.REQUEST.get('verifyCode',8888)
    cache.set(str(_telephone),str(_verify_code),1800)
    if _telephone == None or _telephone == '':
        response['code'] = -1
        response['errorMsg'] = u'请输入手机号'
        return HttpResponse(json.dumps(response,ensure_ascii=False),content_type="application/json")
    if  _verify_code == None or _verify_code == '':
        response['code'] = -1
        response['errorMsg'] = u'请输入验证码'
        return HttpResponse(json.dumps(response,ensure_ascii=False),content_type="application/json")

    _telephone = str(_telephone)
    _verify_code = str(_verify_code)
    if len(_telephone) != 11:
        response['code'] = -1
        response['errorMsg'] = '请输入11位手机号'
        return HttpResponse(json.dumps(response,ensure_ascii=False),content_type="application/json")
    if _telephone.isdigit() == False:
        response['code'] = -1
        response['errorMsg'] = '请输入有效的手机号'
        return HttpResponse(json.dumps(response,ensure_ascii=False),content_type="application/json")
    CM_prog = re.compile(r"^1(34[0-8]|(3[5-9]|5[017-9]|8[278])\d)\d{7}$")
    CU_prog = re.compile(r"^1(3[0-2]|5[256]|8[56])\d{8}$")
    CT_prog = re.compile(r"^1((33|53|8[09])[0-9]|349)\d{7}$")
    telephone_match_CM = CM_prog.match(_telephone)
    telephone_match_CU = CU_prog.match(_telephone)
    telephone_match_CT = CT_prog.match(_telephone)

    if not telephone_match_CM and not telephone_match_CT and not telephone_match_CU:
        response['code'] =  -1
        response['errorMsg'] = '请输入有效的手机号'
        return HttpResponse(json.dumps(response,ensure_ascii=False),content_type="application/json")
    saved_verify_code = cache.get(_telephone)
    if not saved_verify_code:
        response['code'] = -1
        response['errorMsg'] = '请重新发送验证码'
        return HttpResponse(json.dumps(response,ensure_ascii=False),content_type="application/json")
    if saved_verify_code != _verify_code:
        response['code'] = -1
        response['errorMsg'] = '验证码错误，请重新输入'
        return HttpResponse(json.dumps(response,ensure_ascii=False),content_type="application/json")
    query_cook = Cook.objects.filter(telephone = _telephone)
    if not query_cook.exists():
        _name = '****'+_telephone[7:11]
        _headImage = 'http://meiyue.b0.upaiyun.com/head/1_head.jpg'
        cook = Cook(telephone = _telephone, name = _name, headImage = _headImage,shop = shop)
        cook.save()
        response['code'] = 0
        response_data = {}
        response_data['waiterOrderId'] = cook.id
        response_data['waiterOrderName'] = cook.name
        response_data['waiterOrderTelepohone'] = cook.telephone
        response['data'] = response_data
        return HttpResponse(json.dumps(response,ensure_ascii=False),content_type="application/json")
    cook = query_cook[0]
    cook.shop = shop
    cook.save()
    response['code'] = 0
    response_data = {}
    response_data['waiterOrderId'] = cook.id
    response_data['waiterOrderName'] = cook.name
    response_data['waiterOrderTelepohone'] = cook.telephone
    response['data'] = response_data
    return HttpResponse(json.dumps(response,ensure_ascii=False),content_type="application/json")

@csrf_exempt
def verifyWaiterServe(request):
    response = {}
    response['data'] = {}
    response['errorMsg'] = ""
    _shopId = request.session.get('shopId')
    if not _shopId:
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

    _telephone = request.REQUEST.get('telephone',18201637776)
    _verify_code = request.REQUEST.get('verifyCode',8888)
    cache.set(str(_telephone),str(_verify_code),1800)
    if _telephone == None or _telephone == '':
        response['code'] = -1
        response['errorMsg'] = u'请输入手机号'
        return HttpResponse(json.dumps(response,ensure_ascii=False),content_type="application/json")
    if  _verify_code == None or _verify_code == '':
        response['code'] = -1
        response['errorMsg'] = u'请输入验证码'
        return HttpResponse(json.dumps(response,ensure_ascii=False),content_type="application/json")

    _telephone = str(_telephone)
    _verify_code = str(_verify_code)
    if len(_telephone) != 11:
        response['code'] = -1
        response['errorMsg'] = '请输入11位手机号'
        return HttpResponse(json.dumps(response,ensure_ascii=False),content_type="application/json")
    if _telephone.isdigit() == False:
        response['code'] = -1
        response['errorMsg'] = '请输入有效的手机号'
        return HttpResponse(json.dumps(response,ensure_ascii=False),content_type="application/json")
    CM_prog = re.compile(r"^1(34[0-8]|(3[5-9]|5[017-9]|8[278])\d)\d{7}$")
    CU_prog = re.compile(r"^1(3[0-2]|5[256]|8[56])\d{8}$")
    CT_prog = re.compile(r"^1((33|53|8[09])[0-9]|349)\d{7}$")
    telephone_match_CM = CM_prog.match(_telephone)
    telephone_match_CU = CU_prog.match(_telephone)
    telephone_match_CT = CT_prog.match(_telephone)

    if not telephone_match_CM and not telephone_match_CT and not telephone_match_CU:
        response['code'] =  -1
        response['errorMsg'] = '请输入有效的手机号'
        return HttpResponse(json.dumps(response,ensure_ascii=False),content_type="application/json")
    saved_verify_code = cache.get(_telephone)
    if not saved_verify_code:
        response['code'] = -1
        response['errorMsg'] = '请重新发送验证码'
        return HttpResponse(json.dumps(response,ensure_ascii=False),content_type="application/json")
    if saved_verify_code != _verify_code:
        response['code'] = -1
        response['errorMsg'] = '验证码错误，请重新输入'
        return HttpResponse(json.dumps(response,ensure_ascii=False),content_type="application/json")
    query_wait_serve = WaiterServe.objects.filter(telephone = _telephone)
    if not query_wait_serve.exists():
        _name = '****'+_telephone[7:11]
        _headImage = 'http://meiyue.b0.upaiyun.com/head/1_head.jpg'
        waiterServe = WaiterServe(telephone = _telephone, name = _name, headImage = _headImage,shop = shop)
        waiterServe.save()
        response['code'] = 0
        response_data = {}
        response_data['waiterOrderId'] = waiterServe.id
        response_data['waiterOrderName'] = waiterServe.name
        response_data['waiterOrderTelepohone'] = waiterServe.telephone
        response['data'] = response_data
        return HttpResponse(json.dumps(response,ensure_ascii=False),content_type="application/json")
    waiterServe = query_wait_serve[0]
    waiterServe.shop = shop
    waiterServe.save()
    response['code'] = 0
    response_data = {}
    response_data['waiterOrderId'] = waiterServe.id
    response_data['waiterOrderName'] = waiterServe.name
    response_data['waiterOrderTelepohone'] = waiterServe.telephone
    response['data'] = response_data
    return HttpResponse(json.dumps(response,ensure_ascii=False),content_type="application/json")
