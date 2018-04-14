from django import forms

from operation.models import UserSearch

# ModelForm
class UserSearchForm(forms.ModelForm):

    class Meta:
        model = UserSearch
        fields = ['name','article_name']
