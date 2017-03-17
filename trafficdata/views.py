from django.shortcuts import render

# Create your views here.

from django.shortcuts import get_object_or_404, render
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from .models import Tweets
from django.template import loader
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
PAGE_SIZE = 10

def index(request):
	data_list = Tweets.objects.all().order_by('-tweet_date')
	paginator = Paginator(data_list,PAGE_SIZE)
	page = request.GET.get('page')
	try:
		data = paginator.page(page)
	except PageNotAnInteger:
        # If page is not an integer, deliver first page.
		data = paginator.page(1)
	except EmptyPage:
       # If page is out of range (e.g. 9999), deliver last page of results.
		data = paginator.page(paginator.num_pages)
	context = {
		'data_list': data,
	}
	return render(request, 'trafficdata/traffic_data_frontend/index.html', context)
	

def detail(request,id):
	print(id)
	data = Tweets.objects.get(tweet_id = id)
	context = {
		'data': data,
	}
	return render(request, 'trafficdata/traffic_data_frontend/detail.html', context)
def about(request):
	pass