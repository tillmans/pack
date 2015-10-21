__author__ = 'mike'
#encoding:utf-8
from django.http import HttpResponse
import sys,json,datetime
from pack.models import Order,WaiterOrder,OrderSku,Table,OrderRecord,User,TableCategory,TableLock
from django.views.decorators.csrf import csrf_exempt
import logging
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist
from pack.pack_push_2_user import pushAPN,pushMessageToSingle
import pytz

reload(sys)
sys.setdefaultencoding('utf8')


@csrf_exempt
def submitOrder(request):
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
        waiterOrder = WaiterOrder.objects.select_related().get(id = _waiterOrderId)
    except ObjectDoesNotExist:
        response['code'] = 1
        response['errorMsg'] = '请先登录'
        return HttpResponse(json.dumps(response,ensure_ascii=False),content_type="application/json")
    if _lastLoginTime != waiterOrder.lastLoginTime:
        response['code'] = 1
        response['errorMsg'] = '上次登录失效，请重新登录'
        return HttpResponse(json.dumps(response),content_type="application/json")
    ####################END#################

    _tableId = request.REQUEST.get('tableId')
    _priceTotal = request.REQUEST.get('priceTotal')
    _categoryList = request.REQUEST.get('categoryList')
    if _tableId == None or _tableId == '':
        response['code'] = -1
        response['errorMsg'] = '获取tableId失败'
        return HttpResponse(json.dumps(response,ensure_ascii=False),content_type="application/json")

    if _priceTotal == None or _priceTotal == '':
        response['code'] = -1
        response['errorMsg'] = '获取总计价格失败'
        return HttpResponse(json.dumps(response,ensure_ascii=False),content_type="application/json")
    if _categoryList == None or _categoryList == '':
        response['code'] = -1
        response['errorMsg'] = '请输入对应关系'
        return HttpResponse(json.dumps(response),content_type="application/json")
    __categoryList = json.loads(_categoryList)

    if _tableId == None or _tableId == '':
        response['code'] = -1
        response['errorMsg'] = '获取tableId失败'
        return HttpResponse(json.dumps(response,ensure_ascii=False),content_type="application/json")

    if _priceTotal == None or _priceTotal == '':
        response['code'] = -1
        response['errorMsg'] = '获取总计价格失败'
        return HttpResponse(json.dumps(response,ensure_ascii=False),content_type="application/json")

    try:
        table = Table.objects.get(id = _tableId)
    except ObjectDoesNotExist:
        response['code'] = -1
        response['errorMsg'] = '获取餐桌信息失败'
        return HttpResponse(json.dumps(response,ensure_ascii=False),content_type="application/json")
    if table.status == '0':
        response['code'] = -1
        response['errorMsg'] = '请先锁定餐桌，然后下单'
        return HttpResponse(json.dumps(response,ensure_ascii=False),content_type="application/json")
    elif table.status == '1':
        try:
            tableLock = Table.objects.select_related().get(table = table).last()
        except IndexError:
            response['code'] = -1
            response['errorMsg'] = '查找锁定信息失败'
            return HttpResponse(json.dumps(response,ensure_ascii=False),content_type="application/json")
        order = Order(shop = waiterOrder.shop, userId = str(tableLock.user__id), priceTotal = str(_priceTotal),
                      tableId = str(table.id), tableNumber = str(table.tableNumber),status = '0',date =
                    datetime.datetime.now())
        order.save()
        table.status = '3'
        table.save()
        submitRecord = u'点菜成功，订单号为：'.encode('utf-8')
        submitRecord = submitRecord + str(order.id)
        submitRecord = submitRecord + u'，桌号为：'.encode('utf-8')
        submitRecord = submitRecord + str(table.tableNumber)
        record = OrderRecord(record = submitRecord,order=order,date = datetime.datetime.now())
        record.save()
        _orderSKUList = []
        for category in __categoryList:
            categoryId = category['categoryId']
            skuList = category['skuList']
            try:
                tableCategory = TableCategory.objects.select_realted().filter(table__id = str(table.id)).filter(
                    category__id =  str(categoryId))[0]
            except IndexError:
                response['code'] = -1
                response['errorMsg'] = '获取tableCategory失败'
                return HttpResponse(json.dumps(response,ensure_ascii=False),content_type="application/json")
            for sku in skuList:
                _id = sku['skuId']
                _name = sku['skuName']
                _quantity = sku['skuQuantity']
                _sizeName = sku['skuSizeName']
                _price = sku['skuPrice']
                _orderSKUList.append(OrderSku(order = order,tableId = str(table.id) ,skuId = _id,  skuName = _name, skuQuantity =
                    int(_quantity),skuSizeName =_sizeName, skuPrice = _price,status = '0',waiterOrderId = str(
                    tableCategory.waiterOrder.id),cookId = str(tableCategory.cook.id),waiterServeId = str(
                    tableCategory.waiterServe.id)))
            cook = tableCategory.cook
            _deviceInfo = cook.deviceInfo
            OrderSku.objects.bulk_create(_orderSKUList)
            if(len(_deviceInfo and "iOS") == 3):
                pass
