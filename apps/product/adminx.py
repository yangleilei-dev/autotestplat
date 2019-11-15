# !/usr/bin/python3
# -*- coding:utf-8 -*-
# @PROJECT_NAME: autotestplat
# @File : adminx.py
# @AUTHOR: yangleilei
# @Email : yangleilei_carl@163.com
# @DATA_TIME: 2019-11-15 15:50

import xadmin
from apps.product.models import Product


class ProductAdmin:

	list_display = ['product_name', 'Product_desc', 'producter', 'create_time']
	search_fields = ['product_name', 'producter']
	list_filter = ['producter', 'create_time']


xadmin.site.register(Product, ProductAdmin)
