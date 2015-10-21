#encoding:utf-8
from django.http import HttpResponse
import sys,json,re,logging
from pack.models import Shop,Table,WaiterOrder,Cook,WaiterServe,Order,Category,TableCategory
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q

reload(sys)
sys.setdefaultencoding('utf8')



@csrf_exempt
def getTableList(request):
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

    tableQuery = Table.objects.filter(shop = shop).filter(isValid = True).order_by('id')
    tables = tableQuery.reverse()

    response_data_tables = []
    for table in tables:
        _table = {}
        _table['tableId'] = table.id
        _table['tableNumber'] = table.number.encode('utf-8')
        _table['tablePeopleNumber'] = table.peopleNumber
        _table['tableStatus'] = table.status
        response_data_tables.append(_table)
    response_data['tables'] = response_data_tables
    response['code'] = 0
    response['data'] = response_data
    return HttpResponse(json.dumps(response),content_type="application/json")


@csrf_exempt
def tableInfo(request):
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

    #if method = 0 , add;  method = 2 , queryOne; method = 3, delete
    if _method == '0':
        _tableNumber = request.REQUEST.get('tableNumber')
        if _tableNumber == None or _tableNumber == '':
            response['code'] = -1
            response['errorMsg'] = '请输入餐桌号'
            return HttpResponse(json.dumps(response),content_type="application/json")
        _peopleNumber = request.REQUEST.get('tablePeopleNumber')
        if _peopleNumber == None or _peopleNumber == '':
            response['code'] = -1
            response['errorMsg'] = '请输入最大容纳人数'
            return HttpResponse(json.dumps(response),content_type="application/json")
        _tableCategoryList = request.REQUEST.get('tableCategoryList')
        if _tableCategoryList == None or _tableCategoryList == '':
            response['code'] = -1
            response['errorMsg'] = '请输入对应关系'
            return HttpResponse(json.dumps(response),content_type="application/json")
        __tableCategoryList = json.loads(_tableCategoryList)
        __categoryList = []
        for _tableCategory in __tableCategoryList:
            _categoryId = _tableCategory['categoryId']
            _waiterOrderId = _tableCategory['waiterOrderId']
            _cookId = _tableCategory['cookId']
            _waiterServeId = _tableCategory['waiterServeId']
            if _categoryId == None or _categoryId == '':
                response['code'] = -1
                response['errorMsg'] = '获取categoryId失败'
                return HttpResponse(json.dumps(response),content_type="application/json")
            if _waiterOrderId == None or _waiterOrderId == '':
                response['code'] = -1
                response['errorMsg'] = '获取categoryId失败'
                return HttpResponse(json.dumps(response),content_type="application/json")
            if _cookId == None or _cookId == '':
                response['code'] = -1
                response['errorMsg'] = '获取categoryId失败'
                return HttpResponse(json.dumps(response),content_type="application/json")
            if _waiterServeId == None or _waiterServeId == '':
                response['code'] = -1
                response['errorMsg'] = '获取categoryId失败'
                return HttpResponse(json.dumps(response),content_type="application/json")
            try:
                category = Category.objects.get(id = _categoryId)
            except ObjectDoesNotExist:
                response['code'] = -1
                response['errorMsg'] = '查找category失败'
                return HttpResponse(json.dumps(response),content_type="application/json")
            __categoryList.append(category)

        _tableNumber = str(_tableNumber)
        _peopleNumber = int(_peopleNumber)
        table = Table(shop = shop, number = _tableNumber, peopleNumber= _peopleNumber)
        index = 0
        for _tableCategory in __tableCategoryList:
            _waiterOrderId = _tableCategory['waiterOrderId']
            _cookId = _tableCategory['cookId']
            _waiterServeId = _tableCategory['waiterServeId']
            try:
                waiterOrder = WaiterOrder.objects.get(id = str(_waiterOrderId))
            except ObjectDoesNotExist:
                response['code'] = -1
                response['errorMsg'] = '查找厨师失败'
                return HttpResponse(json.dumps(response,ensure_ascii=False),content_type="application/json")
            try:
                cook = Cook.objects.get(id = str(_cookId))
            except ObjectDoesNotExist:
                response['code'] = -1
                response['errorMsg'] = '查找厨师失败'
                return HttpResponse(json.dumps(response,ensure_ascii=False),content_type="application/json")

            try:
                waiterServe = WaiterServe.objects.get(id = str(_waiterServeId))
            except ObjectDoesNotExist:
                response['code'] = -1
                response['errorMsg'] = '查找厨师失败'
                return HttpResponse(json.dumps(response,ensure_ascii=False),content_type="application/json")

            category = __categoryList[index]
            index = index + 1
            tableCategory = TableCategory(category = category, waiterOrder = waiterOrder, cook = cook,
                                          waiterServe = waiterServe)
            tableCategory.save()

        table.save()
        response['code'] = 0
        response_data = {}
        response_data['tableNumber'] = table.number
        response_data['tablePeopleNumber'] = table.peopleNumber
        response_data['tableStatus'] = table.status
        response_data['tableId'] = table.id
        response['data'] = response_data
        return HttpResponse(json.dumps(response),content_type="application/json")

    elif _method == '2':
        _tableId = request.REQUEST.get('tableId')
        if _tableId == None or _tableId == '':
            response['code'] = -1
            response['errorMsg'] = '请输入tableid'
            return HttpResponse(json.dumps(response),content_type="application/json")

        try:
            table = Table.objects.get(id = _tableId)
        except ObjectDoesNotExist:
            response['code'] = -1
            response['errorMsg'] = 'table查询失败'
            return HttpResponse(json.dumps(response),content_type="application/json")

        response['code'] = 0
        response_data = {}
        response_data['tableNumber'] = table.number
        response_data['tablePeopleNumber'] = table.peopleNumber
        response_data['tableStatus'] = table.status
        response_data['tableId'] = table.id
        response['data'] = response_data
        return HttpResponse(json.dumps(response),content_type="application/json")

    elif _method == '3':
        _tableId = request.REQUEST.get('tableId')
        if _tableId == None or _tableId == '':
            response['code'] = -1
            response['errorMsg'] = '请输入tableid'
            return HttpResponse(json.dumps(response),content_type="application/json")
        try:
            table = Table.objects.get(id = _tableId)
        except ObjectDoesNotExist:
            response['code'] = -1
            response['errorMsg'] = 'table查询失败'
            return HttpResponse(json.dumps(response),content_type="application/json")

        table.isValid = False
        table.save()
        response['code'] = 0
        response['data'] = {}
        return HttpResponse(json.dumps(response),content_type="application/json")