#               pushRst = pushAPN(saler.deviceToken,'0',str(orderQuery[0].id))
            elif(len(_deviceInfo and 'Android') == 7):
                pass
#               pushRst = pushMessageToSingle(saler.clientID,'0',str(orderQuery[0].id))
            response['code'] = 0
            return HttpResponse(json.dumps(response,ensure_ascii=False),content_type="application/json")
    elif table.status == '2':
        order = Order(shop = waiterOrder.shop, priceTotal = str(_priceTotal),tableId = str(table.id),
                      tableNumber = str(table.tableNumber),status = '0',date =datetime.datetime.now())
        order.save()
        table.status = '3'
        table.save()
        submitRecord = u'点菜成功，订单号为：'.encode('utf-8')
        submitRecord = submitRecord + str(order.id)
        submitRecord = submitRecord + u'，桌号为：'.encode('utf-8')
        submitRecord = submitRecord + str(table.tableNumber)
        record = OrderRecord(record = submitRecord,order=order,date = datetime.datetime.now())
        record.save()
        _orderSKUList = []
        for category in __categoryList:
            categoryId = category['categoryId']
            try:
                tableCategory = TableCategory.objects.select_realted().filter(table__id = str(table.id)).filter(
                    category__id =  str(categoryId))[0]
            except IndexError:
                response['code'] = -1
                response['errorMsg'] = '获取tableCategory失败'
                return HttpResponse(json.dumps(response,ensure_ascii=False),content_type="application/json")
            skuList = category['skuList']
            for sku in skuList:
                _id = sku['skuId']
                _name = sku['skuName']
                _quantity = sku['skuQuantity']
                _sizeName = sku['skuSizeName']
                _price = sku['skuPrice']
                _orderSKUList.append(OrderSku(order = order,tableId = str(table.id) ,skuId = _id,  skuName = _name, skuQuantity =
                    int(_quantity),skuSizeName =_sizeName, skuPrice = _price,status = '0',waiterOrderId = str(
                    tableCategory.waiterOrder.id),cookId = str(tableCategory.cook.id),waiterServeId = str(
                    tableCategory.waiterServe.id)))
            cook = tableCategory.cook
            _deviceInfo = cook.deviceInfo
            OrderSku.objects.bulk_create(_orderSKUList)
            if(len(_deviceInfo and "iOS") == 3):
                pass
#               pushRst = pushAPN(saler.deviceToken,'0',str(orderQuery[0].id))
            elif(len(_deviceInfo and 'Android') == 7):
                pass
#               pushRst = pushMessageToSingle(saler.clientID,'0',str(orderQuery[0].id))
            response['code'] = 0
            return HttpResponse(json.dumps(response,ensure_ascii=False),content_type="application/json")

    elif table.status == '3':
        response['code'] = -1
        response['errorMsg'] = '该餐桌正在忙碌，无法下单'
        return HttpResponse(json.dumps(response,ensure_ascii=False),content_type="application/json")

