from django.shortcuts import render

# Create your views here.
from pymongo import MongoClient#mongo db client
from django.shortcuts import get_object_or_404, render
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from .models import Tweets,User,City
from django.template import loader
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
PAGE_SIZE = 10
MONGO_URI = 'mongodb://saukumar:1234@ds135680.mlab.com:35680/test_df'
client = MongoClient(MONGO_URI)
db = client.test_df# test_df --> database name
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
	return render(request, 'trafficdata/index.html', context)
	

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
		userQuery = request.GET.get('userQuery')
		# text input from the search bar
		userOption = request.GET.get('user')
		# user option from the user drop down
		cityOption = request.GET.get('city')
		# option from city drop down
		print(cityOption)

		#for text filter
		if userOption and cityOption and userQuery:#both field insert[111]
			_ids = getMongoId(userQuery)
			user_id = User.objects.get(screen_name = userOption)
			if _ids==None:#if user ids is none then __in flter can't be used
				data = Tweets.objects.filter(user_id = user_id ).filter(location=cityOption).filter(tweet_id=_ids)
			else:
				data = Tweets.objects.filter(user_id = user_id ).filter(location=cityOption).filter(tweet_id__in=_ids)
		elif userOption== None and cityOption ==None and userQuery:#[001]
			_ids = getMongoId(userQuery)
			if _ids==None:
				data = Tweets.objects.filter(tweet_id=_ids)
			else:
				data = Tweets.objects.filter(tweet_id__in=_ids)
		elif userOption== None and cityOption and userQuery==None:
			data = Tweets.objects.filter(location=cityOption)
		elif userOption==None and cityOption and userQuery:
			_ids = getMongoId(userQuery)
			if _ids==None:
				data = Tweets.objects.filter(location=cityOption).filter(tweet_id=_ids)
			else:
				data = Tweets.objects.filter(location=cityOption).filter(tweet_id__in=_ids)
		elif userOption and cityOption==None and userQuery==None:
			user_id = User.objects.get(screen_name = userOption)
			data = Tweets.objects.filter(user_id = user_id )
		elif userOption and cityOption==None and userQuery:
			_ids = getMongoId(userQuery)
			user_id = User.objects.get(screen_name = userOption)
			if _ids:
				data = Tweets.objects.filter(user_id = user_id ).filter(tweet_id=_ids)
			else:
				data = Tweets.objects.filter(user_id = user_id ).filter(tweet_id__in=_ids)
		elif userOption and cityOption and userQuery==None:
			user_id = User.objects.get(screen_name = userOption)
			data = Tweets.objects.filter(user_id = user_id ).filter(location=cityOption)
		else: #everything blank
			data = Tweets.objects.all().order_by('-tweet_date')
	context = {
		'data': data,
		'users_list': users_list,
		'city_list':city_list,
		}
	return render(request, 'trafficdata/index.html',context)

def about(request):
	pass
def getMongoId(query):
    temp = db.searchIndex.find({'_id':query})
    if temp.count():
        return temp[0]['tweet_id']
    return None