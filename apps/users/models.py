from django.db import models

# Create your models here.


class BaseModel(models.Model):

	create_time = models.DateTimeField(auto_now=True, verbose_name='创建时间')

	class Meta:
		abstract = True
