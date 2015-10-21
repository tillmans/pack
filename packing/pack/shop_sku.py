#encoding:utf-8
from django.http import HttpResponse
import sys,json
from pack.models import Shop,Sku,SkuSize,Category
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

    categories = Category.objects.filter(shop = shop).order_by('-id')
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
def categoryInfo(request):
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

    _method = request.REQUEST.get('method')
    if _method == None or _method == '':
        response['code'] = -1
        response['errorMsg'] = '获取method失败'
        return HttpResponse(json.dumps(response,ensure_ascii=False),content_type="application/json")
    _method = str(_method)
    if _method == '0':
        _name = request.REQUEST.get('categoryName')
        if _name == None or _name == '':
            response['code'] = -1
            response['errorMsg'] = '请输入名字'
            return HttpResponse(json.dumps(response,ensure_ascii=False),content_type="application/json")

        category = Category(categoryName = _name,shop = shop)
        try:
            category.save()
        except Exception,e:
            print('e')
            response['code'] = -1
            response['errorMsg'] = '保存类别失败'
            return HttpResponse(json.dumps(response),content_type="application/json")
        response['code'] = 0
        response['data'] = {"categoryName":category.categoryName,"categoryId":category.id}
        return HttpResponse(json.dumps(response),content_type="application/json")
    elif _method == '1':
        _categoryId = request.REQUEST.get('categoryId')
        _categoryName = request.REQUEST.get('categoryName')
        if _categoryName == None or _categoryName == '':
            response['code'] = -1
            response['errorMsg'] = '请输入名字'
            return HttpResponse(json.dumps(response,ensure_ascii=False),content_type="application/json")
        if _categoryId == None or _categoryId == '':
            response['code'] = -1
            response['errorMsg'] = '请输入类别id'
            return HttpResponse(json.dumps(response,ensure_ascii=False),content_type="application/json")
        _categoryId = str(_categoryId)
        _categoryName = str(_categoryName)
        try:
            category = Category.objects.get(id = _categoryId)
        except ObjectDoesNotExist:
            response['code'] = 1
            response['errorMsg'] = '获取类别失败'
            return HttpResponse(json.dumps(response,ensure_ascii=False),content_type="application/json")
        category.categoryName = _categoryName
        category.save()
        try:
            category.save()
        except Exception,e:
            print('e')
            response['code'] = -1
            response['errorMsg'] = '保存类别失败'
            return HttpResponse(json.dumps(response),content_type="application/json")
        response['code'] = 0
        response['data'] = {"categoryName":category.categoryName,"categoryId":category.id}
        return HttpResponse(json.dumps(response),content_type="application/json")
    else:
        response['code'] = -1
        response['errorMsg'] = '获取method失败'
        return HttpResponse(json.dumps(response),content_type="application/json")


