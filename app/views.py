from django.shortcuts import render
from app import models
from django import forms
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError

# Create your views here.


class RegisterModelForm(forms.ModelForm):
    class Meta:
        model = models.UserInfo
        fields = ['username', 'email', 'phone', 'password']


def register(request):
    form = RegisterModelForm()
    return render(request, 'register.html', {'form': form})
