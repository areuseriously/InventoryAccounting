from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Department, Position, UserProfile


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class MyModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.name


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    department = MyModelChoiceField(queryset=Department.objects.all())
    position = MyModelChoiceField(queryset=Position.objects.all())

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'department', 'position', 'password1', 'password2')

    def clean(self):
        cleaned_data = super(UserRegistrationForm, self).clean()
        email = cleaned_data.get('email')
        department = cleaned_data.get('department')
        position = cleaned_data.get('position')

