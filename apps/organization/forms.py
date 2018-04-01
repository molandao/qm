from django import forms

from operation.models import UserSearch

#import re
# ModelForm
class UserSearchForm(forms.ModelForm):
    # my_field = forms.CharField()

    class Meta:
        model = UserSearch
        fields = ['name','article_name']
    # 验证手机合法性
    # def clean_mobile(self):
    #     mobile = cleaned_data['mobile']
    #     REGEX_MOBILE = "^1[358]\d{9}$|^147\d{8}$|^176\d{8}$"
    #     p = re.compile(REGEX_MOBILE)
    #     if p.match(mobile):
    #          return mobile
    #     else:
    #        raise forms.ValidationError("手机号码非法",code="mobile_invalid")
