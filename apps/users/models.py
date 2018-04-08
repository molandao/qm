from django.db import models

from django.contrib.auth.models import AbstractUser

from datetime import datetime
# Create your models here.
# users表是第一个被设计的


class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=50,verbose_name=u"昵称", default="")# 昵称
    birday = models.DateField(verbose_name=u"生日",null=True,blank=True)# 生日
    gender = models.CharField(choices=(("male",u"男"),("female",u"女")),default="female",max_length=7)# 性别
    address = models.CharField(max_length=100, default=u"")# 地址
    mobile = models.CharField(max_length=11, null=True, blank=True)# 手机号，注册
    image = models.ImageField(upload_to="image/%Y/%m", default=u"image/default.png", max_length=100) # 头像

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username

    def unread_nums(self):
        from operation.models import UserMessage
        return UserMessage.objects.filter(user=self.id, has_read=False).count()


    # 为了避免循环引用，分层设计.operation models.py (courses ,organzation, users)
    # 邮箱验证码可以考虑放在users里，首页轮播图也是.

class EmailVerifyRecord(models.Model):
    code = models.CharField(max_length=20, verbose_name=u"验证码")
    email = models.EmailField(max_length=50, verbose_name=u"邮箱")
    send_type = models.CharField(choices=(("register","注册"),("forget",u"找回密码"),("update_email",u"修改邮箱")),max_length=30,verbose_name=u"验证码类型")
    send_time = models.DateTimeField(default=datetime.now,verbose_name=u"发送时间") # 括号要去掉，不然会根据model变异的时间生成，去掉才会根据class实例化的时间生成

    class Meta:
        verbose_name = u"邮箱验证码"
        verbose_name_plural = verbose_name

class Banner(models.Model):
    title = models.CharField(max_length=100, verbose_name=u"标题")
    image = models.ImageField(upload_to="banner/%Y/%m",verbose_name=u"轮播图",max_length=100)
    url = models.URLField(max_length=200, verbose_name=u"访问地址")
    index = models.IntegerField(default=100, verbose_name=u"顺序")
    add_time = models.DateTimeField(default=datetime.now,verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"轮播图"
        verbose_name_plural = verbose_name

        # structure里banner存放轮播图