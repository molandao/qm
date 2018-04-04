from django.urls import path

from .views import ArticleListView,ArticleDetailView, ArticleInfoView,ArticleCommentsView, AddCommentsView, ShowContView

app_name='[articles]'
urlpatterns = [
    # 文章组织首页
    path('list/', ArticleListView.as_view(), name='article_list'),

    path('detail/<article_id>', ArticleDetailView.as_view(), name='article_detail'),

    path('info/<article_id>', ArticleInfoView.as_view(), name='article_info'),

    path('comments/<article_id>', ArticleCommentsView.as_view(), name='article_comments'),

    path('add_comments',AddCommentsView.as_view(), name='add_comments'),

    path('content/<content_id>',ShowContView.as_view(),name='show_content'),

]