@csrf_exempt
def getCategoriesWithTable(request):
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

    _tableId = request.session.get('tableId')
    if _tableId == None or _tableId == '':
        response['code'] = -1
        response['errorMsg'] = '获取tableId失败'
        return HttpResponse(json.dumps(response),content_type="application/json")

    categories = Category.objects.filter(shop = shop).order_by('-id')
    response_categories = []
    for category in categories:
        response_category={}
        tableCategoryQuery = TableCategory.objects.filter(category = category).filter(table__id = _tableId)
        if tableCategoryQuery.exists():
            response_category['isTableCategoryExists'] = '1'
        else:
            response_category['isTableCategoryExists'] = '0'
        response_category['categoryName'] = category.categoryName
        response_category['categoryId'] = category.id
        response_categories.append(response_category)
    response['code'] = 0
    response['data'] = response_categories
    return HttpResponse(json.dumps(response,ensure_ascii=False),content_type="application/json")


@csrf_exempt
def getTableCategoryDetail(request):
    response = {}
    response['data'] = {}
    response_data = {}
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

    _tableId = request.session.get('tableId')
    if _tableId == None or _tableId == '':
        response['code'] = -1
        response['errorMsg'] = '获取tableId失败'
        return HttpResponse(json.dumps(response),content_type="application/json")
    _categoryId = request.session.get('categoryId')
    if _categoryId == None or _categoryId == '':
        response['code'] = -1
        response['errorMsg'] = '获取categoryId失败'
        return HttpResponse(json.dumps(response),content_type="application/json")
    _tableId = str(_tableId)
    _categoryId = str(_categoryId)

    tableCategoryQuery = TableCategory.objects.filter(category__id = _categoryId).filter(table__id = _tableId)
    if not tableCategoryQuery.exists():
        response['code'] = -1
        response['errorMsg'] = '查询tableCategory失败'
        return HttpResponse(json.dumps(response),content_type="application/json")
    waiterOrder = tableCategoryQuery[0].waiterOrder
    cook = tableCategoryQuery[0].cook
    waiterServe = tableCategoryQuery[0].waiterServe
    response_data['tableCategoryId'] = str(tableCategoryQuery[0].id)
    response_data_waiter_order = {}
    response_data_waiter_order['waiterOrderId'] = waiterOrder.id
    response_data_waiter_order['waiterOrderName'] = waiterOrder.name
    response_data_waiter_order['waiterOrderTelephone'] = waiterOrder.telephone
    response_data['waiterOrderInfo'] = response_data_waiter_order
    response_data_cook = {}
    response_data_cook['cookId'] = cook.id
    response_data_cook['cookName'] = cook.name
    response_data_cook['cookTelephone'] = cook.telephone
    response_data['cookInfo'] = response_data_cook
    response_data_waiter_serve = {}
    response_data_waiter_serve['waiterServeId'] = waiterServe.id
    response_data_waiter_serve['waiterServeName'] = waiterServe.name
    response_data_waiter_serve['waiterServeTelephone'] = waiterServe.telephone
    response_data['waiterServeInfo'] = response_data_waiter_serve
    response['data'] = response_data
    return HttpResponse(json.dumps(response,ensure_ascii=False),content_type="application/json")

