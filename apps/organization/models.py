from datetime import datetime

from django.db import models

# Create your models here.
'''
class CityDict(models.Model):
    name = models.CharField(max_length=20,verbose_name=u"城市")
    desc = models.CharField(max_length=200,verbose_name=u"描述")
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = u"城市"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name
'''

class ArticleOrg(models.Model):
    name = models.CharField(max_length=50,verbose_name=u"组织名称")
    desc = models.CharField(verbose_name=u"描述",max_length=100)
    click_nums = models.IntegerField(default=0,verbose_name=u"点击数")
    fav_nums = models.IntegerField(default=0,verbose_name=u"收藏数")
    image = models.ImageField(upload_to="org/%Y/%m",verbose_name=u"logo",max_length=100)
    #address = models.CharField(max_length=150, verbose_name=u"组织地址")
    #city = models.ForeignKey(CityDict,verbose_name="所在城市")
    category = models.CharField(max_length=20, choices=(("zzjg","组织机构"),("gx","高校"),("gr","个人")), verbose_name=u"组织类别",default="zzjg")
    readers = models.IntegerField(default=0, verbose_name=u"阅读人数")
    article_nums = models.IntegerField(default=0, verbose_name=u"文章数")

    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = u"组织机构"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Author(models.Model):
    org = models.ForeignKey(ArticleOrg,verbose_name=u"所属组织",on_delete=models.CASCADE)
    # 爱好，文风，兴趣
    name = models.CharField(max_length=20,verbose_name=u"笔名")
    mu_years = models.IntegerField(default=0,verbose_name=u"网龄")
    # work_company = models.CharField(max_length=50, verbose_name=u"就职公司")
    # work_position = models.CharField(max_length=50,verbose_name=u"公司职位")
    writing_style = models.CharField(max_length=50,verbose_name=u"文章风格")
    click_nums = models.IntegerField(default=0,verbose_name=u"点击数")
    fav_nums = models.IntegerField(default=0,verbose_name=u"收藏数")
    image = models.ImageField(upload_to="authors/%Y%m",verbose_name=u"头像",max_length=100,default="")

    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = u"作者"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
