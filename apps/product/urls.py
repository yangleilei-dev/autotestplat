# !/usr/bin/python3
# -*- coding:utf-8 -*-
# @PROJECT_NAME: autotestplat
# @File : urls.py
# @AUTHOR: yangleilei
# @Email : yangleilei_carl@163.com
# @DATA_TIME: 2019-11-15 13:42
from django.urls import path

from apps.product.views import ProductView

app_name = 'product'

urlpatterns = [
	path('product/', ProductView.as_view(), name='product'),
]
