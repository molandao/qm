from django.urls import path
from .views import UserInfoView, UploadImvageView, UpdatePwdView, SendEmailCodeView, UpdateEmailView, BrowsedArticlesView
from .views import MyFavOrgView, MyFavAuthorView, MyFavArticleView, MyMessageView,PostPassagesView, AddPassagesView

app_name = '[users]'
urlpatterns = [

    # 用户信息
    path('info/', UserInfoView.as_view(), name='user_info'),

    # 用户头像上传
    path('image/upload/', UploadImvageView.as_view(), name='image_upload'),

    # 用户修改密码
    path('update/pwd/', UpdatePwdView.as_view(), name='update_pwd'),

    # 发送邮箱验证码
    path('sendemail_code/', SendEmailCodeView.as_view(), name='sendemail_code'),

    # 用户修改邮箱
    path('update_email/', UpdateEmailView.as_view(), name='update_email'),

    # 读过的文章
    path('articles_read/', BrowsedArticlesView.as_view(), name='articles_read'),

    # 收藏的组织
    path('myfav/org/', MyFavOrgView.as_view(), name='myfav_org'),

    # 收藏的作者
    path('myfav/author/', MyFavAuthorView.as_view(), name='myfav_author'),

    # 收藏的文章
    path('myfav/article/', MyFavArticleView.as_view(), name='myfav_article'),

    # 我的消息
    path('mymessage/', MyMessageView.as_view(), name='mymessage'),

    # 投稿
    path('postpassages/',PostPassagesView.as_view(),name='postpassage'),

    # 投稿
    path('postpassages/post',AddPassagesView.as_view(),name='postpassage_post')
]