from django.shortcuts import render

#引入类
from myadmin.models import Types,Goods

#反向需要模块
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.shortcuts import redirect
from django.core.urlresolvers import reverse

#分页需要模块
from django.core.paginator import Paginator
#导入模块
import os,time,json
#图片操作模块
from PIL import Image 

#===============商品分类============================
def typesindex(request):
    #执行数据查询,并放到模版中
    lists =Types.objects.extra(select = {'_has':'concat(path,id)'}).order_by('_has')
    for tb in lists:
        tb.pname = '---'*(tb.path.count(',')-1)
    content = {'typelists':lists}
    return render(request,'myadmin/types/index.html',content)

#商品类别添加    
def typesadd(request,tid):
    if tid == '0':
        content = {'typespid':0,'typespidname':'顶级分类','typespath':'0,'}
    else:
        tb = Types.objects.get(id = tid)
        content = {'typespid':tb.id,'typespidname':tb.name,'typespath':tb.path+str(tb.id)+','}
    return render(request,'myadmin/types/add.html',content)

#类别添加
def typespath(request,tid):
    tlist  = Types.objects.filter(pid = tid)
    lists = []
    for tb in tlist:
        lists.append({'pid':tb.pid,'name':tb.name,'id':tb.id})
        print(tb.name)
    return JsonResponse({'data':lists})

#商品类别增加
def typesinsert(request):
    try:
        list1 = Types.objects.all()
        tb = Types()
        tb.name = request.POST['typesname']
        tb.pid = request.POST['typespid']
        tb.path = request.POST['typespath']
        tb.save()
        content={'typelists':list1,"info":"添加成功!"}
        return render(request,"myadmin/info.html",content)
    except:
        content={"info":"添加失败!"}
        return render(request,"myadmin/info.html",content)

#商品类别删除
def typesdel(request,tid):
    try:
        #获取pid下面的有数据的条数
        row = Types.objects.filter(pid = tid).count()
        if row>0:
            content = {"info":"删除失败:此类别下面还有子类别!"}
            return render(request,"myadmin/info.html",content)
        tb  = Types.objects.get(id = tid)
        tb.delete()
        content={"info":"删除成功!"}
        return render(request,"myadmin/info.html",content)
    except:
        content={"info":"删除失败!"}
        return render(request,"myadmin/info.html",content)

#商品类别编辑
def typesedit(request,tid):
    try:
        tb = Types.objects.get(id = tid)
        content = {'types':tb}
        return render(request,'myadmin/types/edit.html',content)
    except:
        content = {'info':'没有找到需要修改的信息'}
        return render(request,'myadmin/info.html',content)

#商品类别更新
def typesupdate(request,tid):
    tb = Types.objects.get(id = tid)
    tb.name = request.POST['typesname']
    tb.pid = request.POST['typespid']
    tb.path = request.POST['typespath']
    tb.save()
    content = {"info":"修改成功!"}
    return render(request,"myadmin/info.html",content)

#===============商品分类 E==============================


#===============商品信息表 ==============================
#商品信息管理
def goodsindex(request,pIndex):
    lists = Goods.objects.all()
    for gb in lists:
        tlists = Types.objects.get(id = gb.typeid)
        gb.typename = tlists.name
    p = Paginator(lists,5)
    #处理当前页号信息
    if pIndex == "":
        pIndex = '1'
    pIndex = int(pIndex)
     #获取当前页数据
    lists2 = p.page(pIndex)
    plist = p.page_range
    content = {'goodslists':lists2,'pIndex':pIndex,'plist':plist}
    return render(request,'myadmin/goods/index.html',content)
#商品信息添加    
def goodsadd(request):
    # 获取商品的类别信息
    lists = Types.objects.extra(select = {'_has':'concat(path,id)'}).order_by('_has')
    glists = Goods.objects.all()
    content={'typeslists':lists,'goodslists':glists}
    return render(request,'myadmin/goods/add.html',content)