@csrf_exempt
def addSkusWithOrder(request):
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
        waiterOrder = WaiterOrder.objects.select_related().get(id = _waiterOrderId)
    except ObjectDoesNotExist:
        response['code'] = 1
        response['errorMsg'] = '请先登录'
        return HttpResponse(json.dumps(response,ensure_ascii=False),content_type="application/json")
    if _lastLoginTime != waiterOrder.lastLoginTime:
        response['code'] = 1
        response['errorMsg'] = '上次登录失效，请重新登录'
        return HttpResponse(json.dumps(response),content_type="application/json")
    ####################END#################

    _orderId = request.REQUEST.get('orderId')
    _priceTotal = request.REQUEST.get('priceTotal')
    _categoryList = request.REQUEST.get('categoryList')
    if _priceTotal == None or _priceTotal == '':
        response['code'] = -1
        response['errorMsg'] = '获取总计价格失败'
        return HttpResponse(json.dumps(response,ensure_ascii=False),content_type="application/json")
    if _orderId == None or _orderId == '':
        response['code'] = -1
        response['errorMsg'] = '获取orderId失败'
        return HttpResponse(json.dumps(response,ensure_ascii=False),content_type="application/json")
    if _categoryList == None or _categoryList == '':
        response['code'] = -1
        response['errorMsg'] = '请输入对应关系'
        return HttpResponse(json.dumps(response),content_type="application/json")
    __categoryList = json.loads(_categoryList)


    try:
        order = Order.objects.get(id = _orderId)
    except ObjectDoesNotExist:
        response['code'] = -1
        response['errorMsg'] = '获取餐桌信息失败'
        return HttpResponse(json.dumps(response,ensure_ascii=False),content_type="application/json")

    if order.status == '0':
        priceTotal = float(order.pricetotal) + float(_priceTotal)
        order.pricetotal = priceTotal
        order.save()
        submitRecord = u'加菜成功'.encode('utf-8')
        record = OrderRecord(record = submitRecord,order=order,date = datetime.datetime.now())
        record.save()

        _orderSKUList = []
        for category in __categoryList:
            categoryId = category['categoryId']
            try:
                tableCategory = TableCategory.objects.select_realted().filter(table__id = str(table.id)).filter(
                    category__id =  str(categoryId))[0]
            except IndexError:
                response['code'] = -1
                response['errorMsg'] = '获取tableCategory失败'
                return HttpResponse(json.dumps(response,ensure_ascii=False),content_type="application/json")
            skuList = category['skuList']
            for sku in skuList:
                _id = sku['skuId']
                _name = sku['skuName']
                _quantity = sku['skuQuantity']
                _sizeName = sku['skuSizeName']
                _price = sku['skuPrice']
                _orderSKUList.append(OrderSku(order = order,tableId = str(order.tableId) ,skuId = _id,  skuName = _name,
                    skuQuantity =int(_quantity),skuSizeName =_sizeName, skuPrice = _price,status = '0',waiterOrderId = str(
                    tableCategory.waiterOrder.id),cookId = str(tableCategory.cook.id),waiterServeId = str(
                    tableCategory.waiterServe.id)))
            cook = tableCategory.cook
            _deviceInfo = cook.deviceInfo
            OrderSku.objects.bulk_create(_orderSKUList)
            if(len(_deviceInfo and "iOS") == 3):
                pass
#               pushRst = pushAPN(saler.deviceToken,'0',str(orderQuery[0].id))
            elif(len(_deviceInfo and 'Android') == 7):
                pass
#               pushRst = pushMessageToSingle(saler.clientID,'0',str(orderQuery[0].id))
            response['code'] = 0
            return HttpResponse(json.dumps(response,ensure_ascii=False),content_type="application/json")

    else:
        response['code'] = -1
        response['errorMsg'] = ''
        return HttpResponse(json.dumps(response,ensure_ascii=False),content_type="application/json")

