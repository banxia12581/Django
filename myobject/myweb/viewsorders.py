from django.shortcuts import render

from myweb.models import Types,Goods,Users,Orders,Detail

#反向需要模块
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.shortcuts import redirect
from django.core.urlresolvers import reverse

#分页需要模块
from django.core.paginator import Paginator
#导入模版
import os,time,json


# 自定义公共信息加载函数
def loadContent(request):
    content={}
    content['typeslist'] = Types.objects.filter(pid=0)
    content['typeslists'] = Types.objects.all()[:3]

    content['goodslist1'] = Goods.objects.filter(typeid__in=Types.objects.only('id').filter(path__contains=','+str(1)+',')).all()[:5]
    content['goodslist2'] = Goods.objects.filter(typeid__in=Types.objects.only('id').filter(path__contains=','+str(2)+',')).all()[:5]
    content['goodslist3'] = Goods.objects.filter(typeid__in=Types.objects.only('id').filter(path__contains=','+str(3)+',')).all()[:5]
    content['goodslist4'] = Goods.objects.filter(typeid__in=Types.objects.only('id').filter(path__contains=','+str(4)+',')).all()[:5]
    return content


#===============购物车================================
def cart(request):
    content = loadContent(request)
    # 获取对应商品详情信息并放置到content
    if 'shoplist' not in request.session:
        request.session['shoplist'] = {}
    return render(request,"myweb/cart.html",content)

def cartadd(request,sid):
    sd = Goods.objects.get(id = sid)
    #获取要放入购物车的商品信息
    shop = sd.dicts()
    #获取商品添加数量
    shop['m'] = int(request.POST['m'])
    #从session中获取购物车信息
    if 'shoplist' in request.session:
        shoplist = request.session['shoplist']
    else:
        shoplist = {}
    #判断购物车中是否已经存在该商品
    if sid in shoplist:
        #已存在该商品则数量相加
        shoplist[sid]['m'] += shop['m']
    else:
        #如果不存在,添加新商品
        shoplist[sid] = shop
    request.session['shoplist'] =shoplist
    return redirect(reverse('cart'))

def cartchange(request):
    content = loadContent(request)
    # 获取对应商品详情信息并放置到content
    shoplist = request.session['shoplist']
    #获取修改数量的商品
    shopsid = request.GET['sid']
   
    num = int(request.GET['num'])
    if num < 1:
        num = 1
    shoplist[shopsid]['m'] = num
    request.session['shoplist'] = shoplist
    return render(request,"myweb/cart.html")

def cartdel(request,sid):
    shoplist = request.session['shoplist']
    del shoplist[sid]
    request.session['shoplist'] = shoplist
    return redirect(reverse('cart'))

def cartclear(request):
    content = loadContent(request)
    request.session['shoplist'] = {}
    return render(request,"myweb/cart.html",content)

def cartchanum(request):
    shoplist = request.session['shoplist']
    #获取json的数据
    goodsid = request.GET['goodsid']
    goodsnum = int(request.GET['goodsnum'])
    #获取购物车商品对应的库存
    goodone = Goods.objects.get(id  = goodsid) 
    if goodsnum < 1:
        goodsnum = 1
    if goodsnum > goodone.state:
        goodsnum = goodone.state
    #将json传过来的值传回购物车页面
    shoplist[goodsid]['m'] = goodsnum
    request.session['shoplist'] = shoplist
    content={'info':'库存不足'}
    return JsonResponse(content)
#===============购物车E===============================

#===============订单页================================
#订单页
def ordersadd(request):
    ids = request.GET['gids']
    if ids == '':
        return HttpResponse('当前没有需要结算的商品,请选择需要结算的商品')
    gids = ids.split(',')
    #获取购物车中的信息
    shoplist = request.session['shoplist']
    #封装要结算的商品信息,以及商品总金额
    orderlist = {}
    total = 0
    for sid in gids:
        orderlist[sid] = shoplist[sid]
        total += shoplist[sid]['price']* shoplist[sid]['m']
        request.session['orderlist'] = orderlist
        request.session['total'] = total
        #进入结算之后删除购物车的商品
        del shoplist[sid]
    request.session['shoplist'] = shoplist
    return render(request,"myweb/ordersadd.html")
#订单确认页
def ordersconfirm(request):
    return render(request,"myweb/ordersconfirm.html")
#订单提交页
def ordersinsert(request):
    try:
        #封装订单信息
        orders = Orders()
        orders.uid = request.session['mywebuser']['id']
        orders.linkman = request.POST['linkman']
        orders.phone = request.POST['phone']
        orders.address = request.POST['address']
        orders.code = request.POST['code']
        orders.addtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        orders.total = request.session['total']
        orders.status = 0
        orders.save()
        #获取订单详情
        orderlist = request.session['orderlist']
        #遍历订单信息
        for shop in orderlist.values():
            detail = Detail()
            detail.orderid = orders.id
            detail.goodsid = shop['id']
            detail.name = shop['goods']
            detail.price = shop['price']
            detail.num = shop['m']
            detail.save()
            #点击下单数据库商品购买数量增加,库存数量减少
            gdb = Goods.objects.filter(id = shop['id'])
            for gdbone in gdb:
                gdbone.num += shop['m']
                gdbone.store -= shop['m']
                gdbone.save()
        content = {'ordersid':orders.id,'orderstotal':orders.total}
        return render(request,"myweb/orderscash.html",content)
    except:
        content = {'info':'当前用户未登录,请登录'}
        return render(request,'myweb/login.html',content)

#支付信息
def ordersinfo(request):
    return render(request,"myweb/orderscash.html")

#===============订单页E===============================
