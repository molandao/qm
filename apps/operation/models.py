from datetime import datetime

from django.db import models

from users.models import UserProfile
from articles.models import Article

# Create your models here.


class UserSearch(models.Model):# 文章查询
    name = models.CharField(max_length=20,verbose_name=u"作者笔名")
    # mobile = models.CharField(max_length=11,verbose_name=u"手机号")
    article_name = models.CharField(max_length=50,verbose_name=u"文章标题")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"文章查询"
        verbose_name_plural = verbose_name


class ArticleComments(models.Model):
    # 文章评论
    user = models.ForeignKey(UserProfile,verbose_name=u"用户笔名",on_delete=models.CASCADE)
    article = models.ForeignKey(Article, verbose_name=u"文章",on_delete=models.CASCADE)
    comments = models.CharField(max_length=200,verbose_name=u"评论")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"文章评论"
        verbose_name_plural = verbose_name


class UsersFavorite(models.Model):# 用户收藏
    user = models.ForeignKey(UserProfile,verbose_name=u"用户笔名",on_delete=models.CASCADE)
    fav_id = models.IntegerField(default=0, verbose_name=u"数据id")
    fav_type = models.IntegerField(choices=((1,"文章"),(2,"组织"),(3,"作者")),default=1,verbose_name=u"收藏类型")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"用户收藏"
        verbose_name_plural = verbose_name


class UserMessage(models.Model):
    user = models.IntegerField(default=0,verbose_name=u"接收用户")    # 不用外键的原因是消息发给全员
    message = models.CharField(max_length=500,verbose_name=u"消息内容")
    has_read = models.BooleanField(default=False, verbose_name=u"是否已读")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"用户消息"
        verbose_name_plural = verbose_name


class UserBrowsedArticles(models.Model):
    user = models.ForeignKey(UserProfile,verbose_name=u"用户笔名",on_delete=models.CASCADE)
    article = models.ForeignKey(Article, verbose_name=u"文章",on_delete=models.CASCADE)
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"用户文章"
        verbose_name_plural = verbose_name