@csrf_exempt
def skuInfo(request):
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

    _method = request.REQUEST.get('method')
    if _method == None or _method == '':
        response['code'] = -1
        response['errorMsg'] = '获取method失败'
        return HttpResponse(json.dumps(response,ensure_ascii=False),content_type="application/json")
    _method = str(_method)

    #if method = 0 , add; method = 1, update; method = 2 , queryOne; method = 3, delete
    if _method == '0':
        _name = request.REQUEST.get('skuName')
        _desc = request.REQUEST.get('skuDesc')
        _categoryId = request.REQUEST.get('categoryId')
        _img = request.REQUEST.get('skuImg')
        _skuSizeList = request.get('skuSizeList')
        __skuSizeList = json.loads(_skuSizeList)

        if _name == None or _name == '':
            response['code'] = -1
            response['errorMsg'] = '请输入名字'
            return HttpResponse(json.dumps(response),content_type="application/json")
        if _desc == None:
            _desc = ''
        if _categoryId == None or _categoryId == '':
            response['code'] = -1
            response['errorMsg'] = '请选择品类'
            return HttpResponse(json.dumps(response),content_type="application/json")
        if _img == None or _img == '':
            response['code'] = -1
            response['errorMsg'] = '请上传图片'
            return HttpResponse(json.dumps(response),content_type="application/json")


        try:
            category = Category.objects.get(id = str(_categoryId))
        except ObjectDoesNotExist:
            response['code'] = -1
            response['errorMsg'] = '获取品类失败'
            return HttpResponse(json.dumps(response,ensure_ascii=False),content_type="application/json")

        if category.shop.id != _shopId:
            response['code'] = -1
            response['errorMsg'] = '获取品类失败'
            return HttpResponse(json.dumps(response,ensure_ascii=False),content_type="application/json")
        sku = Sku(name = _name, desc = _desc, img = _img, category = category)
        sku.save()
        response_data = {}
        response_data['skuId'] = sku.id
        response_data['skuName'] = sku.name.encode('utf-8')
        response_data['skuDesc'] = sku.desc.encode('utf-8')
        response_data['skuImg'] = sku.img

        response_sku_size_list = []
        for _skuSize in __skuSizeList:
            response_sku_size = {}
            _sizeName = _skuSize['skuSizeName']
            _price = _skuSize['skuPrice']
            skuSize = SkuSize(sku = sku, name = _sizeName, price = _price)
            skuSize.save()
            response_sku_size['skuSizeId'] = skuSize.id
            response_sku_size['skuSizeName'] = skuSize.name.encode('utf-8')
            response_sku_size['skuPrice'] = str(skuSize.price)
            response_sku_size_list.append(response_sku_size)
        response_data['skuSizeList'] = response_sku_size_list
        response['code'] = 0
        response['data'] = response_data
        return HttpResponse(json.dumps(response),content_type="application/json")

    elif _method == '1':
        _skuId = request.REQUEST.get('skuId')
        _name = request.REQUEST.get('skuName')
        _desc = request.REQUEST.get('skuDesc')
        _img = request.REQUEST.get('skuImg')
        _skuSizeList = request.get('skuSizeList')
        __skuSizeList = json.loads(_skuSizeList)

        if _name == None or _name == '':
            response['code'] = -1
            response['errorMsg'] = '请输入名字'
            return HttpResponse(json.dumps(response),content_type="application/json")
        if _desc == None:
            _desc = ''
        if _img == None or _img == '':
            response['code'] = -1
            response['errorMsg'] = '请上传图片'
            return HttpResponse(json.dumps(response),content_type="application/json")
        if _skuId == None or _skuId == '':
            response['code'] = -1
            response['errorMsg'] = '商品id为空'
            return HttpResponse(json.dumps(response),content_type="application/json")

        try:
            sku = Sku.select_related().objects.get(id = _skuId)
        except ObjectDoesNotExist:
            response['code'] = -1
            response['errorMsg'] = '商品查询失败'
            return HttpResponse(json.dumps(response),content_type="application/json")
        
        sku.name = _name
        sku.desc = _desc
        sku.img = _img
        sku.save()

        response['code'] = 0
        response_data = {}
        response_data['skuId'] = sku.id
        response_data['skuName'] = sku.name.encode('utf-8')
        response_data['skuDesc'] = sku.description.encode('utf-8')
        _img = sku.img.split(',')
        response_data['skuImg'] = _img[0]

        _skuSizeList = sku.skuSize_set.all()
        response_sku_size_list = []
        for skuSize in _skuSizeList:
            response_sku_size = {}
            response_sku_size['skuSizeid'] = skuSize.id
            response_sku_size['skuSizeName'] = skuSize.name.encode('utf-8')
            response_sku_size['skuPrice'] = str(skuSize.price)
            response_sku_size_list.append(response_sku_size)
        response_data['skuSizeList'] = response_sku_size_list
        response['code'] = 0
        response['data'] = response_data
        return HttpResponse(json.dumps(response),content_type="application/json")
    elif _method == '2':
        _skuId = request.REQUEST.get('skuId')
        if _skuId == None or _skuId == '':
            response['code'] = -1
            response['errorMsg'] = '商品id为空'
            return HttpResponse(json.dumps(response),content_type="application/json")

        try:
            sku = Sku.select_related().objects.get(id = _skuId)
        except ObjectDoesNotExist:
            response['code'] = -1
            response['errorMsg'] = '商品查询失败'
            return HttpResponse(json.dumps(response),content_type="application/json")

        response['code'] = 0
        response_data = {}
        response_data['skuId'] = sku.id
        response_data['skuName'] = sku.name.encode('utf-8')
        response_data['skuDesc'] = sku.desc.encode('utf-8')
        _img = sku.img.split(',')
        response_data['skuImg'] = _img[0]
        _skuSizeList = sku.skuSize_set.all()
        response_sku_size_list = []
        for skuSize in _skuSizeList:
            response_sku_size = {}
            response_sku_size['skuSizeId'] = skuSize.id
            response_sku_size['skuSizeName'] = skuSize.name.encode('utf-8')
            response_sku_size['skuSizePrice'] = str(skuSize.price)
            response_sku_size_list.append(response_sku_size)
        response_data['skuSizeList'] = response_sku_size_list
        response['data'] = response_data
        return HttpResponse(json.dumps(response),content_type="application/json")
    elif _method == '3':
        _skuId = request.REQUEST.get('skuId')
        if _skuId == None or _skuId == '':
            response['code'] = -1
            response['errorMsg'] = '商品id为空'
            return HttpResponse(json.dumps(response),content_type="application/json")

        try:
            sku = Sku.select_related().objects.get(id = _skuId)
        except ObjectDoesNotExist:
            response['code'] = -1
            response['errorMsg'] = '商品查询失败'
            return HttpResponse(json.dumps(response),content_type="application/json")
        sku.isValid = False
        sku.save()
        response['code'] = 0
        return HttpResponse(json.dumps(response),content_type="application/json")