#商品信息增加
def goodsinsert(request):
    try:
        gb = Goods()
        gb.goods = request.POST['goods']
        gb.typeid = request.POST['gtypesid']
        gb.company = request.POST['company']
        gb.descr = request.POST['descr']
        gb.price = request.POST['price']
        gb.store = request.POST['store']
        gb.state = 1
        gb.clicknum = 0
        gb.addtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        #执行图片的上传
        myfile = request.FILES.get("picname", None)
        if not myfile:
            return HttpResponse("没有上传文件信息！")
        #随机图片名
        randfile = str(int(time.time()))+'.'+myfile.name.split('.').pop()
        destination = open(os.path.join("./static/loadimg/",randfile),'wb+')
        for chunk in myfile.chunks():      # 分块写入文件  
            destination.write(chunk)  
        destination.close()
        #图片缩放
        im =  Image.open("./static/loadimg/"+randfile)
        #解决cannot write mode RGBA as JPEG的bug
        im = im.convert('RGB')
        #缩放到375*375
        im.thumbnail((375,375))
        # 把缩放后的图像以自身格式保存:
        im.save("./static/loadimg/"+randfile,None)
        #缩放到220*1220
        im.thumbnail((220,220))
        # 把缩放后的图像用jpeg格式保存:
        im.save("./static/loadimg/l_md_"+randfile,None)
        #缩放到100*100
        im.thumbnail((100,100))
        # 把缩放后的图像用jpeg格式保存:
        im.save("./static/loadimg/c_xs_"+randfile,None)
        gb.picname = randfile
        gb.save()
        content={"info":"添加成功!"}
        return render(request,"myadmin/info.html",content)
    except:
        content={"info":"添加失败!"}
        return render(request,"myadmin/info.html",content)
#商品信息删除
def goodsdel(request,gid):
    try:
        gb  = Goods.objects.get(id = gid)
        fileinfo = gb.picname #获取要删除的文件
        os.remove("./static/loadimg/"+fileinfo) #执行图片文件删除
        os.remove("./static/loadimg/l_md_"+fileinfo) #执行图片文件删除
        os.remove("./static/loadimg/c_xs_"+fileinfo) #执行图片文件删除
        gb.delete()
        content={"info":"删除成功!"}
        return render(request,"myadmin/info.html",content)
    except:
        content={"info":"删除失败!"}
        return render(request,"myadmin/info.html",content)

#商品信息编辑
def goodsedit(request,gid):
    try:
        #获取要编辑的商品信息
        golists = Goods.objects.get(id = gid)
        #获取商品类别信息
        tlists = Types.objects.extra(select = {'_has':'concat(path,id)'}).order_by('_has')
        content = {'typeslists':tlists,'goods':golists}
        return render(request,'myadmin/goods/edit.html',content)
    except:
        content = {'info':'没有找到要修改的信息！'}
        return render(request,'myadmin/info.html',content)

#商品信息更新
def goodsupdate(request,gid):
    try:
        b = False
        oldpicname = request.POST['oldpicname']
        if None != request.FILES.get("pic"):
            myfile = request.FILES.get("pic", None)
            if not myfile:
                return HttpResponse("没有上传文件信息！")
            #随机图片名
            randfile = str(int(time.time()))+'.'+myfile.name.split('.').pop()
            destination = open(os.path.join("./static/loadimg/",randfile),'wb+')
            for chunk in myfile.chunks():      # 分块写入文件  
                destination.write(chunk)  
            destination.close()
            #图片缩放
            im =  Image.open("./static/loadimg/"+randfile)
            #解决cannot write mode RGBA as JPEG的bug
            im = im.convert('RGB')
            #缩放到375*375
            im.thumbnail((375,375))
            # 把缩放后的图像用jpeg格式保存:
            im.save("./static/loadimg/"+randfile,None)
            #缩放到220*1220
            im.thumbnail((220,220))
            # 把缩放后的图像用jpeg格式保存:
            im.save("./static/loadimg/l_md_"+randfile,None)
            #缩放到100*100
            im.thumbnail((100,100))
            # 把缩放后的图像用jpeg格式保存:
            im.save("./static/loadimg/c_xs_"+randfile,None)
            b = True
            picname = randfile
        else:
            picname = oldpicname
        gb = Goods.objects.get(id = gid)
        gb.picname = picname
        gb.goods = request.POST['goods']
        gb.typeid = request.POST['typeid']
        gb.company = request.POST['company']
        gb.descr = request.POST['descr']
        gb.store = request.POST['store']
        gb.state = request.POST['state']
        gb.save()
        content = {"info":"修改成功!"}
        if b:
            os.remove("./static/loadimg/"+oldpicname) #执行老图片文件删除
            os.remove("./static/loadimg/l_md_"+oldpicname) #执行老图片文件删除
            os.remove("./static/loadimg/c_xs_"+oldpicname) #执行老图片文件删除
    except:
        content = {'info':'修改失败!'}
        if b:
            os.remove("./static/loadimg/"+picname) #执行新图片文件删除
            os.remove("./static/loadimg/l_md_"+picname) #执行新图片文件删除
            os.remove("./static/loadimg/c_xs_"+picname) #执行新图片文件删除
    return render(request,"myadmin/info.html",content)

#===============商品信息表 E==============================

