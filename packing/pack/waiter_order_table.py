#encoding:utf-8
from django.http import HttpResponse
import sys,json
from pack.models import Table,TableLock,WaiterOrder,Order,TableCategory
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
import pytz

reload(sys)
sys.setdefaultencoding('utf8')

@csrf_exempt
def waiterOrderGetTableList(request):
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
    if waiterOrder.saler == None:
        response['code'] = 2
        response['errorMsg'] = '请联系管理员关联您的账户'
        return HttpResponse(json.dumps(response),content_type="application/json")

    tableCategoryQuery = TableCategory.objects.select_related().filter(waiterOrderId = str(_waiterOrderId)).filter(
        table__isValid = True).order_by('id')
    tableCategoryList = tableCategoryQuery.reverse()

    response_data_tables = []
    for tableCategory in tableCategoryList:
        _table = {}
        _table['tableId'] = tableCategory.table.id
        _table['tableNumber'] = tableCategory.table.number.encode('utf-8')
        _table['tablePeopleNumber'] = tableCategory.table.peopleNumber
        _table['tableStatus'] = tableCategory.table.status
        response_data_tables.append(_table)
    response_data['tables'] = response_data_tables
    response['code'] = 0
    response['data'] = response_data
    return HttpResponse(json.dumps(response),content_type="application/json")

@csrf_exempt
def waiterOrderGetTableDetail(request):
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
    if waiterOrder.saler == None:
        response['code'] = 2
        response['errorMsg'] = '请联系管理员关联您的账户'
        return HttpResponse(json.dumps(response),content_type="application/json")

    _tableId = request.REQUEST.get('tableId')
    if _tableId == None or _tableId == '':
        response['code'] = -1
        response['errorMsg'] = '请输入tableid'
        return HttpResponse(json.dumps(response),content_type="application/json")
    _tableId = str(_tableId)
    try:
        table = Table.objects.get(id = _tableId)
    except ObjectDoesNotExist:
        response['code'] = -1
        response['errorMsg'] = '查找table失败'
        return HttpResponse(json.dumps(response),content_type="application/json")
    _table = {}
    _table['tableId'] = table.id
    _table['tableNumber'] = table.number.encode('utf-8')
    _table['tablePeopleNumber'] = table.peopleNumber
    _table['tableStatus'] = table.status
    response_data['tableInfo'] = _table
    if table.status == '1':
        try:
            tableLock = TableLock.objects.filter(table = table).last()
        except IndexError:
            tableLock = None
            response_data['userInfo'] = ''
        _table_lock_userInfo = {}
        _table_lock_userInfo['userId'] = str(tableLock.user.id)
        _table_lock_userInfo['userTelephone'] = str(tableLock.user.telephone)
        _table_lock_userInfo['userName'] = str(tableLock.user.name)
        shanghai_tz = pytz.timezone('Asia/Shanghai')
        date = tableLock.date.astimezone(shanghai_tz)
        _table_lock_userInfo['dateTime'] = date.strftime('%Y/%m/%d %H:%M:%S')
        response_data['userInfo'] = _table_lock_userInfo
    response['code'] = 0
    response['data'] = response_data
    return HttpResponse(json.dumps(response),content_type="application/json")


@csrf_exempt
def setTableStatus(request):
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
    _tableId = str(_tableId)
    try:
        table = Table.objects.get(id = _tableId)
    except ObjectDoesNotExist:
        response['code'] = -1
        response['errorMsg'] = 'table查询失败'
        return HttpResponse(json.dumps(response),content_type="application/json")
    if str(table.waiterOrderId) != str(_waiterOrderId):
        response['code'] = -1
        response['errorMsg'] = '您没有权限进行操作'
        return HttpResponse(json.dumps(response),content_type="application/json")

    if  _method == '0':

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
            orderQuery = Order.objects.filter(tableId = _tableId).filter(Q(status = '0')|Q(
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
        response['code'] = -1
        response['errorMsg'] = '您无权进行此操作'
        return HttpResponse(json.dumps(response),content_type="application/json")

    elif  _method == '2':
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
    elif  _method == '3':
        if table.status == '0':
            table.status = '3'
            table.save()
            response['code'] = 0
            response_data = {}
            response_data['tableNumber'] = table.number
            response_data['tablePeopleNumber'] = table.peopleNumber
            response_data['tableStatus'] = table.status
            response_data['tableId'] = table.id
            response['data'] = response_data
            return HttpResponse(json.dumps(response),content_type="application/json")

        elif table.status == '1' or table.status == '2':
            response['code'] = -1
            response['errorMsg'] = '生成订单，餐桌会自动变为忙碌'
            return HttpResponse(json.dumps(response),content_type="application/json")

        elif table.status == '3':
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