@csrf_exempt
def addTableCategory(request):
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
    _tableId = request.REQUEST.get('tableId')
    _categoryId = request.REQUEST.get('categoryId')
    _waiterOrderId = request.REQUEST.get('waiterOrderId')
    _cookId = request.REQUEST.get('cookId')
    _waiterServeId = request.REQUEST.get('waiterServeId')

    if _tableId == None or _tableId == '':
        response['code'] = -1
        response['errorMsg'] = '请输入tableId'
        return HttpResponse(json.dumps(response),content_type="application/json")
    if _categoryId == None or _categoryId == '':
        response['code'] = -1
        response['errorMsg'] = '请输入tableCategoryId'
        return HttpResponse(json.dumps(response),content_type="application/json")
    if _waiterOrderId == None or _waiterOrderId == '':
        response['code'] = -1
        response['errorMsg'] = '请输入waiterOrderId'
        return HttpResponse(json.dumps(response),content_type="application/json")
    if _cookId == None or _cookId == '':
        response['code'] = -1
        response['errorMsg'] = '请输入cookId'
        return HttpResponse(json.dumps(response),content_type="application/json")
    if _waiterServeId == None or _waiterServeId == '':
        response['code'] = -1
        response['errorMsg'] = '请输入waiterServeId'
        return HttpResponse(json.dumps(response),content_type="application/json")

    _tableId = str(_tableId)
    _waiterOrderId = str(_waiterOrderId)
    _cookId = str(_cookId)
    _waiterServeId = str(_waiterServeId)
    tableCategoryQuery = TableCategory.objects.filter(table__id = _tableId).filter(category__id = _categoryId).filter(waiterOrder__id = _waiterOrderId).filter(cook__id = _cookId).filter(waiterServe__id = _waiterServeId)
    if tableCategoryQuery.exists():
        response['code'] = -1
        response['errorMsg'] = '已经绑定过'
        return HttpResponse(json.dumps(response),content_type="application/json")
    else:
        try:
            table = Table.objects.get(id = _tableId)
        except ObjectDoesNotExist:
            response['code'] = -1
            response['errorMsg'] = '查找厨师失败'
            return HttpResponse(json.dumps(response,ensure_ascii=False),content_type="application/json")
        try:
            category = Category.objects.get(id = _categoryId)
        except ObjectDoesNotExist:
            response['code'] = -1
            response['errorMsg'] = '查找厨师失败'
            return HttpResponse(json.dumps(response,ensure_ascii=False),content_type="application/json")

        try:
            waiterOrder = WaiterOrder.objects.get(id = _waiterOrderId)
        except ObjectDoesNotExist:
            response['code'] = -1
            response['errorMsg'] = '查找厨师失败'
            return HttpResponse(json.dumps(response,ensure_ascii=False),content_type="application/json")
        try:
            cook = Cook.objects.get(id = _cookId)
        except ObjectDoesNotExist:
            response['code'] = -1
            response['errorMsg'] = '查找厨师失败'
            return HttpResponse(json.dumps(response,ensure_ascii=False),content_type="application/json")

        try:
            waiterServe = WaiterServe.objects.get(id = _waiterServeId)
        except ObjectDoesNotExist:
            response['code'] = -1
            response['errorMsg'] = '查找厨师失败'
            return HttpResponse(json.dumps(response,ensure_ascii=False),content_type="application/json")

        tableCategory = TableCategory(table = table,mcategory = category, waiterOrder = waiterOrder, cook = cook,
                                          waiterServe = waiterServe)
        tableCategory.save()
        response_data_waiter_order = {}
        response_data_waiter_order['waiterOrderId'] = waiterOrder.id
        response_data_waiter_order['waiterOrderName'] = waiterOrder.name
        response_data_waiter_order['waiterOrderTelephone'] = waiterOrder.telephone
        response['data'] = response_data_waiter_order
        return HttpResponse(json.dumps(response),content_type="application/json")



