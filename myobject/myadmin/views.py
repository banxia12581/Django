from django.shortcuts import render

#引入类
from myadmin.models import Orders,Detail,Goods,Users

#反向需要模块
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import redirect
from django.core.urlresolvers import reverse

#分页需要模块
from django.core.paginator import Paginator
#导入模版
import os,time,json

#验证加密解密
import django.utils.timezone as timezone

#===============视图方法==============================

#后台首页视图方法
def index(request):
    #所有用户
    ub = Users.objects.all()
    #新订单/待处理订单
    orbs = Orders.objects.filter(status=0)
    #订单总数
    orb = Orders.objects.all()
    #商品总数
    gdb = Goods.objects.filter(state = 1)
    usl = len(ub)
    orl = len(orb)
    orsl = len(orbs)
    gdl = len(gdb)
    content={'usl':usl,'orl':orl,'orsl':orsl,'gdl':gdl}

    return render(request,'myadmin/index.html',content)

#===============后台管理员============================

def login(request):
    return render(request,'myadmin/login.html')

def dologin(request):
    #验证码判断
    input_code = request.POST.get("showcode")
    if  input_code != request.session['verifycode']:
        content = {'info':'验证码输出错误!'}
        return render(request,'myadmin/login.html',content)
    #判断登录账户
    try:
        ob = Users.objects.get(username=request.POST['username'])
        #判断用户是否的管理员
        if ob.state == 0:
            import hashlib
            m = hashlib.md5() 
            m.update(bytes(request.POST['passwd'],encoding="utf8"))
            #判断密码是否正确
            if ob.passwd == m.hexdigest():
                request.session['adminuser'] = ob.name
                return redirect(reverse('myadmin_index'))
            else:
                content = {'info':'登录密码错误!'}
        else:
            content = {'info':'登录账户不是系统管理员!'}
    except:
        content = {'info':'登录账户错误!'}
    return render(request,'myadmin/login.html',content)

def loginout(request):
    #清除登录的session,使用session的单条删除方法
    del request.session['adminuser']
    #跳转到用户登录页面
    return redirect(reverse('myadmin_login'))

#===============后台管理员 E===========================


#===============验证码管理 ============================

def showcode(request):
    #引入随机函数模块
    import random
    from PIL import Image, ImageDraw, ImageFont
    #定义变量，用于画面的背景色、宽、高
    #bgcolor = (random.randrange(20, 100), random.randrange(
    #    20, 100),100)
    bgcolor = (238,238,238)
    width = 100
    height = 30
    #创建画面对象
    im = Image.new('RGB', (width, height), bgcolor)
    #创建画笔对象
    draw = ImageDraw.Draw(im)
    #调用画笔的point()函数绘制噪点
    for i in range(0, 100):
        xy = (random.randrange(0, width), random.randrange(0, height))
        fill = (random.randrange(0, 220), random.randrange(0, 245), random.randrange(0, 255))
        draw.point(xy, fill=fill)
    #定义验证码的备选值
    str1 = 'ABCD123EFGHIJK456LMNOPQRS789TUVWXYZ0'
    #随机选取4个值作为验证码
    rand_str = ''
    for i in range(0, 4):
        rand_str += str1[random.randrange(0, len(str1))]
    #构造字体对象，ubuntu的字体路径为“/usr/share/fonts/truetype/freefont”
    font = ImageFont.truetype('static/STXIHEI.TTF', 21)
    #font = ImageFont.load_default().font
    #构造字体颜色
    fontcolor = (255, random.randrange(0, 255), random.randrange(0, 255))
    #绘制4个字
    draw.text((5, 2), rand_str[0], font=font, fill=fontcolor)
    draw.text((25, 2), rand_str[1], font=font, fill=fontcolor)
    draw.text((50, 2), rand_str[2], font=font, fill=fontcolor)
    draw.text((75, 2), rand_str[3], font=font, fill=fontcolor)
    #释放画笔
    del draw
    #存入session，用于做进一步验证
    request.session['verifycode'] = rand_str
    """
    python2的为
    # 内存文件操作
    import cStringIO
    buf = cStringIO.StringIO()
    """
    # 内存文件操作-->此方法为python3的
    import io
    buf = io.BytesIO()
    #将图片保存在内存中，文件类型为png
    im.save(buf, 'png')
    #将内存中的图片数据返回给客户端，MIME类型为图片png
    return HttpResponse(buf.getvalue(), 'image/png')

#===============验证码管理 E ===========================



#===============会员管理 ==============================
#会员管理
def usersindex(request,pIndex):
    lists = Users.objects.all()
    p = Paginator(lists,6)
    #处理当前页号信息
    if pIndex == "":
        pIndex = '1'
    pIndex = int(pIndex)
     #获取当前页数据
    lists2 = p.page(pIndex)
    plist = p.page_range
    context = {'userslists':lists2,'pIndex':pIndex,'plist':plist}
    return render(request,'myadmin/users/index.html',context)
#会员添加    
def usersadd(request):
    lists = Users.objects.all()
    content={'userslists':lists}
    return render(request,'myadmin/users/add.html',content)

#会员增加
def usersinsert(request):
    #判断两次输入密码是否一直
    pwd = request.POST['passwd']
    repwd = request.POST['repasswd']
    if  repwd != pwd:
        content={"info":"两次密码不相同,请重新输入!"}
        return render(request,"myadmin/users/add.html",content)
    try:
        ob = Users()
        ob.name = request.POST['name']
        ob.username = request.POST['username']
        #获取密码并md5
        import hashlib
        m = hashlib.md5() 
        m.update(bytes(request.POST['passwd'],encoding="utf8"))
        ob.passwd = m.hexdigest()
        ob.sex = request.POST['sex']
        ob.email = request.POST['email']
        ob.code = request.POST['code']
        ob.address = request.POST['address']
        ob.phone = request.POST['phone']
        ob.state = 1
        ob.addtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        ob.save()
        content={"info":"添加成功!"}
        return render(request,"myadmin/info.html",content)
    except:
        content={"info":"添加失败!"}
        return render(request,"myadmin/info.html",content)

#会员删除
def usersdel(request,uid):
    try:
        ob  = Users.objects.get(id = uid)
        ob.delete()
        content={"info":"删除成功!"}
        return render(request,"myadmin/info.html",content)
    except:
        content={"info":"删除失败!"}
        return render(request,"myadmin/info.html",content)

#会员编辑
def usersedit(request,uid):
    try:
        ob = Users.objects.get(id = uid)
        content = {'users':ob}
        return render(request,'myadmin/users/edit.html',content)
    except:
        content = {'info':'没有找到需要修改的信息'}
        return render(request,'myadmin/info.html',content)

#会员更新
def usersupdate(request,uid):
    try:
        ob = Users.objects.get(id = uid)
        ob.name = request.POST['name']
        ob.sex = request.POST['sex']
        ob.email = request.POST['email']
        ob.code = request.POST['code']
        ob.address = request.POST['address']
        ob.phone = request.POST['phone']
        ob.state = request.POST['state']
        ob.save()
        content = {"info":"修改成功!"}
    except:
        context = {'info':'修改失败!'}
    return render(request,"myadmin/info.html",content)

#===============会员管理 E==============================