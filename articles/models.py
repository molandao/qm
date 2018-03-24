from datetime import datetime

from django.db import models

# Create your models here.


class Article(models.Model):
    name = models.CharField(max_length=50, verbose_name=u"文章名")
    desc = models.CharField(max_length=300, verbose_name=u"文章介绍")
    detail = models.TextField(verbose_name=u"文章详情")
    art_len = models.CharField(choices=(("dp",u"短篇"),("zp",u"中篇"),("cp",u"长篇")),max_length=2)
    read_times = models.IntegerField(default=0,verbose_name=u"预计阅读时长")
    readers = models.IntegerField(default=0,verbose_name=u"阅读人数")
    fav_nums = models.IntegerField(default=0, verbose_name=u"收藏人数")

    # image = models.ImageField(upliad_to="articles/%Y%m",verbose_name=u”封面图",max_length=100)
    click_nums = models.IntegerField(default=0,verbose_name=u"点击数")
    add_time = models.DateTimeField(default=datetime.now,verbose_name=u"添加时间")

    class Meta:
        verbose_name=u"文章"
        verbose_name_plural = verbose_name


# 文章和章节一对多或一对一
class Lesson(models.Model):
    article = models.ForeignKey(Article,verbose_name=u"文章")
    name = models.CharField(max_length=100,verbose_name=u"章节名")
    add_time = models.DateTimeField(default=datetime.now,verbose_name=u"添加时间")
    class Meta:
        verbose_name = u"章节"
        verbose_name_plural = verbose_name


class Content(models.Model):
    lesson = models.ForeignKey(Lesson,verbose_name=u"章节")
    name = models.CharField(max_length=100, verbose_name=u"视频名称")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")
    class Meta:
        verbose_name = u"内容"
        verbose_name_plural = verbose_name


class MoreArticles(models.Model):
    article = models.ForeignKey(Article,verbose_name=u"文章")
    name = models.CharField(max_length=100, verbose_name=u"名称")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")
    # download = models.FileField(upload_to="course/resource/%Y%m",verbose_name=u"资源文件",max_length=100)

    class Meta:
        verbose_name = u"更多文章"
        verbose_name_plural = verbose_name