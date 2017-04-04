from __future__ import unicode_literals
from django.db import models


# Create your models here.
class Tweets(models.Model):
	tweet_id = models.BigIntegerField(primary_key = True)
	tweet_text = models.CharField(max_length = 200,null=True)
	user_id = models.ForeignKey(
		'User',
		)
	query_id = models.ForeignKey(
		'Query'
		)
	tweet_date = models.DateTimeField(auto_now_add=True,null=True)
	traffic_info = models.CharField(max_length=10,null=True)#  classifier output
	location = models.CharField(max_length=100,null=True)

	def __str__(self):
		return self.tweet_text

class User(models.Model):
	#user_id= models.AutoField(primary_key=True) not require, django will autoatically do that 
	user_Twitter_id = models.CharField(max_length = 50,null=True)
	screen_name = models.CharField(max_length = 50,null=True)
	followers_count = models.IntegerField(null=True)
	friends_count = models.IntegerField(null=True)
	time_zone = models.CharField(max_length = 100,null=True)

	def __str__(self):
		return self.screen_name

class Query(models.Model):
	query = models.ForeignKey(
		'QueryType'
		)
	city = models.ForeignKey(
		'City'
		)
	key_word = models.ForeignKey(
		'KeyWords'
		)
	def __str__(self):
		return self.query.query_type
class City(models.Model):
	#city_id =  models.AutoField(primary_key=True) not require, django will autoatically do that 
	location = models.CharField(max_length=50,null=False)# city longitatude and latitude with radius
	city_name = models.CharField(max_length=50,null=False)# name of the city

class QueryType(models.Model):
	#query_id = models.IntegerField(primary_key=True)#not require, django will autoatically do that 
	query_type = models.CharField(max_length=30)## only two type for now - 1 User time line and 2 Key word + location based

	def __str__(self):
		return self.query_type

class KeyWords(models.Model):
	#key_word_id = models.AutoField(primary_key=True)#not require, django will autoatically do that 
	key_word = models.CharField(max_length=20)# key word for the city like rain,traffic water and so on

	def __str__():
		return self.key_word