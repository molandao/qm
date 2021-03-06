#一般用来存储form的定义
from django import forms
from captcha.fields import CaptchaField

from .models import UserProfile
from articles.models import Article
from organization.models import Author


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=5)
    # username 和password 一定要和index里的input的name一直，不然不会做判断
    # 减少数据库负担
    #对注册表进行认证


class RegisterForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, min_length=5)
    captcha = CaptchaField(error_messages={"invalid":u"验证码错误"})


class ForgetForm(forms.Form):
    email = forms.EmailField(required=True)
    captcha = CaptchaField(error_messages={"invalid": u"验证码错误"})


class ModifyPwdrForm(forms.Form):
    password1 = forms.CharField(required=True, min_length=5)
    password2 = forms.CharField(required=True, min_length=5)


class UploadImageForm(forms.ModelForm):
    class Meta:
        # ModelForm user定义了个字段叫做image
        model = UserProfile
        fields = ['image']


class ArticleImageForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['image']


class UserInfoForm(forms.ModelForm):
    class Meta:
        # ModelForm user定义了个字段叫做image
        model = UserProfile
        fields = ['nick_name','gender','birday','mobile']


class UserPostPassage(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['name','desc','detail','art_len','read_times','category','tag','author','youneed_know','image']
