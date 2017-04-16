import tweepy
from collections import deque
from mysql.connector import connect, Error
import re
import tweepy
tweet_id = 0
# DB Configuration
config = {
  'user': 'XXX',
  'password': 'XXX',
  'host': 'XX.XX-westXXX2.rds.XXX.com',
  'database': 'xXX',
  'raise_on_warnings': True,
}
consumer_key = "XXXX"
consumer_secret = "XXXX"
access_token = "XXX-XXXXX"
access_token_secret = "XXXX"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
a = api.search(q='construction', geocode=chennai)
for tweet in a:
    b.append(tweet.text)
    
    
#simple DB Connection
add_data_tweets =("INSERT INTO trafficdata_socialmediadata "
                   "(tweet_id, query_type, query, tweet_text, user_id, tweet_data,language, location, screen_name, followers_count, friends_count, time_zone)"
                   "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")

try:
	cnx = connect(**config)
	cursor = cnx.cursor()
	tweet_data = (125656564,"this is for test","4569",'as','ass',"1970-01-12 00:12:12",'ln','sf','sd',12,12,'e')
	cursor.execute(add_data_tweets, tweet_data)

        #Make sure data is committed to the database
	cnx.commit()

except Error as error:
    print "Error occour"
    print(error)
finally:
	cursor.close()
	cnx.close()
