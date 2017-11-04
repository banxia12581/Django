from django.conf.urls import url

from . import views,viewsorders,viewsusers

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    # 网站前端商品展示
    url(r'^$', views.index, name="index"), #首页
    url(r'^list$', views.list, name="list"), #列表页
    url(r'^list/(?P<gid>[0-9]+)$', views.list, name="list2"), #带参数列表页
    url(r'^detail/(?P<gid>[0-9]+)$', views.detail, name="detail"), #详情页

    #注册页面
    url(r'^register$', views.register, name="register"), 
    url(r'^regupdate$', views.regupdate, name="regupdate"), 
    #登录页面
    url(r'^login$', views.login, name="login"), 
    url(r'^dologin$', views.dologin,name='dologin'),
    url(r'^loginout$', views.loginout,name='loginout'),
    #验证码管理
    url(r'^showcode$', views.showcode,name='showcode'),



    #购物车
    url(r'^cart$', viewsorders.cart, name="cart"),
    url(r'^cartadd/(?P<sid>[0-9]+)$', viewsorders.cartadd, name="cartadd"),#添加购物车
    url(r'^cartchange$', viewsorders.cartchange, name="cartchange"),#修改购物车
    url(r'^cartdel/(?P<sid>[0-9]+)$', viewsorders.cartdel,name='cartdel'), #从购物车中删除一个商品
    url(r'^cartclear$', viewsorders.cartclear,name='cartclear'), #清空购物车
    url(r'^cartchanum$', viewsorders.cartchanum,name='cartchanum'), #购物车数量更改

    #订单
    url(r'^ordersadd$', viewsorders.ordersadd, name="ordersadd"),#订单添加页
    url(r'^ordersconfirm$', viewsorders.ordersconfirm, name="ordersconfirm"),#订单确认页
    url(r'^ordersinsert$', viewsorders.ordersinsert, name="ordersinsert"),#订单提交页
    url(r'^ordersinfo$', viewsorders.ordersinfo, name="ordersinfo"),#订单支付页

    #个人中心
    url(r'^member$', viewsusers.member, name="member"),
    url(r'^memberdetail$', viewsusers.memberdetail, name="memberdetail"),#个人中心修改页
    url(r'^memberchange$', viewsusers.memberchange, name="memberchange"),#个人中心修改页

    #订单中心
    url(r'^order$', viewsusers.order, name="order"),
    url(r'^orderdetail/(?P<odid>[0-9]+)$', viewsusers.orderdetail, name="orderdetail"),#订单详情
    url(r'^orderoffsta$', viewsusers.orderoffsta, name="orderoffsta"),#将已发货订单确认收货
    url(r'^ordercelsta$', viewsusers.ordercelsta, name="ordercelsta"),#将新订单取消收货
]
