from django.db import models

#会员类
class Users(models.Model):
    username = models.CharField(max_length=32)
    name = models.CharField(max_length=16)
    passwd = models.CharField(max_length=32)
    sex = models.IntegerField()
    address = models.CharField(max_length=255)
    code = models.CharField(max_length=6)
    phone = models.CharField(max_length=16)
    email = models.CharField(max_length=50)
    state = models.IntegerField()
    addtime = models.CharField(max_length=50)
    def dicts(self):
        return {'id':self.id,'username':self.username,'name':self.name,'address':self.address,'phone':self.phone,'code':self.code,'email':self.email,'shopcart':{}}


#商品类别类
class Types(models.Model):
    name = models.CharField(max_length=32)
    pid = models.IntegerField()
    path = models.CharField(max_length=255)
    def dodict(self):
        return {'id':self.id,'pid':self.pid}

#商品信息表类
class Goods(models.Model):
    typeid = models.IntegerField()
    goods = models.CharField(max_length=32)
    company = models.CharField(max_length=50)
    descr = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    picname = models.CharField(max_length=255)
    state = models.IntegerField()
    store = models.IntegerField()
    num = models.IntegerField()
    clicknum = models.IntegerField()
    addtime = models.CharField(max_length=32)
    def dicts(self):
        return {'id':self.id,'goods':self.goods,'price':self.price,'num':self.num,'picname':self.picname,'num':self.num,'store':self.store,'descr':self.descr,'m':1}



#订单表类
class Orders(models.Model):
    uid = models.IntegerField()
    linkman = models.CharField(max_length=32)
    address = models.CharField(max_length=255)
    code = models.CharField(max_length=6)
    phone = models.CharField(max_length=16)
    addtime = models.CharField(max_length=32)
    total = models.DecimalField(max_digits=8, decimal_places=2)
    status = models.IntegerField()
    def dicts(self):
        return {'uid':self.uid,'status':self.status,'linkman':self.linkman,'phone':self.phone}

#订单详情表类
class Detail(models.Model):
    orderid = models.IntegerField()
    goodsid = models.IntegerField()
    name = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    num = models.IntegerField()