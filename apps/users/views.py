from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View


class LoginView(View):
	"""登陆"""
	@staticmethod
	def get(request):

		return render(request, 'users/login.html')

	@staticmethod
	def post(request):
		username = request.POST.get('form-username')
		password = request.POST.get('form-password')
		user = auth.authenticate(username=username, password=password)
		if user:
			auth.login(request, user)
			request.session['user'] = username
			return HttpResponseRedirect('/index.html/')
		else:
			return render(request, 'users/login.html')


class IndexView(View):
	"""首页"""
	@staticmethod
	def get(request):

		return render(request, 'index.html')


class LogoutView(View):
	"""退出登陆"""
	@staticmethod
	def get(request):
		auth.logout(request)
		return render(request, 'users/login.html')


