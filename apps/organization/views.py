from django.shortcuts import render
from django.views.generic import View

from .models import ArticleOrg, Author
from operation.models import UsersFavorite

from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

from .forms import UserSearchForm
from django.http import HttpResponse
from articles.models import Article

from django.contrib.auth import authenticate, login,logout

import json

from django.db.models import Q
# Create your views here.


class OrgView(View):
    # 文章机构列表功能
    def get(self,request):
        # 组织机构
        all_orgs = ArticleOrg.objects.all()
        # 组织搜索
        search_keywords = request.GET.get('keywords', "")
        if search_keywords:
            all_orgs = all_orgs.filter(Q(name__icontains=search_keywords) | Q(desc__icontains=search_keywords))

        hot_orgs = all_orgs.order_by("-click_nums")[:3]
        # 类别筛选
        category = request.GET.get('ct',"")
        if category:
           all_orgs = all_orgs.filter(category=category)

        sort= request.GET.get('sort',"")
        if sort:
            if sort == "readers":
                all_orgs = all_orgs.order_by("-readers")
            elif sort == "articles":
                all_orgs = all_orgs.order_by("-article_nums")

        org_nums = all_orgs.count()

        try:
            page = request.GET.get('page',1)
        except:
            page = 1
            # 对组织机构分页
        p = Paginator(all_orgs, 4, request=request)
        orgs = p.page(page)

        return render(request,"org_list.html",{
            "all_orgs":orgs,
            "org_nums":org_nums,
            "category":category,
            "hot_orgs":hot_orgs,
            "sort":sort,
            "search_keywords":search_keywords,
        })


class AddUserSearchView(View):
    # 搜索
    def post(self,request):
        usersearch_form = UserSearchForm(request.POST)
        if usersearch_form.is_valid():
            user_search = usersearch_form.save(commit=True)
            #json语法是要里面是双引号，切记。且切记要导入json包！
            return HttpResponse('{"status":"success"}', content_type='application/json')
        else:
            return HttpResponse('{"status":"fail","msg":"添加出错"}', content_type='application/json')


class OrgHomeView(View):
    def get(self,request,org_id):
        article_org = ArticleOrg.objects.get(id=int(org_id))
        # 自动放进来.关于article_set,author_set是反向取出所有articles,authors
        all_articles = article_org.article_set.all()[:3]
        all_authors = article_org.author_set.all()[:2]

        current_page = "home"

        article_org.click_nums += 1
        article_org.save()

        has_fav = False
        if request.user.is_authenticated:
            if UsersFavorite.objects.filter(user=request.user, fav_id=article_org.id, fav_type=2):
                has_fav = True

        return render(request,'org-detail-homepage.html',{
            'all_articles':all_articles,
            'all_authors':all_authors,
            'article_org':article_org,
            'current_page':current_page,
            'has_fav':has_fav,
        })


class OrgArticleView(View):
    def get(self,request,org_id):
        article_org = ArticleOrg.objects.get(id=int(org_id))
        # 自动放进来.关于article_set,author_set是反向取出所有articles,authors
        all_articles = article_org.article_set.all()

        current_page = "article"

        has_fav = False
        if request.user.is_authenticated:
            if UsersFavorite.objects.filter(user=request.user, fav_id=article_org.id, fav_type=2):
                has_fav = True

        return render(request,'org-detail-article.html',{
            'all_articles':all_articles,
            'article_org':article_org,
            'current_page': current_page,
            'has_fav': has_fav,

        })


class OrgDescView(View):
    def get(self,request,org_id):
        article_org = ArticleOrg.objects.get(id=int(org_id))
        current_page = "desc"

        has_fav = False
        if request.user.is_authenticated:
            if UsersFavorite.objects.filter(user=request.user, fav_id=article_org.id, fav_type=2):
                has_fav = True

        return render(request,'org-detail-desc.html',{
            'article_org':article_org,
            'current_page': current_page,
            'has_fav': has_fav,

        })


class OrgAuthorView(View):
    def get(self,request,org_id):
        article_org = ArticleOrg.objects.get(id=int(org_id))
        current_page = "author"
        all_authors = article_org.author_set.all()

        has_fav = False
        if request.user.is_authenticated:
            if UsersFavorite.objects.filter(user=request.user, fav_id=article_org.id, fav_type=2):
                has_fav = True

        return render(request,'org-detail-authors.html',{
            'article_org':article_org,
            'current_page': current_page,
            'all_authors':all_authors,
            'has_fav': has_fav,

        })


