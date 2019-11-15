from django.db import models

from apps.users.models import BaseModel
# Create your models here.


class Product(BaseModel):
	"""产品模型"""
	product_name = models.CharField(max_length=64, verbose_name='产品名称')
	product_desc = models.CharField(max_length=200, verbose_name='产品描述')
	producter = models.CharField(max_length=200, verbose_name='产品负责人')

	class Meta:
		verbose_name_plural = verbose_name = '产品'

	def __str__(self):
		return self.product_name
