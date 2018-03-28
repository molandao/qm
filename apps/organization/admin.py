from django.contrib import admin

# Register your models here.

from .models import ArticleOrg,Author


class ArticleOrgAdmin(admin.ModelAdmin):
    list_display = ['name','desc','click_nums','fav_nums','add_time']
    search_fields = ['name','desc','click_nums','fav_nums']
    list_filter = ['name','desc','click_nums','fav_nums','add_time']


admin.site.register(ArticleOrg,ArticleOrgAdmin)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['org','name','mu_years','writing_style','click_nums','fav_nums','add_time']
    search_fields = ['org','name','mu_years','writing_style','click_nums','fav_nums']
    list_filter = ['org__name','name','mu_years','writing_style','click_nums','fav_nums','add_time']

admin.site.register(Author, AuthorAdmin)