@csrf_exempt
def alterSkuName(request):
    logger = logging.getLogger('Pack.app')
    logger.info(request.REQUEST)
    response = {}
    response['data'] = {}
    response['errorMsg'] = ""
    response_data = {}
    _shopId = request.session.get('shopId')
    _shopId = str(_shopId)
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

    _skuId = request.REQUEST.get('skuId')
    _skuName = request.REQUEST.get('skuName')

    if _skuId == None or _skuId == '':
        response['code'] = -1
        response['errorMsg'] = '商品id为空'
        return HttpResponse(json.dumps(response),content_type="application/json")
    if _skuName == None or _skuName == '':
        response['code'] = -1
        response['errorMsg'] = '请输入名字'
        return HttpResponse(json.dumps(response),content_type="application/json")
    _skuId = str(_skuId)
    _skuName = str(_skuName)

    try:
        sku = Sku.select_related().objects.get(id = _skuId)
    except ObjectDoesNotExist:
        response['code'] = -1
        response['errorMsg'] = '商品查询失败'
        return HttpResponse(json.dumps(response),content_type="application/json")

    sku.name = _skuName
    sku.save()
    response['code'] = 0
    response['data'] = sku.name.encode('utf-8')
    return HttpResponse(json.dumps(response),content_type="application/json")


@csrf_exempt
def alterSkuImg(request):
    logger = logging.getLogger('Pack.app')
    logger.info(request.REQUEST)
    response = {}
    response['data'] = {}
    response['errorMsg'] = ""
    response_data = {}
    _shopId = request.session.get('shopId')
    _shopId = str(_shopId)
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

    _skuId = request.REQUEST.get('skuId')
    _skuImg = request.REQUEST.get('skuImg')

    if _skuId == None or _skuId == '':
        response['code'] = -1
        response['errorMsg'] = '商品id为空'
        return HttpResponse(json.dumps(response),content_type="application/json")
    if _skuImg == None or _skuImg == '':
        response['code'] = -1
        response['errorMsg'] = '图片url为空'
        return HttpResponse(json.dumps(response),content_type="application/json")
    _skuId = str(_skuId)
    _skuImg = str(_skuImg)

    try:
        sku = Sku.select_related().objects.get(id = _skuId)
    except ObjectDoesNotExist:
        response['code'] = -1
        response['errorMsg'] = '商品查询失败'
        return HttpResponse(json.dumps(response),content_type="application/json")

    sku.img = _skuImg
    sku.save()
    response['code'] = 0
    response['data'] = sku.img
    return HttpResponse(json.dumps(response),content_type="application/json")

@csrf_exempt
def addSkuSize(request):
    logger = logging.getLogger('Pack.app')
    logger.info(request.REQUEST)
    response = {}
    response['data'] = {}
    response['errorMsg'] = ""
    response_data = {}
    _shopId = request.session.get('shopId')
    _shopId = str(_shopId)
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

    _skuId = request.REQUEST.get('skuId')
    _skuSizeName = request.REQUEST.get('skuSizeName')
    _skuSizePrice = request.REQUEST.get('skuSizePrice')

    if _skuId == None or _skuId == '':
        response['code'] = -1
        response['errorMsg'] = 'skuSizeId为空'
        return HttpResponse(json.dumps(response),content_type="application/json")
    if _skuSizeName == None or _skuSizeName == '':
        response['code'] = -1
        response['errorMsg'] = 'skuSizeId为空'
        return HttpResponse(json.dumps(response),content_type="application/json")
    if _skuSizePrice == None or _skuSizePrice == '':
        response['code'] = -1
        response['errorMsg'] = 'skuSizeId为空'
        return HttpResponse(json.dumps(response),content_type="application/json")
    _skuId = str(_skuId)
    _skuSizeName = str(_skuSizeName)
    _skuSizePrice = str(_skuSizePrice)

    try:
        sku = Sku.objects.get(id = _skuId)
    except ObjectDoesNotExist:
        response['code'] = -1
        response['errorMsg'] = '商品查询失败'
        return HttpResponse(json.dumps(response),content_type="application/json")
    skuSize = SkuSize(name = _skuSizeName, price = _skuSizePrice, sku = sku)
    skuSize.save()
    response['code'] = 0
    response_data['skuSizeId'] = skuSize.id
    response_data['skuSizeName'] = skuSize.name.encode('utf-8')
    response_data['skuSizePrice'] = str(skuSize.price)
    response['data'] = response_data
    return HttpResponse(json.dumps(response),content_type="application/json")


