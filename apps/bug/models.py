from django.db import models

from apps.product.models import Product
from apps.users.models import BaseModel
# Create your models here.


class Bug(BaseModel):

	BUG_STATUS = (
		('jh', '激活'),
		('jj', '已解决'),
		('gb', '已关闭'),
	)
	BUG_LEVEL = (
		('1', '1'),
		('2', '2'),
		('3', '3'),
	)

	product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
	bug_name = models.CharField(max_length=200, verbose_name='Bug名称')
	bug_detail = models.CharField(max_length=2000, verbose_name='Bug详情')
	bug_status = models.CharField(max_length=5, choices=BUG_STATUS, default='jh', null=True)
	bug_level = models.CharField(max_length=5, choices=BUG_LEVEL, default='3', verbose_name='严重程度', null=True)
	bug_creater = models.CharField(max_length=200, verbose_name='创建人')
	bug_assign = models.CharField(max_length=200, verbose_name='分配')

	class Meta:
		verbose_name_plural = verbose_name = 'Bug'

	def __str__(self):
		return self.bug_name

