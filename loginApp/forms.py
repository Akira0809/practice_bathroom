from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.conf import settings

User = get_user_model()

#ユーザー登録
class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=True)
        
        # 確認するまでログイン不可にする
        user.is_active = True
        
        user.save()
        
        return user

#データ入力
class ProfileForm(forms.Form):
    username = forms.CharField(max_length=100)
    name = forms.CharField(max_length = 100)
    birthday = forms.DateField(widget=forms.SelectDateWidget())