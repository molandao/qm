from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.backends import ModelBackend
from .models import UserProfile,EmailVerifyRecord
from django.db.models import Q
from django.views.generic.base import View
from .forms import LoginForm, RegisterForm, ForgetForm,ModifyPwdrForm, UploadImageForm, UserInfoForm, ArticleImageForm
from django.contrib.auth.hashers import make_password

from utils.email_send import send_register_email

from utils.mixin_utils import LoginRequiredMixin

from django.http import HttpResponse, HttpResponseRedirect

import json

from operation.models import UserBrowsedArticles, UsersFavorite,UserMessage

from organization.models import ArticleOrg, Author

from articles.models import Article, Content, Lesson

from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

from .models import Banner

from django.urls import reverse


class CustomBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username)|Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None
#
# Create your views here.


def home(request):
    return render(request,'index.html')
# def user_login(request):
#     # GET POST_more safety
#     if request.method == "POST":
#         user_name = request.POST.get("username","")
#         pass_word = request.POST.get("password","")
#         user = authenticate(username=user_name , password=pass_word)
#         if user is not None:
#             login(request,user)
#             return render(request,"index.html")
#         else:
#             return render(request,"login.html",{"msg":"用户名或密码错误"})
#     elif request.method == "GET":
#         return render(request,"login.html",{})


