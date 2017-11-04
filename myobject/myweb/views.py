from django.shortcuts import render

from myweb.models import Types,Goods,Users

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

# 自定义公共信息加载函数
def loadContent(request):
    content={}
    content['typeslist'] = Types.objects.filter(pid=0)
    content['typeslists'] = Types.objects.all()[:3]
    content['gdlistphone'] = Goods.objects.filter(typeid__in=Types.objects.only('id').filter(path__contains=','+str(1)+',')).order_by('-num')[:4]
    content['gdlistsmyy'] = Goods.objects.filter(typeid__in=Types.objects.only('id').filter(path__contains=','+str(4)+',')).order_by('-num')[:4]
    content['gdlistznsb'] = Goods.objects.filter(typeid__in=Types.objects.only('id').filter(path__contains=','+str(2)+',')).order_by('-num')[:5]
    content['gdlistgame'] = Goods.objects.filter(typeid__in=Types.objects.only('id').filter(path__contains=','+str(10)+',')).order_by('-num')[:5]

    content['goodslist1'] = Goods.objects.filter(typeid__in=Types.objects.only('id').filter(path__contains=','+str(1)+',')).order_by('-num')[:5]
    content['goodslist2'] = Goods.objects.filter(typeid__in=Types.objects.only('id').filter(path__contains=','+str(2)+',')).all()[:5]
    content['goodslist3'] = Goods.objects.filter(typeid__in=Types.objects.only('id').filter(path__contains=','+str(3)+',')).all()[:5]
    content['goodslist4'] = Goods.objects.filter(typeid__in=Types.objects.only('id').filter(path__contains=','+str(4)+',')).all()[:5]
    return content

# 首页
def index(request):
    content = loadContent(request)

    content['gdlistall'] = Goods.objects.all()
    content['tylistall'] = Types.objects.all()
    content['gdlistnav1'] = Goods.objects.filter(typeid=5).all()[:2]
    content['gdlistnav2'] = Goods.objects.filter(typeid=6).all()[:2]
    content['gdlistnav3'] = Goods.objects.filter(typeid=7).all()[:2]
    content['gdlistnav4'] = Goods.objects.filter(typeid=8).all()[:2]
    content['gdlistnav5'] = Goods.objects.filter(typeid=9).all()[:2]
    content['gdlistnav6'] = Goods.objects.filter(typeid=24).all()[:2]
    content['gdlistnav7'] = Goods.objects.filter(typeid=23).all()[:2]
    content['gdlistnav8'] = Goods.objects.filter(typeid=12).all()[:2]
    content['gdlistnav9'] = Goods.objects.filter(typeid=11).all()[:2]
    content['gdlistnav10'] = Goods.objects.filter(typeid=25).all()[:2]
    content['gdlistnav11'] = Goods.objects.filter(typeid=26).all()[:2]
    content['gdlistnav12'] = Goods.objects.filter(typeid=28).all()[:2]
    content['gdlistnav13'] = Goods.objects.filter(typeid=29).all()[:2]
    content['gdlistnav14'] = Goods.objects.filter(typeid=27).all()[:2]
    content['gdlistnav15'] = Goods.objects.filter(typeid=31).all()[:2]
    content['gdlistnav16'] = Goods.objects.filter(typeid=32).all()[:2]
    
    content['goodshot1'] = Goods.objects.order_by('-num')[:5]
    content['goodshot2'] = Goods.objects.order_by('-num')[5:10]

    
    return render(request,'myweb/index.html',content)

# 列表页
def list(request,gid=0):
    content = loadContent(request)
    if gid == 0:
        #获取所有顶级类别下的1级类别
        content['goodslist'] = Goods.objects.all()
    else:
        #获取1级类别下的所有子类别信息
        content['types'] = Types.objects.filter(pid = gid)
        #判断ttid参数是否有值
        if request.GET.get('ttid',None):
            content['goodslist'] = Goods.objects.filter(typeid = request.GET['ttid'])
        else:
            # 获取指定商品类别下的所有商品信息
            content['goodslist'] = Goods.objects.filter(typeid__in=Types.objects.only('id').filter(path__contains=','+str(gid)+',')).order_by('-num')
    #如果请求排序
    sgbid = request.GET.get('sort',None)
    print(sgbid,type(sgbid))
    if sgbid == '1':
        content['goodslist'] = Goods.objects.filter(typeid__in=Types.objects.only('id').filter(path__contains=','+str(gid)+',')).order_by('-num')
        print(content['goodslist'])
    elif sgbid == '2':
        content['goodslist'] = Goods.objects.filter(typeid__in=Types.objects.only('id').filter(path__contains=','+str(gid)+',')).order_by('-addtime')
        print(2)
    elif sgbid == '3':
        content['goodslist'] = Goods.objects.filter(typeid__in=Types.objects.only('id').filter(path__contains=','+str(gid)+',')).order_by('-price')
        print(3)

    # 获取所需商品列表信息并放置到content
    return render(request,'myweb/list.html',content)


# 详情页
def detail(request,gid):
    content = loadContent(request)
    # 获取对应商品详情信息并放置到content
    gb = Goods.objects.get(id = gid)
    gb.clicknum += 1
    gb.save()
    content['goods'] = gb
    return render(request,'myweb/detail.html',content)

#注册页面
def register(request):
    return render(request,'myweb/register.html')

def regupdate(request):
    #判断两次密码是否一致
    pwd = request.POST['passwd']
    repwd = request.POST['repasswd']
    if repwd != pwd:
        content = {"info":"两次密码不相同,请重新输入!"}
        return render(request,"myweb/register.html",content)
    try:
        gb = Users()
        gb.username = request.POST['username']
        import hashlib
        m = hashlib.md5()
        m.update(bytes(request.POST['passwd'],encoding="utf8"))
        gb.passwd = m.hexdigest()
        gb.email = request.POST['email']
        gb.phone = request.POST['phone']
        gb.addtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        gb.state = 1
        gb.save()
        content={"info":"注册成功!可以登录了"}
        return render(request,"myweb/register.html",content)
    except:
        content={"info":"注册失败!"}
        return render(request,"myweb/register.html",content)


#登录页面
def login(request):
    return render(request,'myweb/login.html')

def dologin(request):
    #验证码判断
    input_code = request.POST.get("showcode")
    if  input_code != request.session['verifycode']:
        content = {'info':'验证码输出错误!'}
        return render(request,'myweb/login.html',content)
    #判断登录账户
    try:
        gb = Users.objects.get(username=request.POST['username'])
        #判断用户是否的管理员
        if gb.state != 2:
            import hashlib
            m = hashlib.md5() 
            m.update(bytes(request.POST['passwd'],encoding="utf8"))
            #判断密码是否正确
            if gb.passwd == m.hexdigest():
                request.session['mywebuser'] = gb.dicts()
                return redirect(reverse('index'))
            else:
                content = {'info':'登录密码错误!'}
        else:
            content = {'info':'登录账户不是注册账户!'}
    except:
        content = {'info':'登录账户错误!'}
    return render(request,'myweb/login.html',content)

def loginout(request):
    #清除登录的session,使用session的单条删除方法
    try:
        del request.session['mywebuser']
        #跳转到用户登录页面
        return redirect(reverse('index'))
    except:
        content = {'info':'没有用户登录,无法返回'}
        return render(request,"myweb/login.html",content)

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

