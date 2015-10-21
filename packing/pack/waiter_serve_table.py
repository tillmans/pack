__author__ = 'mike'
#encoding:utf-8
from django.http import HttpResponse
import sys,json
from pack.models import Table,TableLock,WaiterServe,TableCategory
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
import pytz

reload(sys)
sys.setdefaultencoding('utf8')

@csrf_exempt
def waiterServeGetTableList(request):
    response = {}
    response_data = {}
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
    if waiterServe.saler == None:
        response['code'] = 2
        response['errorMsg'] = '请联系管理员关联您的账户'
        return HttpResponse(json.dumps(response),content_type="application/json")

    tableCategoryQuery = TableCategory.objects.select_related().filter(waiterServeId = str(_waiterServeId)).filter(
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
def waiterServeGetTableDetail(request):
    response = {}
    response_data = {}
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
    if waiterServe.saler == None:
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
