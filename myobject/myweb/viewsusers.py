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

#==========个人中心=======================
def member(request):
    try:
        ob = Orders.objects.filter(uid = request.session['mywebuser']['id'])
        #代发货订单数量
        newon = 0
        #已发货订单数量
        faon = 0
        for orders in ob:
            #代发货订单
            if orders.status == 0:
                newon += 1
            #已发货订单数量
            elif orders.status == 1:
            	faon += 1
        content = {'newon':newon,'faon':faon}
        return render(request,'myweb/member.html',content)
    except:
        content = {'info':'当前用户未登录,请登录'}
        return render(request,'myweb/login.html',content)

def memberdetail(request):
    try:
        ub = Users.objects.get(id = request.session['mywebuser']['id'])
        content = {'userlist':ub}
        return render(request,'myweb/memberdetail.html',content)
    except:
        content = {'info':'当前用户未登录,请登录'}
        return render(request,'myweb/login.html',content)

def memberchange(request):
    #判断两次输入密码是否一直
    pwd = request.POST['passwd']
    repwd = request.POST['repasswd']
    if  repwd != pwd:
        content={"info":"两次密码不相同,请重新输入!"}
        return render(request,"myweb/memberdetail.html",content)
    ub = Users.objects.get(id = request.session['mywebuser']['id'])
    #获取密码并md5
    import hashlib
    m = hashlib.md5() 
    m.update(bytes(request.POST['passwd'],encoding="utf8"))
    ub.passwd = m.hexdigest()
    ub.email = request.POST['email']
    ub.phone = request.POST['phone']
    ub.save()
    content={'info':'修改成功'}
    return redirect(reverse('memberdetail'),content)
#==========个人中心=======================


#==========订单中心=======================
def order(request):
    #获取当前用户下的所有订单信息
    odb = Orders.objects.only('id').filter(uid = request.session['mywebuser']['id'])
    deb = Detail.objects.filter(orderid__in = Orders.objects.only('id').filter(uid = request.session['mywebuser']['id']))
    gob = []
    for debone in deb:
        gob.append(debone.goodsid)
    goodslist = Goods.objects.filter(id__in=gob)
    content = {'orderlist':odb,'detaillist':deb,'goodslist':goodslist}
    return render(request,'myweb/order.html',content)

#订单详情
def orderdetail(request,odid):
    odb = Orders.objects.filter(id = odid)
    deb = Detail.objects.filter(orderid = odid)
    gob = []
    for debone in deb:
        gob.append(debone.goodsid)
    goodslist = Goods.objects.filter(id__in=gob)
    content = {'orderlist':odb,'detaillist':deb,'goodslist':goodslist}
    return render(request,'myweb/orderdetail.html',content)

#将已发货订单确认收货
def orderoffsta(request):
    #获取Json数据
    ids = request.GET['orid']
    ost = int(request.GET['orstatus'])
    ordb = Orders.objects.get(id = ids)
    ordb.status = ost
    ordb.save()
    return JsonResponse({})
#将新订单进行取消
def ordercelsta(request):
    #获取Json数据
    ids = request.GET['orid']
    order = Orders.objects.get(id=ids)
    ost = int(request.GET['orstatus'])
    order.status = ost
    order.save()
    deb = Detail.objects.filter(orderid=ids)
    for debone in deb:
        gdb = Goods.objects.get(id=debone.goodsid)
        gdb.store += debone.num
        gdb.num -= debone.num
        gdb.save()
    return JsonResponse({})
#==========订单中心=======================
