from django.shortcuts import render
from django.views.generic.base import View

from .models import Article, Content
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

from operation.models import UsersFavorite, ArticleComments, UserBrowsedArticles

from django.http import HttpResponse

from utils.mixin_utils import LoginRequiredMixin

from django.db.models import Q
# mixin 基本代表一个基础的view

# Create your views here.


class ArticleListView(View):
    def get(self,request):
        all_articles = Article.objects.all().order_by("-add_time")

        # 文章搜索
        search_keywords = request.GET.get('keywords',"")
        if search_keywords:
            all_articles = all_articles.filter(Q(name__icontains=search_keywords)|Q(desc__icontains=search_keywords)|Q(detail__icontains=search_keywords))

        # 排序，最多阅读数，最多点击数
        sort = request.GET.get('sort', "")
        if sort:
            if sort == "readers":
                all_articles = all_articles.order_by("-readers")
            elif sort == "hot":
                all_articles = all_articles.order_by("-click_nums")

        try:
            page = request.GET.get('page',1)
        except:
            page = 1
            # 对组织机构分页
        p = Paginator(all_articles, 9, request=request)
        articles = p.page(page)

        hot_articles = Article.objects.all().order_by("-click_nums")[:3]

        return render(request,'article-list.html',{
            "all_articles":articles,
            "sort":sort,
            "hot_articles":hot_articles,

        })


class ArticleDetailView(View):
    def get(self,request,article_id):
        article = Article.objects.all().get(id=int(article_id))

        article.click_nums += 1
        article.save()

        tag = article.tag
        if tag:
            relate_articles = Article.objects.filter(tag=tag)[:1]
        else:
            relate_articles = []

        has_fav_article = False
        has_fav_org = False

        if request.user.is_authenticated:
            if UsersFavorite.objects.filter(user=request.user, fav_id=article.id, fav_type=1):
                has_fav_article = True
            if UsersFavorite.objects.filter(user=request.user, fav_id=article.article_org.id, fav_type=2):
                has_fav_org = True

        return render(request,"article-detail.html",{
            "article":article,
            "relate_articles":relate_articles,
            "has_fav_article":has_fav_article,
            "has_fav_org":has_fav_org,

        })


class ArticleInfoView(LoginRequiredMixin, View):
    def get(self, request, article_id):
        # 文章章节信息
        article = Article.objects.get(id=int(article_id))
        article.readers += 1
        article.save()

        # 把user和article连接起来，可以查询用户是否已经关联了文章
        user_arts = UserBrowsedArticles.objects.filter(user=request.user, article=article)
        if not user_arts:
            user_arts = UserBrowsedArticles(user=request.user, article=article)
            user_arts.save()

        user_articles = UserBrowsedArticles.objects.filter(article=article)
        user_ids = [user_article.user.id for user_article in user_articles]
        all_user_articles = UserBrowsedArticles.objects.filter(user_id__in=user_ids)
        # 取出所有文章id
        article_ids = [user_article.article.id for user_article in all_user_articles]
        relate_articles = Article.objects.filter(id__in=article_ids).order_by("-click_nums")[:2]


        return render(request ,"article-chapter.html",{
            "article":article,
            "relate_articles":relate_articles,

        })


# 继承顺序是从左到右的
class ArticleCommentsView(LoginRequiredMixin, View):
    def get(self, request, article_id):
        article = Article.objects.get(id=int(article_id))

        all_comments = ArticleComments.objects.all()
        return render(request, "article-comment.html", {
            "article": article,
            "all_comments":all_comments,

        })


class AddCommentsView(View):
    # 用户添加文章评论
    def post(self,request):
        if not request.user.is_authenticated:
            return HttpResponse('{"status":"fail", "msg":"用户未登录"}', content_type='application/json')

        article_id = request.POST.get("article_id", 0)
        comments = request.POST.get("comments",0)

        if int(article_id) > 0 and comments:
            article_comments = ArticleComments()
            article = Article.objects.get(id=int(article_id))
            # get是只取出一条数据
            article_comments.article = article
            article_comments.comments = comments
            article_comments.user = request.user
            article_comments.save()
            return HttpResponse('{"status":"success", "msg":"添加成功"}', content_type='application/json')
        else:
            return HttpResponse('{"status":"fail", "msg":"添加失败"}', content_type='application/json')


class ShowContView(View):
    def get(self, request, content_id):
        # 文章章节信息
        content = Content.objects.get(id=int(content_id))
        article = content.lesson.article
        article.readers += 1
        article.save()
        # 把user和article连接起来，可以查询用户是否已经关联了文章
        user_arts = UserBrowsedArticles.objects.filter(user=request.user, article=article)
        if not user_arts:
            user_arts = UserBrowsedArticles(user=request.user, article=article)
            user_arts.save()

        user_articles = UserBrowsedArticles.objects.filter(article=article)
        user_ids = [user_article.user.id for user_article in user_articles]
        all_user_articles = UserBrowsedArticles.objects.filter(user_id__in=user_ids)
        # 取出所有文章id
        article_ids = [user_article.article.id for user_article in all_user_articles]
        relate_articles = Article.objects.filter(id__in=article_ids).order_by("-click_nums")[1:3]

        return render(request ,"article-content.html",{
            "article":article,
            "relate_articles":relate_articles,
            "content":content,

        })
