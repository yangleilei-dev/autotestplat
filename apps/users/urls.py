# !/usr/bin/python3
# -*- coding:utf-8 -*-
# @PROJECT_NAME: autotestplat
# @File : urls.py
# @AUTHOR: yangleilei
# @Email : yangleilei_carl@163.com
# @DATA_TIME: 2019-11-15 13:42
from django.urls import path

from apps.users.views import LoginView, LogoutView, IndexView

app_name = 'users'

urlpatterns = [
	path('login/', LoginView.as_view(), name='login'),
	path('index.html/', IndexView.as_view(), name='index'),
	path('logout/', LogoutView.as_view(), name='logout'),
]
