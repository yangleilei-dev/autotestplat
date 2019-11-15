# !/usr/bin/python3
# -*- coding:utf-8 -*-
# @PROJECT_NAME: autotestplat
# @File : adminx.py
# @AUTHOR: yangleilei
# @Email : yangleilei_carl@163.com
# @DATA_TIME: 2019-11-15 16:39

import xadmin
from apps.bug.models import Bug


class BugAdmin:

	list_display = ['bug_name', 'bug_detail', 'bug_status', 'bug_level', 'bug_creater', 'bug_assign', 'create_time']
	search_fields = ['bug_name', 'bug_creater']
	list_filter = ['bug_status', 'bug_level', 'bug_assign']


xadmin.site.register(Bug, BugAdmin)
