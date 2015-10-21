from django.conf.urls import patterns, include, url
from django.contrib import admin
import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'packing.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^sendVerifyCode$','pack.user.sendVerifyCode'),
    url(r'^verifyTelephone$','pack.user.verifyTelephone'),
    url(r'^updateClientID$','pack.user.updateClientID'),
    url(r'^userInfo$','pack.user.userInfo'),
    url(r'^userFeedBack$','pack.user.userFeedBack'),

    url(r'^getShopsNearby$','pack.user_nearby.getShopsNearby'),
    url(r'^getTablesWithShop$','pack.user_nearby.getTablesWithShop'),
    url(r'^userLockTable$','pack.user_nearby.userLockTable'),
    url(r'^userUnlockTable$','pack.user_nearby.userUnlockTable'),
    url(r'^userGetTableLockDetail$','pack.user_nearby.userGetTableLockDetail'),
    url(r'^checkUserTable$','pack.user_nearby.checkUserTable'),
    url(r'^getShopDetail$','pack.user_nearby.getShopDetail'),

    url(r'^getUserOrders$','pack.user_order.getUserOrders'),
    url(r'^getUserOrderDetail$','pack.user_order.getUserOrderDetail'),

    url(r'^aliPay$','pack.user_pay.aliPay'),
    url(r'^getPayResult$','pack.user_pay.getPayResult'),

    url(r'^shopVerifyTelephone$','pack.shop.shopVerifyTelephone'),
    url(r'^shopInfo$','pack.shop.shopInfo'),
    url(r'^shopAddressInfo$','pack.shop.shopAddressInfo'),
    url(r'^getShopAccountInfo$','pack.shop.getShopAccountInfo'),
    url(r'^shopWalletInfo$','pack.shop.shopWalletInfo'),
    url(r'^startService$','pack.shop.startService'),
    url(r'^closeService$','pack.shop.closeService'),
    url(r'^shopFeedback$','pack.shop.shopFeedback'),
    url(r'^shopUpdateClientID$','pack.shop.shopUpdateClientID'),

    url(r'^getShopWaiterOrderList$','pack.shop_member.getShopWaiterOrderList'),
    url(r'^getShopCookList$','pack.shop_member.getShopCookList'),
    url(r'^getShopWaiterServeList$','pack.shop_member.getShopWaiterServeList'),
    url(r'^verifyWaiterOrder$','pack.shop_member.verifyWaiterOrder'),
    url(r'^verifyCook$','pack.shop_member.verifyCook'),
    url(r'^verifyWaiterServe$','pack.shop_member.verifyWaiterServe'),

    url(r'^getCategories$','pack.shop_sku.getCategories'),
    url(r'^categoryInfo$','pack.shop_sku.categoryInfo'),
    url(r'^skuInfo$','pack.shop_sku.skuInfo'),
    url(r'^alterSkuName$','pack.shop_sku.alterSkuName'),
    url(r'^alterSkuImg$','pack.shop_sku.alterSkuImg'),
    url(r'^addSkuSize$','pack.shop_sku.addSkuSize'),
    url(r'^alterSkuSize$','pack.shop_sku.alterSkuSize'),
    url(r'^delSkuSize$','pack.shop_sku.delSkuSize'),
    url(r'^getSkusWithCategory$','pack.shop_sku.adgetSkusWithCategory'),

    url(r'^getTableList$','pack.shop_table.getTableList'),
    url(r'^tableInfo$','pack.shop_table.tableInfo'),
    url(r'^getCategoriesWithTable$','pack.shop_table.getCategoriesWithTable'),
    url(r'^getTableCategoryDetail$','pack.shop_table.getTableCategoryDetail'),
    url(r'^addTableCategory$','pack.shop_table.addTableCategory'),
    url(r'^alterTableNumber$','pack.shop_table.alterTableNumber'),
    url(r'^alterTablePeopleNumber$','pack.shop_table.alterTablePeopleNumber'),
    url(r'^alterTableCategoryWaiterOrder$','pack.shop_table.alterTableCategoryWaiterOrder'),
    url(r'^alterTableCategoryCook$','pack.shop_table.alterTableCategoryCook'),
    url(r'^alterTableCategoryWaiterServe$','pack.shop_table.alterTableCategoryWaiterServe'),
    url(r'^setTableStatus$','pack.shop_table.setTableStatus'),
    url(r'^alterTableCategoryCook$','pack.shop_table.alterTableCategoryCook'),
    url(r'^alterTableCategoryCook$','pack.shop_table.alterTableCategoryCook'),

    url(r'^getShopOrderDetailWithTable$','pack.shop_member.getShopOrderDetailWithTable'),
    url(r'^getShopOrderDetail$','pack.shop_member.getShopOrderDetail'),

    url(r'^waiterOrderInfo$','pack.waiter_order.waiterOrderInfo'),
    url(r'^waiterOrderFeedback$','pack.waiter_order.waiterOrderFeedback'),
    url(r'^waiterOrderUpdateClientID$','pack.waiter_order.waiterOrderUpdateClientID'),

    url(r'^getCategories$','pack.waiter_order_sku.getCategories'),
    url(r'^getShopSkusWithCategory$','pack.waiter_order_sku.getShopSkusWithCategory'),
    url(r'^getShopSkus$','pack.waiter_order_sku.getShopSkus'),

    url(r'^waiterOrderGetTableList$','pack.waiter_order_table.waiterOrderGetTableList'),
    url(r'^waiterOrderGetTableDetail$','pack.waiter_order_table.waiterOrderGetTableDetail'),
    url(r'^setTableStatus$','pack.waiter_order_table.setTableStatus'),

    url(r'^submitOrder$','pack.waiter_order_order.submitOrder'),
    url(r'^addSkusWithOrder$','pack.waiter_order_order.addSkusWithOrder'),
    url(r'^finishOrder$','pack.waiter_order_order.finishOrder'),
    url(r'^getShopOrderDetailWithTable$','pack.waiter_order_order.getShopOrderDetailWithTable'),

    url(r'^cookInfo$','pack.cook.cookInfo'),
    url(r'^cookFeedback$','pack.cook.cookFeedback'),
    url(r'^cookUpdateClientID$','pack.cook.cookUpdateClientID'),

    url(r'^cookInfo$','pack.cook_table.cookInfo'),
    url(r'^cookGetTableDetail$','pack.cook_table.cookGetTableDetail'),

    url(r'^cookGetOrderSkuList$','pack.cook_order.cookGetOrderSkuList'),
    url(r'^cookFinishOrderSku$','pack.cook_order.cookFinishOrderSku'),
    url(r'^cookCancelOrderSku$','pack.cook_order.cookCancelOrderSku'),
    url(r'^getShopOrderDetailWithTable$','pack.cook_order.getShopOrderDetailWithTable'),

    url(r'^cookGetTableList$','pack.waiter_serve.cookGetTableList'),
    url(r'^waiterServeFeedback$','pack.waiter_serve.waiterServeFeedback'),
    url(r'^waiterServeUpdateClientID$','pack.waiter_serve.waiterServeUpdateClientID'),

    url(r'^waiterServeGetTableList$','pack.waiter_serve_table.waiterServeGetTableList'),
    url(r'^waiterServeGetTableDetail$','pack.waiter_serve_table.waiterServeGetTableDetail'),

    url(r'^waiterServeGetOrderSkuList$','pack.cook_serve.waiterServeGetOrderSkuList'),
    url(r'^waiterServeFinishOrderSku$','pack.cook_serve.waiterServeFinishOrderSku'),
    url(r'^getShopOrderDetailWithTable$','pack.cook_serve.getShopOrderfDetailWithTable'),

    url(r'^$','pack.webViews.index'),
    url(r'^shopProtocol$','pack.webViews.shopProtocol'),
    url(r'^userProtocol$','pack.webViews.userProtocol'),

    ( r'^js/(?P<path>.*)$', 'django.views.static.serve',
            { 'document_root': settings.STATIC_URL+'js/'}
    ),

    ( r'^css/(?P<path>.*)$', 'django.views.static.serve',
            { 'document_root': settings.STATIC_URL+'css/' }
    ),
 
    ( r'^img/(?P<path>.*)$', 'django.views.static.serve',
            { 'document_root': settings.STATIC_URL+'img/' }
    ),
)
