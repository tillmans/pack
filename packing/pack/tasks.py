# encoding:utf-8
from __future__ import absolute_import
import time
from celery.task import task
from pack.pack_push_2_user import pushAPN,pushMessageToSingle
from pack.messageNotify import notify
from pack.models import Order,Table,OrderRecord
import logging,datetime

@task

def sendMsg(clientID, type, orderId, telephone):
    print("sendMsg")
    pushRst = pushMessageToSingle(clientID,type,orderId)
    if pushRst['result'] != 'successed_online':
        notify(telephone,type)

@task

def tableTask(orderId):
    logger = logging.getLogger('Pack.app')
    logger.info("tableTask")
    logger.info(orderId)
    print('tableTask')
    time.sleep(60*5)
    try:
        order = Order.objects.get(id = orderId)
    except:
        print('no such order')
    if str(order.status) == '0':
        order.status = '100'
        order.save()
        record = u'您的订单失效了，已取消'
        record = OrderRecord(record = record,order=order,date = datetime.datetime.now())
        record.save()
        _tableId = order.tableId
        try:
            table = Table.objects.get(id = _tableId)
        except:
            logger.info('not found such table')
        else:
            table.status = '0'
            table.userId = ''
            table.lockTimeStamp = '0'
            table.save()
        _deviceInfo = order.saler.deviceInfo
        if(len(_deviceInfo and "iOS") == 3):
            pushRst = pushAPN(order.user.deviceToken,'1001',str(order.id))
            logger.info(pushRst)
        elif(len(_deviceInfo and 'Android') == 7):
            pushRst = pushMessageToSingle(order.user.clientID,'1001',str(order.id))
            print(pushRst['result'])
            if pushRst['result'] != 'successed_online':
                notify(order.saler.telephone,'1')

@task

def checkTableStatusTask(currentTimeStamp,userId,tableId):
    logger = logging.getLogger('Pack.app')
    logger.info("tableTask")
    logger.info(tableId)
    print('tableTask')
    time.sleep(60*2)
    try:
        table = Table.objects.get(id = tableId)
    except:
        print('no such order')
    if str(table.userId) == str(userId) and str(table.lockTimeStamp) == str(currentTimeStamp) and str(table.status) == '2':
        table.status = '0'
        table.userId = '0'
        table.lockTimeStamp = '0'
        table.save()

