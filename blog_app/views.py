from django.shortcuts import render, get_object_or_404

# Create your views here.

from django.http import HttpResponse, HttpResponseNotFound, Http404
import datetime
# from polls.model import Poll
from django.utils import timezone
from .models import Post


def post_list(request):
	# return render(request, 'blog_app/post_list.html', {})
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
	return render(request, 'blog_app/post_list.html', {'posts':posts})

def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'blog_app/post_detail.html', {'post':post})	

def current_datetime(request):
	now = datetime.datetime.now()
	html = "<html><body> It is now %s. </body></html>" % now
	return HttpResponse(html)

# def detail(request, poll_id):
# 	try:
# 		p = Poll.object.get(pk=poll_id)
# 	except Poll.DoesNotExist:
# 		raise Http404("Poll does not exist")

# 	return render(request, 'polls/detail.html', {'poll':p})

	