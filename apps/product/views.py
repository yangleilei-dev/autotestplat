from django.shortcuts import render
from django.views.generic.base import View

from apps.product.models import Product
# Create your views here.


class ProductView(View):

	@staticmethod
	def get(request):
		username = request.session.get('user', '')
		product_list = Product.objects.all()
		context = {
			'user': username,
			'product_list': product_list,
		}
		return render(request, 'product/product.html', context=context)