class AddFavView(View):
    # 用户（取消）收藏def my_view(request):

    def post(self,request):
        # 须知id和类型
        fav_id = request.POST.get('fav_id', 0)
        fav_type = request.POST.get('fav_type', 0)
        # 查询是否存在,所以首先是用户登录
        # print(request.user)
        if not request.user.is_authenticated:
            return HttpResponse('{"status":"fail", "msg":"用户未登录"}', content_type='application/json')
        exist_records = UsersFavorite.objects.filter(user=request.user, fav_id=int(fav_id), fav_type=int(fav_type))
        if exist_records:
            # 记录已存在，则为取消收藏
            exist_records.delete()

            if int(fav_type)==1:
                article = Article.objects.get(id=int(fav_id))
                article.fav_nums -= 1
                if article.fav_nums < 0:
                    article.fav_nums = 0
                article.save()
            elif int(fav_type) == 2:
                article_org = ArticleOrg.objects.get(id=int(fav_id))
                article_org.fav_nums -= 1
                if article_org.fav_nums < 0:
                    article_org.fav_nums = 0
                article_org.save()
            elif int(fav_type) == 3:
                author = Author.objects.get(id=int(fav_id))
                author.fav_nums -= 1
                if author.fav_nums < 0:
                    author.fav_nums = 0
                author.save()

            return HttpResponse('{"status":"success","msg":"收藏"}', content_type='application/json')
        else:
            user_fav = UsersFavorite()
            if int(fav_id) > 0 and int(fav_type) > 0:
                user_fav.user = request.user
                user_fav.fav_id = int(fav_id)
                user_fav.fav_type = int(fav_type)
                user_fav.save()

                if int(fav_type) == 1:
                    article = Article.objects.get(id=int(fav_id))
                    article.fav_nums += 1
                    article.save()
                elif int(fav_type) == 2:
                    article_org = ArticleOrg.objects.get(id=int(fav_id))
                    article_org.fav_nums += 1
                    article_org.save()
                elif int(fav_type) == 3:
                    author = Author.objects.get(id=int(fav_id))
                    author.fav_nums += 1
                    author.save()

                return HttpResponse('{"status":"success", "msg":"已收藏"}', content_type='application/json')
            else:
                return HttpResponse('{"status":"fail", "msg":"收藏出错"}', content_type='application/json')


class AuthorListView(View):
    # 作者列表
    def get(self, request):
        all_authors = Author.objects.all()

        # 文章搜索
        search_keywords = request.GET.get('keywords', "")
        if search_keywords:
            all_authors = all_authors.filter(Q(name__icontains=search_keywords))

        sort = request.GET.get('sort', "")
        if sort:
            if sort == "hot":
                all_authors = all_authors.order_by("-click_nums")

        sorted_author = Author.objects.all().order_by("-click_nums")[:3]

        aut_nums = all_authors.count()

        try:
            page = request.GET.get('page',1)
        except:
            page = 1
            # 对组织机构分页
        p = Paginator(all_authors, 3, request=request)
        authors = p.page(page)

        return render(request, "authors-list.html", {
            "all_authors":authors,
            "sorted_author":sorted_author,
            "sort":sort,
            "aut_nums":aut_nums,
            "search_keywords":search_keywords,
        })


class AuthorDetailView(View):
    def get(self,request,author_id):
        author = Author.objects.get(id=int(author_id))
        author.click_nums += 1
        author.save()

        all_articles = Article.objects.filter(author=author)

        sorted_author = Author.objects.all().order_by("-click_nums")[:3]

        has_author_faved = False
        if UsersFavorite.objects.filter(user=request.user,fav_type=3,fav_id=author.id):
            has_author_faved = True

        has_org_faved = False
        if UsersFavorite.objects.filter(user=request.user,fav_type=2,fav_id=author.org.id):
            has_org_faved = True
        return render(request,"authors-detail.html",{
            "author":author,
            "all_articles":all_articles,
            "sorted_author": sorted_author,
            "has_author_faved":has_author_faved,
            "has_org_faved":has_org_faved,
        })