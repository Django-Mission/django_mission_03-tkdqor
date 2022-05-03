from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class UserBaseForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = '__all__'


# 회원가입을 위한 Form
class UserCreateForm(UserBaseForm):
    password2 = forms.CharField(widget=forms.PasswordInput())
    class Meta(UserBaseForm.Meta):
        fields = ['username', 'email', 'phone', 'password']


# 회원가입을 위해 UserCreationForm 변경
class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ['username', 'email']