@csrf_exempt
def alterTableNumber(request):
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
    _tableId = request.REQUEST.get('tableId')
    _tableNumber = request.REQUEST.get('tableNumber')

    if _tableId == None or _tableId == '':
        response['code'] = -1
        response['errorMsg'] = '请输入tableid'
        return HttpResponse(json.dumps(response),content_type="application/json")
    if _tableNumber == None or _tableNumber == '':
        response['code'] = -1
        response['errorMsg'] = '请输入餐桌号'
        return HttpResponse(json.dumps(response),content_type="application/json")

    _tableNumber = str(_tableNumber)

    try:
        table = Table.objects.get(id = _tableId)
    except ObjectDoesNotExist:
        response['code'] = -1
        response['errorMsg'] = 'table查询失败'
        return HttpResponse(json.dumps(response),content_type="application/json")

    table.number = _tableNumber
    table.save()

    response['code'] = 0
    response_data = {}
    response_data['tableNumber'] = table.number
    response_data['tablePeopleNumber'] = table.peopleNumber
    response_data['tableStatus'] = table.status
    response_data['tableId'] = table.id
    response['data'] = response_data
    return HttpResponse(json.dumps(response),content_type="application/json")


@csrf_exempt
def alterTablePeopleNumber(request):
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
    _tableId = request.REQUEST.get('tableId')
    _peopleNumber = request.REQUEST.get('tablePeopleNumber')

    if _tableId == None or _tableId == '':
        response['code'] = -1
        response['errorMsg'] = '请输入tableId'
        return HttpResponse(json.dumps(response),content_type="application/json")
    if _peopleNumber == None or _peopleNumber == '':
        response['code'] = -1
        response['errorMsg'] = '请输入容纳人数'
        return HttpResponse(json.dumps(response),content_type="application/json")

    _peopleNumber = str(_peopleNumber)

    try:
        table = Table.objects.get(id = _tableId)
    except ObjectDoesNotExist:
        response['code'] = -1
        response['errorMsg'] = 'table查询失败'
        return HttpResponse(json.dumps(response),content_type="application/json")

    table.peopleNumber = _peopleNumber
    table.save()

    response['code'] = 0
    response_data = {}
    response_data['tableNumber'] = table.number
    response_data['tablePeopleNumber'] = table.peopleNumber
    response_data['tableStatus'] = table.status
    response_data['tableId'] = table.id
    response['data'] = response_data
    return HttpResponse(json.dumps(response),content_type="application/json")


