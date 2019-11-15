from django.shortcuts import render
from django.views.generic.base import View

from apps.bug.models import Bug
# Create your views here.


class BugView(View):

	@staticmethod
	def get(request):
		username = request.session.get('user', '')
		bug_list = Bug.objects.all()
		context = {
			'user': username,
			'bug_list': bug_list,
		}
		return render(request, 'bug/bug.html', context=context)
