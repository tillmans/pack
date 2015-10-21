#encoding:utf-8
from django.http import HttpResponse
import sys,json
from pack.models import Sku,Category,WaiterOrder
from django.views.decorators.csrf import csrf_exempt
import logging
from django.core.exceptions import ObjectDoesNotExist

reload(sys)
sys.setdefaultencoding('utf8')


@csrf_exempt
def getCategories(request):
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

    _shopId = request.REQUEST.get('shopId')
    if _shopId == None or _shopId == '':
        response['code'] = -1
        response['errorMsg'] = '获取商家信息失败'
        return HttpResponse(json.dumps(response,ensure_ascii=False),content_type="application/json")
    _shopId = int(_shopId)
    if _shopId != str(waiterOrder.id):
        response['code'] = -1
        response['errorMsg'] = '账户不对应'
        return HttpResponse(json.dumps(response,ensure_ascii=False),content_type="application/json")

    categories = Category.objects.filter(shop__id = _shopId).order_by('-id')
    response_categories = []
    for category in categories:
        response_category={}
        response_category['categoryName'] = category.categoryName
        response_category['categoryId'] = category.id
        response_categories.append(response_category)
    response['code'] = 0
    response['data'] = response_categories
    return HttpResponse(json.dumps(response,ensure_ascii=False),content_type="application/json")

@csrf_exempt
def getShopSkusWithCategory(request):
    response = {}
    response_data = {}
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

    _shopId = request.REQUEST.get('shopId')
    if _shopId == None or _shopId == '':
        response['code'] = -1
        response['errorMsg'] = '获取商家信息失败'
        return HttpResponse(json.dumps(response,ensure_ascii=False),content_type="application/json")
    _shopId = int(_shopId)
    if _shopId != str(waiterOrder.id):
        response['code'] = -1
        response['errorMsg'] = '账户不对应'
        return HttpResponse(json.dumps(response,ensure_ascii=False),content_type="application/json")

    _categoryId =request.REQUEST.get('categoryId')
    if _categoryId == None or _categoryId == '':
        response['code'] = -1
        response['errorMsg'] = '获取品类id失败'
        return HttpResponse(json.dumps(response),content_type="application/json")

    skuQuery = Sku.objects.filter(isValid = True).filter(category_id = _categoryId).order_by('id')
    if not skuQuery.exists():
        response['code'] = 0
        response['data'] = {'skus':[]}
        return HttpResponse(json.dumps(response),content_type="application/json")
    skus = skuQuery.reverse()

    response_data_skus = []
    for sku in skus:
        response_data_sku = {}
        response_data_sku['skuId'] = sku.id
        response_data_sku['skuName'] = sku.name.encode('utf-8')
        response_data_sku['skuDesc'] = sku.description.encode('utf-8')
        _img = sku.img.split(',')
        response_data_sku['skuImg'] = _img[0]
        _skuSizeList = sku.skuSize_set.all()
        response_data_sku_size_list = []
        flag = 0
        for skuSize in _skuSizeList:
            if flag == 0:
                response_data_sku['skuPriceDesc'] = str(skuSize.price)
                flag = 1
            response_data_sku_size = {}
            response_data_sku_size['skuSizeid'] = skuSize.id
            response_data_sku_size['skuSizeName'] = skuSize.sizeName.encode('utf-8')
            response_data_sku_size['skuPrice'] = str(skuSize.price)
            response_data_sku_size_list.append(response_data_sku_size)
        response_data_sku['skuSizeList'] = response_data_sku_size_list
        response_data_sku_size_list_count = len(response_data_sku_size_list)
        if response_data_sku_size_list_count > 1:
            response_data['skuPriceDesc'] = str(response_data_sku_size_list_count)
        response_data_sku['skuSizeListCount'] = str(response_data_sku_size_list_count)
        response_data_skus.append(response_data_sku)
    response_data['skus'] = response_data_skus
    response['code'] = 0
    response['data'] = response_data_skus
    return HttpResponse(json.dumps(response),content_type="application/json")



@csrf_exempt
def getShopSkus(request):
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

    _shopId = request.REQUEST.get('shopId')
    if _shopId == None or _shopId == '':
        response['code'] = -1
        response['errorMsg'] = '获取商家信息失败'
        return HttpResponse(json.dumps(response,ensure_ascii=False),content_type="application/json")
    _shopId = int(_shopId)
    if _shopId != str(waiterOrder.id):
        response['code'] = -1
        response['errorMsg'] = '账户不对应'
        return HttpResponse(json.dumps(response,ensure_ascii=False),content_type="application/json")

    categoryQuery = Category.objects.select_related().filter(shop__id = _shopId)
    response_categories = []
    for category in categoryQuery:
        response_category = {}
        response_category['categoryId'] = category.id
        response_category['categoryName'] = category.categoryName
        skus = category.sku_set.filter(isValid=True).order_by('id')
        response_category_skus = []
        for sku in skus:
            response_category_sku = {}
            response_category_sku['skuId'] = sku.id
            response_category_sku['skuName'] = sku.name.encode('utf-8')
            response_category_sku['skuDesc'] = sku.description.encode('utf-8')
            _img = sku.img.split(',')
            response_category_sku['skuImg'] = _img[0]
            _skuSizeList = sku.skuSize_set.all()
            response_category_sku_size_list = []
            flag = 0
            for skuSize in _skuSizeList:
                if flag == 0:
                    response_category_sku['skuPriceDesc'] = str(skuSize.price)
                    flag = 1
                response_category_sku_size = {}
                response_category_sku_size['skuSizeid'] = skuSize.id
                response_category_sku_size['skuSizeName'] = skuSize.sizeName.encode('utf-8')
                response_category_sku_size['skuPrice'] = str(skuSize.price)
                response_category_sku_size_list.append(response_category_sku_size)
            response_category_sku['skuSizeList'] = response_category_sku_size_list
            response_category_sku_size_list_count = len(response_category_sku_size_list)
            if response_category_sku_size_list_count > 1:
                response_category_sku['skuPriceDesc'] = str(response_category_sku_size_list_count)
            response_category_sku['skuSizeListCount'] = str(response_category_sku_size_list_count)
            response_category_skus.append(response_category_sku)
        response_category['skus'] = response_category_skus
        response_categories.append(response_category)
    response['code'] = 0
    response['data'] = response_categories
    return HttpResponse(json.dumps(response),content_type="application/json")


