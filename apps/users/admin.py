from django.contrib import admin

# Register your models here.
from .models import UserProfile, EmailVerifyRecord, Banner

class UserProfileAdmin(admin.ModelAdmin):
    pass


admin.site.register(UserProfile,UserProfileAdmin)


class EmailVerifyRecordAdmin(admin.ModelAdmin):
    list_display = ['code','email','send_type','send_time']
    search_fields = ['code','email','send_type']
    list_filter = ['code','email','send_type','send_time']


admin.site.register(EmailVerifyRecord,EmailVerifyRecordAdmin)


class BannerAdmin(admin.ModelAdmin):
    list_display = ['title','image','url','index','add_time']
    search_fields = ['title','image','url','index']
    list_filter = ['title','image','url','index','add_time']


admin.site.register(Banner, BannerAdmin)


# class MyAdminSite(admin.AdminSite):
#     site_header = '青木管理系统'  # 此处设置页面显示标题
#     site_title = '青木运维'  # 此处设置页面头部标题
#
# # admin_site = MyAdminSite(name='management') # 使用admin_site实例注册需要管理的模型类


admin.site.site_header = "青木后台管理系统"
admin.site.site_title = '青木后台'
