from django.contrib import admin
from pack.models import User,ShopWallet,Shop,Category,WaiterOrder,Cook,WaiterServe
from pack.models import Sku,SkuSize,Table,TableCategory,TableLock,Order,OrderSku,OrderRecord,ShopEvaluate
from pack.models import TransferMoney,ShopFeedBack,WaiterOrderFeedBack,CookFeedBack,WaiterServeFeedBack,UserFeedBack
# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ('id','telephone','headImage', 'name','lastLoginTime','clientID','deviceToken','deviceInfo')
admin.site.register(User,UserAdmin)

class ShopWalletAdmin(admin.ModelAdmin):
    list_display = ('id','realName','cardNumber','cardType','moneyLeft','moneyTotal','moneyTotalOnPlatform')
admin.site.register(ShopWallet,ShopWalletAdmin)

class ShopAdmin(admin.ModelAdmin):
    list_display = ('id','setInfoStatus','shopwallet','telephone','name''headImage',
                   'type','desc','isServiceOn','startTimeStamp','endTimeStamp','star',
                   'location','province','city','district','addressDetail','lastLoginTime','clientID',
                    'deviceToken','deviceInfo')

admin.site.register(Shop,ShopAdmin)

class WaiterOrderAdmin(admin.ModelAdmin):
    list_display = ('id','shop','telephone','name','headImage','clientID','lastLoginTime','clientID',
                    'deviceToken','deviceInfo')
admin.site.register(WaiterOrder,WaiterOrderAdmin)

class CookAdmin(admin.ModelAdmin):
    list_display = ('id','shop','telephone','name','headImage','clientID','lastLoginTime','clientID',
                    'deviceToken','deviceInfo')
admin.site.register(Cook,CookAdmin)

class WaiterServeAdmin(admin.ModelAdmin):
    list_display = ('id','shop','telephone','name','headImage','clientID','lastLoginTime','clientID',
                    'deviceToken','deviceInfo')
admin.site.register(WaiterServe,WaiterServeAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','categoryName','saler')

admin.site.register(Category,CategoryAdmin)

class SkuAdmin(admin.ModelAdmin):
    list_display = ('id','name','desc', 'category','img','isValid')

admin.site.register(Sku,SkuAdmin)

class SkuSizeAdmin(admin.ModelAdmin):
    list_display = ('id','name','price')

admin.site.register(SkuSize,SkuSizeAdmin)


class TableAdmin(admin.ModelAdmin):
    list_display = ('id','shop','number','isValid','peopleNumber','status')

admin.site.register(Table,TableAdmin)

class TableCategoryAdmin(admin.ModelAdmin):
    list_display = ('id','table','category','waiterOrder','cook','waiterServe')
admin.site.register(TableCategory,TableCategoryAdmin)

class TableLockAdmin(admin.ModelAdmin):
    list_display = ('id','table','user','date','isValid')
admin.site.register(TableLock,TableLockAdmin)


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id','userId','shop', 'tableId','tableNumber',
                    'status','priceTotal','note','thirdChargeNO','date')

admin.site.register(Order,OrderAdmin)

class OrderSkuAdmin(admin.ModelAdmin):
    ist_display = ('id','order','tableId','skuId','skuName','skuPrice', 'skuSizeName','skuQuantity','status',
                   'waiterOrderId','cookId','waiterServeId')

admin.site.register(OrderSku,OrderSkuAdmin)

class OrderRecordAdmin(admin.ModelAdmin):
    list_display = ('id','order','record','date')

admin.site.register(OrderRecord,OrderRecordAdmin)

class ShopEvaluateAdmin(admin.ModelAdmin):
    list_display = ('id','user','shop','star','date')
admin.site.register(ShopEvaluate,ShopEvaluateAdmin)

class TransferMoneyAdmin(admin.ModelAdmin):
    list_display = ('id','shop','total','startDateString','endDateString','date')
admin.site.register(TransferMoney,TransferMoneyAdmin)

class ShopFeedBackAdmin(admin.ModelAdmin):
    list_display = ('shop','msg')

admin.site.register(ShopFeedBack,ShopFeedBackAdmin)

class WaiterOrderFeedBackAdmin(admin.ModelAdmin):
    list_display = ('waiterOrder','msg')

admin.site.register(WaiterOrderFeedBack,WaiterOrderFeedBackAdmin)

class CookFeedBackAdmin(admin.ModelAdmin):
    list_display = ('cook','msg')

admin.site.register(Cook,CookFeedBackAdmin)

class WaiterServeFeedBackAdmin(admin.ModelAdmin):
    list_display = ('WaiterServe','msg')

admin.site.register(WaiterServe,WaiterServeFeedBackAdmin)

class UserFeedBackAdmin(admin.ModelAdmin):
    list_display = ('user','msg')

admin.site.register(UserFeedBack,UserFeedBackAdmin)