@csrf_exempt
def alterTableCategoryWaiterOrder(request):
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
    _tableCategoryId = request.REQUEST.get('tableCategoryId')
    _waiterOrderId = request.REQUEST.get('waiterOrderId')

    if _tableCategoryId == None or _tableCategoryId == '':
        response['code'] = -1
        response['errorMsg'] = '请输入tableCategoryId'
        return HttpResponse(json.dumps(response),content_type="application/json")
    if _waiterOrderId == None or _waiterOrderId == '':
        response['code'] = -1
        response['errorMsg'] = '请输入容纳人数'
        return HttpResponse(json.dumps(response),content_type="application/json")

    _waiterOrderId = str(_waiterOrderId)

    try:
        tableCategory = TableCategory.objects.get(id = _tableCategoryId)
    except IndexError:
        response['code'] = -1
        response['errorMsg'] = 'tableCategory查询失败'
        return HttpResponse(json.dumps(response),content_type="application/json")

    try:
        waiterOrder = WaiterOrder.objects.filter(id = _waiterOrderId)
    except ObjectDoesNotExist:
        response['code'] = -1
        response['errorMsg'] = 'waiterOrderId查询失败'
        return HttpResponse(json.dumps(response),content_type="application/json")

    tableCategory.waiterOrder = waiterOrder
    tableCategory.save()
    response_data_waiter_order = {}
    response_data_waiter_order['waiterOrderId'] = waiterOrder.id
    response_data_waiter_order['waiterOrderName'] = waiterOrder.name
    response_data_waiter_order['waiterOrderTelephone'] = waiterOrder.telephone
    response['data'] = response_data_waiter_order
    return HttpResponse(json.dumps(response),content_type="application/json")


@csrf_exempt
def alterTableCategoryCook(request):
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
    _tableCategoryId = request.REQUEST.get('tableCategoryId')
    _cookId = request.REQUEST.get('cookId')

    if _tableCategoryId == None or _tableCategoryId == '':
        response['code'] = -1
        response['errorMsg'] = '获取categoryId失败'
        return HttpResponse(json.dumps(response),content_type="application/json")
    if _cookId == None or _cookId == '':
        response['code'] = -1
        response['errorMsg'] = '请输入容纳人数'
        return HttpResponse(json.dumps(response),content_type="application/json")

    _cookId = str(_cookId)

    try:
        tableCategory = TableCategory.objects.get(id = _tableCategoryId)
    except IndexError:
        response['code'] = -1
        response['errorMsg'] = 'tableCategory查询失败'
        return HttpResponse(json.dumps(response),content_type="application/json")

    try:
        cook = Cook.objects.filter(id = _cookId)
    except ObjectDoesNotExist:
        response['code'] = -1
        response['errorMsg'] = 'waiterOrderId查询失败'
        return HttpResponse(json.dumps(response),content_type="application/json")

    tableCategory.cook = cook
    tableCategory.save()
    response_data_waiter_order = {}
    response_data_waiter_order['cookId'] = cook.id
    response_data_waiter_order['cookName'] = cook.name
    response_data_waiter_order['cookTelephone'] = cook.telephone
    response['data'] = response_data_waiter_order
    return HttpResponse(json.dumps(response),content_type="application/json")


@csrf_exempt
def alterTableCategoryWaiterServe(request):
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
    _tableCategoryId = request.REQUEST.get('tableCategoryId')
    _waiterServeId = request.REQUEST.get('waiterServeId')

    if _tableCategoryId == None or _tableCategoryId == '':
        response['code'] = -1
        response['errorMsg'] = '请输入tableCategoryId'
        return HttpResponse(json.dumps(response),content_type="application/json")
    if _waiterServeId == None or _waiterServeId == '':
        response['code'] = -1
        response['errorMsg'] = '请输入容纳人数'
        return HttpResponse(json.dumps(response),content_type="application/json")

    _waiterServeId = str(_waiterServeId)

    try:
        tableCategory = TableCategory.objects.get(id = _tableCategoryId)
    except IndexError:
        response['code'] = -1
        response['errorMsg'] = 'tableCategory查询失败'
        return HttpResponse(json.dumps(response),content_type="application/json")

    try:
        waiterServe = WaiterServe.objects.filter(id = _waiterServeId)
    except ObjectDoesNotExist:
        response['code'] = -1
        response['errorMsg'] = 'waiterServeId查询失败'
        return HttpResponse(json.dumps(response),content_type="application/json")

    tableCategory.waiterServe = waiterServe
    tableCategory.save()
    response_data_waiter_order = {}
    response_data_waiter_order['waiterServeId'] = waiterServe.id
    response_data_waiter_order['waiterServeName'] = waiterServe.name
    response_data_waiter_order['waiterServeTelephone'] = waiterServe.telephone
    response['data'] = response_data_waiter_order
    return HttpResponse(json.dumps(response),content_type="application/json")