@csrf_exempt
def alterSkuSize(request):
    logger = logging.getLogger('Pack.app')
    logger.info(request.REQUEST)
    response = {}
    response['data'] = {}
    response['errorMsg'] = ""
    response_data = {}
    _shopId = request.session.get('shopId')
    _shopId = str(_shopId)
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

    _skuSizeId = request.REQUEST.get('skuSizeId')
    _skuSizeName = request.REQUEST.get('skuSizeName')
    _skuSizePrice = request.REQUEST.get('skuSizePrice')

    if _skuSizeId == None or _skuSizeId == '':
        response['code'] = -1
        response['errorMsg'] = 'skuSizeId为空'
        return HttpResponse(json.dumps(response),content_type="application/json")
    if _skuSizeName == None or _skuSizeName == '':
        response['code'] = -1
        response['errorMsg'] = 'skuSizeId为空'
        return HttpResponse(json.dumps(response),content_type="application/json")
    if _skuSizePrice == None or _skuSizePrice == '':
        response['code'] = -1
        response['errorMsg'] = 'skuSizeId为空'
        return HttpResponse(json.dumps(response),content_type="application/json")
    _skuSizeId = str(_skuSizeId)
    _skuSizeName = str(_skuSizeName)
    _skuSizePrice = str(_skuSizePrice)

    try:
        skuSize = SkuSize.objects.get(id = _skuSizeId)
    except ObjectDoesNotExist:
        response['code'] = -1
        response['errorMsg'] = '商品查询失败'
        return HttpResponse(json.dumps(response),content_type="application/json")
    skuSize.name = _skuSizeName
    skuSize.price = _skuSizePrice
    skuSize.save()
    response['code'] = 0
    response_data['skuSizeId'] = skuSize.id
    response_data['skuSizeName'] = skuSize.name.encode('utf-8')
    response_data['skuSizePrice'] = str(skuSize.price)
    response['data'] = response_data
    return HttpResponse(json.dumps(response),content_type="application/json")


@csrf_exempt
def delSkuSize(request):
    logger = logging.getLogger('Pack.app')
    logger.info(request.REQUEST)
    response = {}
    response['data'] = {}
    response['errorMsg'] = ""
    _shopId = request.session.get('shopId')
    _shopId = str(_shopId)
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

    _skuSizeId = request.REQUEST.get('skuSizeId')

    if _skuSizeId == None or _skuSizeId == '':
        response['code'] = -1
        response['errorMsg'] = 'skuSizeId为空'
        return HttpResponse(json.dumps(response),content_type="application/json")
    _skuSizeId = str(_skuSizeId)

    try:
        skuSize = SkuSize.objects.get(id = _skuSizeId)
    except ObjectDoesNotExist:
        response['code'] = -1
        response['errorMsg'] = '商品查询失败'
        return HttpResponse(json.dumps(response),content_type="application/json")
    skuSize.delete()
    response['code'] = 0
    return HttpResponse(json.dumps(response),content_type="application/json")


@csrf_exempt
def getSkusWithCategory(request):
    logger = logging.getLogger('Pack.app')
    logger.info(request.REQUEST)
    response = {}
    response['data'] = {}
    response['errorMsg'] = ""
    response_data = {}
    _shopId = request.session.get('shopId')
    _shopId = str(_shopId)
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
        shop = Shop.objects.select_related().get(id = _shopId)
    except ObjectDoesNotExist:
        response['code'] = 1
        response['errorMsg'] = '请先登录'
        return HttpResponse(json.dumps(response,ensure_ascii=False),content_type="application/json")
    if _lastLoginTime != shop.lastLoginTime:
        response['code'] = 1
        response['errorMsg'] = '上次登录失效，请重新登录'
        return HttpResponse(json.dumps(response),content_type="application/json")
    ####################END#################

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
        # _skuSizeList = sku.skuSize_set.all()
        # response_data_sku_size_list = []
        # for skuSize in _skuSizeList:
        #     response_data_sku_size = {}
        #     response_data_sku_size['skuSizeid'] = skuSize.id
        #     response_data_sku_size['skuSizeName'] = skuSize.sizeName.encode('utf-8')
        #     response_data_sku_size['skuPrice'] = str(skuSize.price)
        #     response_data_sku_size_list.append(response_data_sku_size)
        # response_data_sku['skuSizeList'] = response_data_sku_size_list
        # response_data_skus.append(response_data_sku)
    response_data['skus'] = response_data_skus
    response['code'] = 0
    response['data'] = response_data_skus
    return HttpResponse(json.dumps(response),content_type="application/json")
