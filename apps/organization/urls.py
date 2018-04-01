from django.urls import path

from .views import OrgView, AddUserSearchView, OrgHomeView, OrgArticleView, OrgDescView, OrgAuthorView, AddFavView


urlpatterns = [
    # 文章组织首页
    path('list/', OrgView.as_view(), name='org_list'),

    path('add_search/', AddUserSearchView.as_view(), name='add_search'),

    path('home/<org_id>/',OrgHomeView.as_view(),name='org_home'),

    path('article/<org_id>/', OrgArticleView.as_view(), name='org_article'),

    path('desc/<org_id>/', OrgDescView.as_view(), name='org_desc'),

    path('author/<org_id>/', OrgAuthorView.as_view(), name='org_author'),

    # 机构收藏
    path('add_fav/', AddFavView.as_view(), name='add_fav'),


]