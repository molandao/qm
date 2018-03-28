from django.contrib import admin

# Register your models here.
from .models import Article,Lesson,Content,MoreArticles


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['name','desc','detail','art_len','read_times','readers','fav_nums','image','click_nums','add_time']
    search_fields = ['name','desc','detail','art_len','readers','fav_nums','image','click_nums']
    list_filter = ['name','desc','detail','art_len','read_times','readers','fav_nums','image','click_nums','add_time']


admin.site.register(Article,ArticleAdmin)


class LessonAdmin(admin.ModelAdmin):
    list_display = ['article','name','add_time']
    search_fields = ['article','name']
    list_filter = ['article__name','name','add_time']
    #__name外键的NAME字段


admin.site.register(Lesson,LessonAdmin)


class ContentAdmin(admin.ModelAdmin):
    list_display = ['lesson','name','add_time']
    search_fields = ['lesson','name']
    list_filter = ['lesson__name','name','add_time']


admin.site.register(Content,ContentAdmin)


class MoreArticlesAdmin(admin.ModelAdmin):
    list_display = ['article','name','add_time']
    search_fields = ['article','name']
    list_filter = ['article__name','name','add_time']


admin.site.register(MoreArticles,MoreArticlesAdmin)