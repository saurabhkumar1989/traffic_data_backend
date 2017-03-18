from django.shortcuts import render

# Create your views here.

from django.shortcuts import get_object_or_404, render
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from .models import Tweets,User,City
from django.template import loader
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
PAGE_SIZE = 10

def index(request):
	city_list = City.objects.all()
	users_list = User.objects.all()
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
	#print(users)
	context = {
		'data': data,
		'users_list': users_list,
		'city_list':city_list,
	}
	return render(request, 'trafficdata/traffic_data_frontend/index.html', context)
	

def detail(request,id):
	print(id)
	data = Tweets.objects.get(tweet_id = id)
	context = {
		'data': data,
	}
	return render(request, 'trafficdata/traffic_data_frontend/detail.html', context)
def search(request):
	city_list = City.objects.all()
	users_list = User.objects.all()
	if request.method == "GET":
		userQuery = request.GET.get('userQuery')# text input from the search bar
		userOption = request.GET.get('user')# user option from the user drop down
		user_id = User.objects.get(screen_name = userOption)
		data = Tweets.objects.filter(user_id = user_id )
		context = {
		'data': data,
		'users_list': users_list,
		'city_list':city_list,
		}
	return render(request, 'trafficdata/traffic_data_frontend/index.html',context)

def about(request):
	pass