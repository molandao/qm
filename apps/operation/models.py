from datetime import datetime

from django.db import models

from users.models import UserProfile
from articles.models import Article

# Create your models here.


class UserSearch(models.Model):# 文章查询 想看……
    name = models.CharField(max_length=20,verbose_name=u"用户名")
    article_name = models.CharField(max_length=50,verbose_name=u"文章关键词")
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

        # fields = ['name','desc','detail','art_len','read_times','category','tag','author','youneed_know','image']


# class PostPassages(models.Model):
#     name = models.ForeignKey(Article, verbose_name=u"文章名",on_delete=models.CASCADE)
#     user = models.ForeignKey(UserProfile,verbose_name=u"用户笔名",on_delete=models.CASCADE)


    # name = models.CharField(max_length=50, verbose_name=u"文章名")
    # desc = models.CharField(max_length=300, verbose_name=u"文章介绍")
    # detail = models.TextField(verbose_name=u"文章详情")
    # art_len = models.CharField(choices=(("dp", u"短篇"), ("zp", u"中篇"), ("cp", u"长篇")), max_length=2,
    #                            verbose_name=u"文章长度")
    # read_times = models.IntegerField(default=0, verbose_name=u"预计阅读时长")
    # readers = models.IntegerField(default=0, verbose_name=u"阅读人数")
    # fav_nums = models.IntegerField(default=0, verbose_name=u"收藏人数")
    # category = models.CharField(max_length=20, verbose_name=u"文章类别", default=u"散文")
    # tag = models.CharField(default="", verbose_name=u"文章标签", max_length=10)
    # author = models.ForeignKey(Author, verbose_name=u"作者", null=True, blank=True, on_delete=models.CASCADE)
    # youneed_know = models.CharField(max_length=300, verbose_name=u"自述", default="")
    #
    # image = models.ImageField(upload_to="articles/%Y%m", verbose_name=u"封面图", max_length=100, default="")
    # click_nums = models.IntegerField(default=0, verbose_name=u"点击数")
    # add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")
    #
    # is_banner = models.BooleanField(default=False, verbose_name=u"是否轮播")