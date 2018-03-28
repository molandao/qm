from django.contrib import admin

# Register your models here.

from .models import UserSearch,ArticleComments,UsersFavorite,UserMessage,UserBrowsedArticles


class UserSearchAdmin(admin.ModelAdmin):
    list_display = ['name','article_name','add_time']
    search_fields = ['name','article_name']
    list_filter = ['name','article_name','add_time']


admin.site.register(UserSearch,UserSearchAdmin)


class ArticleCommentsAdmin(admin.ModelAdmin):
    list_display = ['user','article','comments','add_time']
    search_fields = ['user','article','comments']
    list_filter = ['user','article__name','comments','add_time']


admin.site.register(ArticleComments,ArticleCommentsAdmin)


class UsersFavoriteAdmin(admin.ModelAdmin):
    list_display = ['user','fav_id','fav_type','add_time']
    search_fields = ['user','fav_id','fav_type']
    list_filter = ['user','fav_id','fav_type','add_time']


admin.site.register(UsersFavorite,UsersFavoriteAdmin)


class UserMessageAdmin(admin.ModelAdmin):
    list_display = ['user','message','has_read','add_time']
    search_fields = ['user','message','has_read']
    list_filter = ['user','message','has_read','add_time']


admin.site.register(UserMessage,UserMessageAdmin)


class UserBrowsedArticlesAdmin(admin.ModelAdmin):
    list_display = ['user','article','add_time']
    search_fields = ['user','article']
    list_filter = ['user','article__name','add_time']


admin.site.register(UserBrowsedArticles,UserBrowsedArticlesAdmin)