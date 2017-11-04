#自定义后台中间件
from django.shortcuts import render
#回跳函数的模块
from django.shortcuts import redirect
from django.core.urlresolvers import reverse

#正则匹配的模块
import re

class MywebMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # 定义网站前提台不登录不可以访问的路由url
        urllist = ['/ordersadd']
        # 获取当前请求路径
        path = request.path
        if path in urllist:
            # 判断当前用户是否没有登录
            if "mywebuser" not in request.session:
                # 执行登录界面跳转
                content = {'info':'没有用户登录,请先进行登录'}
                return render(request,"myweb/login.html",content)

        response = self.get_response(request)
        
        # Code to be executed for each request/response after
        # the view is called.

        return response