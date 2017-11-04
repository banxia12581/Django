1.文件说明

myobject：仿魅族商城项目

myshop.sql：数据库

2.运行环境

开发语言：python3.6

数据库：pymysql

操作系统：linux

3.系统结构

4.1项目的目录结构

此次商城系统主要分前台和后台两部分.主要结构是基于Django框架的结构,前台和后台分别对应文件组,前台文件为myweb,后台文件为myadmin.具体结构如下所示:

myobject/

├── manage.py

├── myobject

│   ├── init.py

│   ├── pycache

│   ├── settings.py

│   ├── urls.py

│   └── wsgi.py

├── myadmin                  #网站后台

│   ├── adminmiddleware.py    #中间键文件

│   ├── models.py             #模版文件

│   ├── urls.py                #路由文件

│   ├── viewsgoods.py         #商品管理视图

│   ├── viewsorders.py         #订单管理视图

│   └── views.py               #后台管理视图

├── myweb                    #网站前台

│   ├── models.py             #模版文件

│   ├── urls.py                #路由文件

│   ├── viewsorders.py         #订单管理视图

│   ├── views.py               #前台管理视图

│   └── viewsusers.py          #个人中心管理视图

├── static                     #网站静态文件

│   ├── loadimg              #后台商品上传图片文件

│   ├── myadmin             #网站后台静态文件

│   │   ├── css               #css样式文件

│   │   ├── fonts             #字体文件

│   │   ├── img              #图片文件

│   │   └── js                #JS文件

│   ├── myweb               #网站前台静态文件

│   │   ├── css               #css样式文件

│   │   ├── fonts             #字体文件

│   │   ├── img              #图片文件

│   │   └── js                #JS文件

│   └── STXIHEI.TTF           

└── templates                #模板目录

    ├── myadmin             #后台模板总目录

    │   ├── base.html

    │   ├── goods            #商品信息管理模板

    │   │   ├── add.html

    │   │   ├── edit.html

    │   │   └── index.html

    │   ├── index.html

    │   ├── info.html

    │   ├── login.html

    │   ├── orders                 #订单信息管理模板

    │   │   ├── detailshow.html

    │   │   └── index.html

    │   ├── types                  #后台类别管理模板

    │   │   ├── add.html

    │   │   ├── edit.html

    │   │   └── index.html

    │   └── users                  #后台会员管理

    │       ├── add.html

    │       ├── edit.html

    │       └── index.html

    └── myweb                   #前台模板目录

        ├── base.html   

        ├── cart.html              #购物车页面

        ├── detail.html             #商品详情页面

        ├── index.html             #首页

        ├── list.html               #商品列表页

        ├── login.html             #登录页

        ├── memberdetail.html

        ├── member.html          #个人中心页

        ├── menu.html

        ├── orderdetail.html        #订单详情页

        ├── order.html             #个人中心订单展示页

        ├── ordersadd.html         #订单添加页

        ├── orderscash.html

        ├── ordersconfirm.html

        └── register.html            #注册页面

 

按照Django的要求,前台和后台文件独立,视图和模型分别写views目录和 models 目录中,前台和后台都有各自的视图和模型文件.

4.操作说明

4.1 登录用户

1.后台用户

唯一用户：admin

密码123456

2.前台

可新注册

也可以使用数据库里的用户如yexiutuo/reningyuan/linhan

密码均为：123456