@csrf_exempt
def setTableStatus(request):
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
    _tableId = request.REQUEST.get('tableId')
    if _method == None or _method == '':
        response['code'] = -1
        response['errorMsg'] = '获取method失败'
        return HttpResponse(json.dumps(response,ensure_ascii=False),content_type="application/json")
    if _tableId == None or _tableId == '':
        response['code'] = -1
        response['errorMsg'] = '请输入tableId'
        return HttpResponse(json.dumps(response),content_type="application/json")
    _method = str(_method)

    if  _method == '0':
        try:
            table = Table.objects.get(id = _tableId)
        except ObjectDoesNotExist:
            response['code'] = -1
            response['errorMsg'] = 'table查询失败'
            return HttpResponse(json.dumps(response),content_type="application/json")

        if table.status == '1' or table.status == '2':
            table.status = '0'
            table.save()
            response['code'] = 0
            response_data = {}
            response_data['tableNumber'] = table.number
            response_data['tablePeopleNumber'] = table.peopleNumber
            response_data['tableStatus'] = table.status
            response_data['tableId'] = table.id
            response['data'] = response_data
            return HttpResponse(json.dumps(response),content_type="application/json")

        elif table.status == '3':
            orderQuery = Order.objects.filter(shop = shop).filter(tableId = _tableId).filter(Q(status = '0')|Q(
                status = '1')|Q(status = '2'))
            print orderQuery
            if len(orderQuery) > 0:
                response['code'] = -1
                response['errorMsg'] = '有订单未完成，暂无法设置为空闲'
                return HttpResponse(json.dumps(response),content_type="application/json")
            table.status = '0'
            table.save()
            response['code'] = 0
            response_data = {}
            response_data['tableNumber'] = table.number
            response_data['tablePeopleNumber'] = table.peopleNumber
            response_data['tableStatus'] = table.status
            response_data['tableId'] = table.id
            response['data'] = response_data
            return HttpResponse(json.dumps(response),content_type="application/json")

        elif table.status == '0':
            response['code'] = 0
            response_data = {}
            response_data['tableNumber'] = table.number
            response_data['tablePeopleNumber'] = table.peopleNumber
            response_data['tableStatus'] = table.status
            response_data['tableId'] = table.id
            response['data'] = response_data
            return HttpResponse(json.dumps(response),content_type="application/json")

    elif _method == '1':
        try:
            table = Table.objects.get(id = _tableId)
        except ObjectDoesNotExist:
            response['code'] = -1
            response['errorMsg'] = 'table查询失败'
            return HttpResponse(json.dumps(response),content_type="application/json")
        response['code'] = -1
        response['errorMsg'] = '您无权进行此操作'
        return HttpResponse(json.dumps(response),content_type="application/json")

    elif  _method == '2':
        try:
            table = Table.objects.get(id = _tableId)
        except ObjectDoesNotExist:
            response['code'] = -1
            response['errorMsg'] = 'table查询失败'
            return HttpResponse(json.dumps(response),content_type="application/json")

        if table.status == '0':
            table.status = '2'
            table.save()
            response['code'] = 0
            response_data = {}
            response_data['tableNumber'] = table.number
            response_data['tablePeopleNumber'] = table.peopleNumber
            response_data['tableStatus'] = table.status
            response_data['tableId'] = table.id
            response['data'] = response_data
            return HttpResponse(json.dumps(response),content_type="application/json")

        elif table.status == '1' or table.status == '3':
            response['code'] = -1
            response['errorMsg'] = '您无权进行此操作'
            return HttpResponse(json.dumps(response),content_type="application/json")

        elif table.status == '2':
            response['code'] = 0
            response_data = {}
            response_data['tableNumber'] = table.number
            response_data['tablePeopleNumber'] = table.peopleNumber
            response_data['tableStatus'] = table.status
            response_data['tableId'] = table.id
            response['data'] = response_data
            return HttpResponse(json.dumps(response),content_type="application/json")

    response['code'] = -1
    response['errorMsg'] = 'method错误'
    return HttpResponse(json.dumps(response),content_type="application/json")


