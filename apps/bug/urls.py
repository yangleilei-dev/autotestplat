# !/usr/bin/python3
# -*- coding:utf-8 -*-
# @PROJECT_NAME: autotestplat
# @File : urls.py
# @AUTHOR: yangleilei
# @Email : yangleilei_carl@163.com
# @DATA_TIME: 2019-11-15 16:38
from django.urls import path

from apps.bug.views import BugView

app_name = 'bug'

urlpatterns = [
	path('bug/', BugView.as_view(), name='bug'),
]
