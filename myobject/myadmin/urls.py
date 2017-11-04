from django.conf.urls import url

#引入后台管理视图
from . import views,viewsgoods,viewsorders

urlpatterns = [
    #后台首页路由
    url(r'^$', views.index,name='myadmin_index'),

    #会员管理
    url(r'^users(?P<pIndex>[0-9]*)$', views.usersindex,name='myadmin_usersindex'),
    url(r'^usersadd$', views.usersadd,name='myadmin_usersadd'),
    url(r'^usersinsert$', views.usersinsert,name='myadmin_usersinsert'),
    url(r'^usersdel/(?P<uid>[0-9]+)$', views.usersdel,name='myadmin_usersdel'),
    url(r'^usersedit/(?P<uid>[0-9]+)$', views.usersedit,name='myadmin_usersedit'),
    url(r'^usersupdate/(?P<uid>[0-9]+)$', views.usersupdate,name='myadmin_usersupdate'),


    #后台管理员管理
    url(r'^login$', views.login,name='myadmin_login'),
    url(r'^dologin$', views.dologin,name='myadmin_dologin'),
    url(r'^loginout$', views.loginout,name='myadmin_loginout'),

    #验证码管理
    url(r'^showcode$', views.showcode,name='myadmin_showcode'),

    #商品类别
    url(r'^types$', viewsgoods.typesindex,name='myadmin_typesindex'),
    url(r'^typesadd/(?P<tid>[0-9]+)$', viewsgoods.typesadd,name='myadmin_typesadd'),
    url(r'^typesinsert$', viewsgoods.typesinsert,name='myadmin_typesinsert'),
    url(r'^typesdel/(?P<tid>[0-9]+)$', viewsgoods.typesdel,name='myadmin_typesdel'),
    url(r'^typesedit/(?P<tid>[0-9]+)$', viewsgoods.typesedit,name='myadmin_typesedit'),
    url(r'^typesupdate/(?P<tid>[0-9]+)$', viewsgoods.typesupdate,name='myadmin_typesupdate'),
    url(r'^typespath/([0-9]+)$', viewsgoods.typespath,name='myadmin_typespath'),

    #商品信息
    url(r'^goods(?P<pIndex>[0-9]*)$', viewsgoods.goodsindex,name='myadmin_goodsindex'),
    url(r'^goodsadd$', viewsgoods.goodsadd,name='myadmin_goodsadd'),
    url(r'^goodsinsert$', viewsgoods.goodsinsert,name='myadmin_goodsinsert'),
    url(r'^goodsdel/(?P<gid>[0-9]+)$', viewsgoods.goodsdel,name='myadmin_goodsdel'),
    url(r'^goodsedit/(?P<gid>[0-9]+)$', viewsgoods.goodsedit,name='myadmin_goodsedit'),
    url(r'^goodsupdate/(?P<gid>[0-9]+)$', viewsgoods.goodsupdate,name='myadmin_goodsupdate'),

    #订单表
    url(r'^orders/(?P<pIndex>[0-9]*)$', viewsorders.ordersindex,name='myadmin_ordersindex'),
    url(r'^detailshow/(?P<did>[0-9]+)$', viewsorders.detailshow,name='myadmin_detailshow'),
    url(r'^detailstatus$', viewsorders.detailstatus,name='myadmin_detailstatus'),
    url(r'^orderoff/(?P<dofid>[0-9]+)$', viewsorders.orderoff,name='myadmin_orderoff'),#已发货订单展示
    url(r'^orderreceive/(?P<dorid>[0-9]+)$', viewsorders.orderreceive,name='myadmin_orderreceive'),#已收货订单展示
    url(r'^ordernew/(?P<donid>[0-9]+)$', viewsorders.ordernew,name='myadmin_ordernew'),#新订单展示

]
