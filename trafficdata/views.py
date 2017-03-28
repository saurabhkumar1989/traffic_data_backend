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
	city_list = Tweets.objects.order_by().values_list('location',flat=True).distinct()# get all the distinct city value
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
	context = {
		'data': data,
		'users_list': users_list,
		'city_list':city_list,
	}
	return render(request, 'trafficdata/traffic_data_frontend/index.html', context)
	

def detail(request,id):
	data = Tweets.objects.get(tweet_id = id)
	context = {
		'data': data,
	}
	return render(request, 'trafficdata/detail.html', context)
def search(request):
	city_list = Tweets.objects.order_by().values_list('location',flat=True).distinct()
	users_list = User.objects.all()
	if request.method == "GET":
		userQuery = request.GET.get('userQuery')# text input from the search bar
		userOption = request.GET.get('user')# user option from the user drop down
		cityOption = request.GET.get('city')# option from city drop down
		print(cityOption)
		if userOption!=None and cityOption!=None:#both field insert
			user_id = User.objects.get(screen_name = userOption)
			data = Tweets.objects.filter(user_id = user_id ).filter(location=cityOption)
		elif userOption== None and cityOption!=None:
			data = Tweets.objects.filter().filter(location=cityOption)
		elif userOption!= None and cityOption==None:
			user_id = User.objects.get(screen_name = userOption)
			data = Tweets.objects.filter(user_id = user_id )
		else: #both blank
			data = Tweets.objects.all().order_by('-tweet_date')
	context = {
		'data': data,
		'users_list': users_list,
		'city_list':city_list,
		}
	return render(request, 'trafficdata/index.html',context)

def about(request):
	pass