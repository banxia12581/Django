from django.shortcuts import render

#引入类
from myadmin.models import Orders,Detail,Goods,Users

#反向需要模块
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.shortcuts import redirect
from django.core.urlresolvers import reverse

#分页需要模块
from django.core.paginator import Paginator
#导入模版
import os,time,json



#===============订单管理 ==============================
#订单管理
def ordersindex(request,pIndex):
    lists = Orders.objects.all()
    userslist = Users.objects.all()
    p = Paginator(lists,6)
    #处理当前页号信息
    if pIndex == "":
        pIndex = '1'
    pIndex = int(pIndex)
     #获取当前页数据
    lists2 = p.page(pIndex)
    plist = p.page_range
    context = {'orderslists':lists2,'pIndexi':pIndex,'plist':plist,'userslist':userslist}
    return render(request,'myadmin/orders/index.html',context)

#订单详情展示
def detailshow(request,did):
    orb = Orders.objects.get(id = did)
    deb = Detail.objects.filter(orderid  =  did)
    userslist = Users.objects.all()
    gob = []
    for debone in deb:
        gob.append(debone.goodsid)
    goodslist = Goods.objects.filter(id__in=gob)
    content1 = {'detaillists':deb,'orderslist':orb,'goodslist':goodslist,'userslist':userslist}
    return render(request,"myadmin/orders/detailshow.html",content1)

#订单状态修改
def detailstatus(request):
    #获取Json数据
    ids = request.GET['oid']
    ost = int(request.GET['ostatus'])
    ordb = Orders.objects.get(id = ids)
    detb = Detail.objects.filter(orderid = ids)
    for detone in detb:
        gdb = Goods.objects.get(id = detone.goodsid)
        if ost == 3:
            gdb.store +=detone.num
            gdb.save()
    ordb.status = ost
    ordb.save()
    return JsonResponse({})

#新订单管理
def ordernew(request,donid):
    lists = []
    userslist = Users.objects.all()
    ordb = Orders.objects.all()
    for ordone in ordb:
        if ordone.status == 0:
            lists.append(ordone)
    p = Paginator(lists,6)
    #处理当前页号信息
    if donid == "":
        donid = '1'
    donid = int(donid)
     #获取当前页数据
    lists2 = p.page(donid)
    plist = p.page_range
    context = {'orderslists':lists2,'pIndexn':donid,'plist':plist,'userslist':userslist}
    return render(request,'myadmin/orders/index.html',context)

#已发货订单管理
def orderoff(request,dofid):
    lists = []
    userslist = Users.objects.all()
    ordb = Orders.objects.all()
    for ordone in ordb:
        if ordone.status == 1:
            lists.append(ordone)
    p = Paginator(lists,6)
    #处理当前页号信息
    if dofid == "":
        dofid = '1'
    dofid = int(dofid)
     #获取当前页数据
    lists2 = p.page(dofid)
    plist = p.page_range
    context = {'orderslists':lists2,'pIndexo':dofid,'plist':plist,'userslist':userslist}
    return render(request,'myadmin/orders/index.html',context)

#已收货订单管理
def orderreceive(request,dorid):
    lists = []
    userslist = Users.objects.all()
    ordb = Orders.objects.all()
    for ordone in ordb:
        if ordone.status == 2:
            lists.append(ordone)
    p = Paginator(lists,6)
    #处理当前页号信息
    if dorid == "":
        dorid = '1'
    dorid = int(dorid)
     #获取当前页数据
    lists2 = p.page(dorid)
    plist = p.page_range
    context = {'orderslists':lists2,'pIndexr':dorid,'plist':plist,'userslist':userslist}
    return render(request,'myadmin/orders/index.html',context)
#===============订单管理 E==============================
