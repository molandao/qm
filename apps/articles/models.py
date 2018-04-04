from datetime import datetime

from django.db import models

from organization.models import ArticleOrg,Author

# Create your models here.


class Article(models.Model):
    article_org = models.ForeignKey(ArticleOrg, verbose_name=u"组织机构",null=True,blank=True, on_delete=models.CASCADE)

    name = models.CharField(max_length=50, verbose_name=u"文章名")
    desc = models.CharField(max_length=300, verbose_name=u"文章介绍")
    detail = models.TextField(verbose_name=u"文章详情")
    art_len = models.CharField(choices=(("dp",u"短篇"),("zp",u"中篇"),("cp",u"长篇")),max_length=2,verbose_name=u"文章长度")
    read_times = models.IntegerField(default=0,verbose_name=u"预计阅读时长")
    readers = models.IntegerField(default=0,verbose_name=u"阅读人数")
    fav_nums = models.IntegerField(default=0, verbose_name=u"收藏人数")
    category = models.CharField(max_length=20, verbose_name=u"文章类别", default=u"散文")
    tag = models.CharField(default="", verbose_name=u"文章标签", max_length=10)
    author = models.ForeignKey(Author, verbose_name=u"作者",null=True,blank=True, on_delete=models.CASCADE)
    youneed_know = models.CharField(max_length=300, verbose_name=u"自述", default="")

    image = models.ImageField(upload_to="articles/%Y%m",verbose_name=u"封面图",max_length=100,default="")
    click_nums = models.IntegerField(default=0,verbose_name=u"点击数")
    add_time = models.DateTimeField(default=datetime.now,verbose_name=u"添加时间")

    class Meta:
        verbose_name=u"文章"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name

    def get_zj_nums(self):
        # 获取课程章数
        return self.lesson_set.all().count()

    def get_read_users(self):
        return self.userbrowsedarticles_set.all()[:5]

    # 获取文章所有章节
    def get_article_lesson(self):
        return self.lesson_set.all()


# 文章和章节一对多或一对一
class Lesson(models.Model):
    article = models.ForeignKey(Article,verbose_name=u"文章",on_delete=models.CASCADE)
    name = models.CharField(max_length=100,verbose_name=u"章节名")
    add_time = models.DateTimeField(default=datetime.now,verbose_name=u"添加时间")
    class Meta:
        verbose_name = u"章节"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def get_lesson_content(self):
        return self.content_set.all()


class Content(models.Model):
    lesson = models.ForeignKey(Lesson,verbose_name=u"章节",on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name=u"文章标题")
    art_content = models.TextField(null=True, verbose_name=u"文章内容")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")
    class Meta:
        verbose_name = u"内容"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class MoreArticles(models.Model):
    article = models.ForeignKey(Article,verbose_name=u"文章",on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name=u"名称")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")
    # download = models.FileField(upload_to="course/resource/%Y%m",verbose_name=u"资源文件",max_length=100)

    class Meta:
        verbose_name = u"更多文章"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name