@csrf_exempt
def finishOrder(request):
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
        waiterOrder = WaiterOrder.objects.select_related().get(id = _waiterOrderId)
    except ObjectDoesNotExist:
        response['code'] = 1
        response['errorMsg'] = '请先登录'
        return HttpResponse(json.dumps(response,ensure_ascii=False),content_type="application/json")
    if _lastLoginTime != waiterOrder.lastLoginTime:
        response['code'] = 1
        response['errorMsg'] = '上次登录失效，请重新登录'
        return HttpResponse(json.dumps(response),content_type="application/json")
    ####################END#################

    _orderId = request.REQUEST.get('orderId')
    if _orderId == None or _orderId == '':
        response['code'] = -1
        response['errorMsg'] = '获取orderId失败'
        return HttpResponse(json.dumps(response,ensure_ascii=False),content_type="application/json")

    try:
        order = Order.objects.get(id = _orderId)
    except ObjectDoesNotExist:
        response['code'] = -1
        response['errorMsg'] = '获取餐桌信息失败'
        return HttpResponse(json.dumps(response,ensure_ascii=False),content_type="application/json")

    if order.status == '0':
        if order.userId == '':
            order.status = '4'
            order.save()
            submitRecord = u'就餐完毕'.encode('utf-8')
            record = OrderRecord(record = submitRecord,order=order,date = datetime.datetime.now())
            record.save()

            try:
                table = Table.objects.get(id = str(order.tableId))
            except ObjectDoesNotExist:
                response['code'] = -1
                response['errorMsg'] = '获取餐桌信息失败'
                return HttpResponse(json.dumps(response,ensure_ascii=False),content_type="application/json")
            table.status = '0'
            table.save()
            response['code'] = 0
            return HttpResponse(json.dumps(response,ensure_ascii=False),content_type="application/json")
        else:
            order.status = '2'
            order.save()
            submitRecord = u'就餐完毕'.encode('utf-8')
            record = OrderRecord(record = submitRecord,order=order,date = datetime.datetime.now())
            record.save()
            tableLockQuery = TableLock.objects.select_related().filter(user__id = order.userId).filter(table__id
                        = str(order.tableId)).filter(isValid = True)
            if not tableLockQuery.exists():
                logger.info('不存在该tableLockQuery')
                try:
                    table = Table.objects.get(id = str(order.tableId))
                except ObjectDoesNotExist:
                    response['code'] = -1
                    response['errorMsg'] = '获取餐桌信息失败'
                    return HttpResponse(json.dumps(response,ensure_ascii=False),content_type="application/json")
                table.status = '0'
                table.save()
                response['code'] = 0
                return HttpResponse(json.dumps(response,ensure_ascii=False),content_type="application/json")
            else:
                user = tableLockQuery[0].user
                tableLockQuery.update(isValid = False)
                _deviceInfo = user.deviceInfo
                if(len(_deviceInfo and "iOS") == 3):
                    pass
    #               pushRst = pushAPN(saler.deviceToken,'0',str(orderQuery[0].id))
                elif(len(_deviceInfo and 'Android') == 7):
                    pass
    #               pushRst = pushMessageToSingle(saler.clientID,'0',str(orderQuery[0].id))

                try:
                    table = Table.objects.get(id = str(order.tableId))
                except ObjectDoesNotExist:
                    response['code'] = -1
                    response['errorMsg'] = '获取餐桌信息失败'
                    return HttpResponse(json.dumps(response,ensure_ascii=False),content_type="application/json")
                table = tableLockQuery[0].table
                table.status = '0'
                table.save()
                response['code'] = 0
                return HttpResponse(json.dumps(response,ensure_ascii=False),content_type="application/json")


@csrf_exempt
def getShopOrderDetailWithTable(request):
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