class LoginView(View):
    def get(self,request):
        banner_articles = Article.objects.filter(is_banner=True)[:3]

        return render(request, "login.html", {
            "banner_articles":banner_articles
        })
    def post(self,request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            # pass

            user_name = request.POST.get("username", "")
            pass_word = request.POST.get("password", "")
            user = authenticate(username=user_name, password=pass_word)
            if user is not None:
                if user.is_active:

                    login(request, user)

                    return HttpResponseRedirect(reverse("index"))
                else:
                    return render(request, "login.html", {"msg": "用户未激活"})
            else:
                return render(request,"login.html",{"msg":"用户名或密码错误"})
        else:
            return render(request, "login.html", {"login_form":login_form})

        #然后是form


class RegisterView(View):
    def get(self,request):
        register_form = RegisterForm()
        banner_articles = Article.objects.filter(is_banner=True)[:3]

        return render(request, "register.html", {
            'register_form':register_form,
            "banner_articles":banner_articles,
        })
    def post(self,request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_name = request.POST.get("email", "")
            if UserProfile.objects.filter(email=user_name):
                return render(request, "register.html", {"register_form":register_form, "msg": "用户已存在"})
            pass_word = request.POST.get("password", "")
            user_profile = UserProfile()
            user_profile.username = user_name
            #panduan yonghushifoucunzai

            user_profile.email = user_name
            user_profile.is_active = False
            #加密密码
            user_profile.password = make_password(pass_word)
            user_profile.save()

            # 写入欢迎注册的消息
            user_message = UserMessage()
            user_message.user = user_profile.id
            user_message.message = "欢迎注册青木"
            user_message.save()

            send_register_email(user_name,"register")
            return render(request, "login.html")

        else:
            return render(request, "register.html", {"register_form": register_form})


class ActiveUserView(View):
    def get(self,request,active_code):
        all_records = EmailVerifyRecord.objects.filter(code=active_code)
        if all_records:
            for record in all_records:
                email = record.email
                user = UserProfile.objects.get(email=email)
                user.is_active=True
                user.save()
        else:
            return render(request, "active_fail.html")

        return render(request,"login.html")


class ForgetPwdView(View):
    def get(self,request):
        forget_form = ForgetForm()
        banner_articles = Article.objects.filter(is_banner=True)[:3]

        return render(request,"forgetpwd.html",{
            "forget_form":forget_form,
            "banner_articles":banner_articles
        })
    def post(self,request):
        forget_form = ForgetForm(request.POST)
        if forget_form.is_valid():
            email = request.POST.get("email","")
            send_register_email(email, "forget")
            return render(request, "send_success.html")
        else:
            return render(request, "forgetpwd.html", {
                "forget_form": forget_form
            })


class ResetView(View):
    def get(self,request,active_code):
        all_records = EmailVerifyRecord.objects.filter(code=active_code)
        if all_records:
            for record in all_records:
                email = record.email
                return render(request, "password_reset.html",{"email":email})
        else:
            return render(request, "active_fail.html")

        return render(request,"login.html")


class ModifyPwdView(View):
    def post(self,request):
        modify_form = ModifyPwdrForm(request.POST)
        if modify_form.is_valid():
            pwd1 = request.POST.get("password1","")
            pwd2 = request.POST.get("password2","")
            email = request.POST.get("email","")

            if pwd1 != pwd2:
                return render(request, "password_reset.html",{"email":email,"msg":"密码不一致"})
            user = UserProfile.objects.get(email=email)
            user.password = make_password(pwd2)
            user.save()

            return render(request, "login.html")
        else:
            email = request.POST.get("email","")

            return render(request, "password_reset.html", {"email": email, "modify_form":modify_form})


class UserInfoView(LoginRequiredMixin, View):
    # 用户个人信息 需要登录
    def get(self,request):
        current_page = "info"
        return render(request, 'usercenter-info.html',{
            "current_page":current_page,
        })

    def post(self, request):
        # ModelForm
        user_info_form = UserInfoForm(request.POST, instance=request.user)
        # 修改,所以需要加入instance
        if user_info_form.is_valid():
            user_info_form.save()
            return HttpResponse('{"status":"success"}', content_type='application/json')

        else:
            return HttpResponse(json.dumps(user_info_form.errors), content_type='application/json')



class UploadImvageView(LoginRequiredMixin,View):
    # 用户头像修改
    def post(self, request):
        # 实例化，传进来的是request.POST  文件放在request.files
        image_form = UploadImageForm(request.POST, request.FILES, instance=request.user)
        if image_form.is_valid():
            image = image_form.cleaned_data['image']
            # request.user.image = image
            # request.user.save()
            image_form.save()
            return HttpResponse('{"status":"success"}', content_type='application/json')
        else:
            return HttpResponse('{"status":"fail"}', content_type='application/json')


class UpdatePwdView(View):

    # 个人中心修改用户密码
    def post(self, request):
        modify_form = ModifyPwdrForm(request.POST)
        if modify_form.is_valid():
            pwd1 = request.POST.get("password1", "")
            pwd2 = request.POST.get("password2", "")

            if pwd1 != pwd2:
                return HttpResponse('{"status":"fail","msg":"密码不一致"}', content_type='application/json')
            user = request.user
            user.password = make_password(pwd2)
            user.save()

            return HttpResponse('{"status":"success"}', content_type='application/json')
        else:
            return HttpResponse(json.dumps(modify_form.errors), content_type='application/json')


class SendEmailCodeView(LoginRequiredMixin, View):
    def get(self, request):
        email = request.GET.get('email','')
        # 判断邮箱存在，且没被注册过
        if UserProfile.objects.filter(email=email):
            return HttpResponse('{"email":"邮箱已存在}', content_type='application/json')

        send_register_email(email,"update_email")

        return HttpResponse('{"status":"success"}', content_type='application/json')


class UpdateEmailView(LoginRequiredMixin, View):
    def post(self, request):
        email = request.POST.get('email','')
        code = request.POST.get('code','')

        # 验证
        existed_records = EmailVerifyRecord.objects.filter(email=email, code=code, send_type='update_email')
        if existed_records:
            user = request.user
            user.email = email
            user.save()
            return HttpResponse('{"status":"success"}', content_type='application/json')
        else:
            return HttpResponse('{"email":"验证码错误}', content_type='application/json')


class BrowsedArticlesView(LoginRequiredMixin, View):
    # 阅读过的文章
    def get(self, request):
        user_browsedarticles = UserBrowsedArticles.objects.filter(user=request.user)

        current_page = "articles_read"
        return render(request, 'usercenter-read.html',{
            "user_browsedarticles":user_browsedarticles,
            "current_page":current_page,
        })


class MyFavOrgView(LoginRequiredMixin, View):
    # 收藏的组织
    def get(self, request):
        org_list = []
        fav_orgs = UsersFavorite.objects.filter(user=request.user, fav_type=2)
        for fav_org in fav_orgs:
            org_id = fav_org.fav_id
            org = ArticleOrg.objects.get(id=org_id)
            org_list.append(org)

        current_page = "myfav"
        return render(request, 'usercenter-fav-org.html',{
            "org_list":org_list,

            "current_page":current_page,

        })


class MyFavAuthorView(LoginRequiredMixin, View):
    # 收藏的组织
    def get(self, request):
        author_list = []
        fav_authors = UsersFavorite.objects.filter(user=request.user, fav_type=3)
        for fav_author in fav_authors:
            author_id = fav_author.fav_id
            author = Author.objects.get(id=author_id)
            author_list.append(author)

        current_page = "myfav"

        return render(request, 'usercenter-fav-author.html',{
            "author_list":author_list,

            "current_page": current_page,

        })


class MyFavArticleView(LoginRequiredMixin, View):
    # 收藏的组织
    def get(self, request):
        article_list = []
        fav_articles = UsersFavorite.objects.filter(user=request.user, fav_type=1)
        for fav_article in fav_articles:
            article_id = fav_article.fav_id
            article = Article.objects.get(id=article_id)
            article_list.append(article)

        current_page = "myfav"

        return render(request, 'usercenter-fav-article.html',{
            "article_list":article_list,

            "current_page": current_page,

        })


class MyMessageView(LoginRequiredMixin,View):
    def get(self, request):

        all_messages = UserMessage.objects.filter(user=request.user.id)

        # 用户进入个人消息后清空未读消息
        all_unread_messages = UserMessage.objects.filter(user=request.user.id, has_read=False)
        for unread_message in all_unread_messages:
            unread_message.has_read = True
            unread_message.save()

        try:
            page = request.GET.get('page',1)
        except:
            page = 1
            # 对组织机构分页
        p = Paginator(all_messages, 4, request=request)
        messages = p.page(page)

        current_page = "mymessage"
        return render(request, 'usercenter-message.html', {
            "messages":messages,
            "current_page":current_page,
        })


class LogoutView(View):
    # 用户登出
    def get(self, request):
        logout(request)
        # 重定向
        return HttpResponseRedirect(reverse("index"))


class IndexView(View):
    # 首页
    def get(self, request):
        all_banners = Banner.objects.all().order_by('index')
        articles = Article.objects.filter(is_banner=False)[:6]
        banner_articles = Article.objects.filter(is_banner=True)[:3]
        article_orgs = ArticleOrg.objects.all()[:10]

        return render(request, 'index.html', {
            "all_banners":all_banners,
            "articles":articles,
            "banner_articles":banner_articles,
            "article_orgs":article_orgs,
        })


class PostPassagesView(View):
    def get(self,request):
        current_page = "postpassage"
        all_articles = Article.objects.all()
        all_orgs = ArticleOrg.objects.all()
        all_authors = Author.objects.all()
        return render(request, 'usercenter_tg.html',{
            "current_page":current_page,
            "all_articles":all_articles,
            "all_orgs":all_orgs,
            "all_authors":all_authors,
        })


class AddPassagesView(View):
    def post(self, request):
        article_name = request.POST.get("article_name","")
        desc = request.POST.get("desc","")
        detail = request.POST.get("detail","")
        # art_len = request.POST.get("art_len","")
        read_times = request.POST.get("read_times","")
        category = request.POST.get("category","")
        tag = request.POST.get("tag","")
        author = request.POST.get("author","")
        youneed_know = request.POST.get("youneed_know","")
        img = request.FILES.get('image')
        content = request.POST.get("content","")
        lesson = request.POST.get("lesson","")
        article_org = request.POST.get("article_org",10)

        if content :
            post_article = Article()
            post_article.desc = desc
            post_article.detail = detail
            # post_article.art_len = art_len
            post_article.name = article_name
            post_article.read_times = read_times
            post_article.category = category
            post_article.tag = tag
            author = Author.objects.get(id=int(author))
            post_article.author = author
            post_article.youneed_know = youneed_know
            article_org = ArticleOrg.objects.get(id=article_org)
            post_article.article_org = article_org
            # post_article.image = Author.objects.get(image=image)
            # image_form = ArticleImageForm(request.POST, request.FILES, instance=request.user)
            # if image_form.is_valid():
            #     image = image_form.cleaned_data['image']
            # image_form.save()
            post_article.save()
            post_content = Content()
            post_content.name = article_name
            post_content.art_content = content
            lesson = Lesson.objects.get(id=int(lesson))
            post_content.lesson = lesson
            post_content.save()
            return HttpResponse('{"status":"success","msg":"提交成功"}', content_type='application/json')
        else:
            return HttpResponse('{"status":"fail","msg":"提交失败"}',content_type='application/json')