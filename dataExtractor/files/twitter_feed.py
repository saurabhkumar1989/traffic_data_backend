import tweepy
from checkConnection import is_connected
import re

def get_userId_data(api,twitter_id,numbr_of_tweets,since_id):
    tweets = api.user_timeline(id= twitter_id ,count = numbr_of_tweets, since_id = since_id)# here tweepy checkt the above user keys
    return tweets
def get_search_query_data(api,twitter_id):
    tweets = api.search(q=twitter_id[0], geocode=twitter_id[1])
    return tweets
# Below function will hit the twitter api and retune all the tweet
def twitterData(query_type,configurations,twitter_id,numbr_of_tweets,since_id):
    auth = tweepy.OAuthHandler(configurations['consumer_key'], configurations['consumer_secret'])
    auth.set_access_token(configurations['access_token'], configurations['access_token_secret'])
    api = tweepy.API(auth)
    internet_working = is_connected()
    all_tweet = []
    # handel error in case of authentication failure or connection error
    if internet_working:
        try:
            #for reference http://docs.tweepy.org/en/v3.5.0/api.html#API.user_timeline
            if query_type == "user_timeline":
                all_tweet = get_userId_data(api,twitter_id ,numbr_of_tweets, since_id)# here tweepy checkt the above user keys
            else:
                all_tweet = get_search_query_data(api,twitter_id)
            
        except tweepy.TweepError as error:
		   print error.message
    else:
         print "Check yout internet connection"
         
    return all_tweet

def tweetData(query_type,twitter_id,tweet):
	#this function is for extracting the tweet data like tweet text, id from a object
	#this return a tuple a according to the query

	#in future release i will update the database to save  emoji also

	######################## for Emoticon removal from tweet.text##################
	#to remove unicode emoji, so 1366: Incorrect
	# string value: '\xF0\x9F\x9A\x97' for column 'tweet_text' at row 1 error can be avoided

    try:
    # Wide UCS-4 build
        myre = re.compile(u'['
            u'\U0001F300-\U0001F64F'
            u'\U0001F680-\U0001F6FF'
            u'\u2600-\u26FF\u2700-\u27BF]+', 
            re.UNICODE)
    except re.error:
        # Narrow UCS-2 build
        myre = re.compile(u'('
            u'\ud83c[\udf00-\udfff]|'
            u'\ud83d[\udc00-\ude4f\ude80-\udeff]|'
            u'[\u2600-\u26FF\u2700-\u27BF])+', 
            re.UNICODE)
######################## End of Emoticon removal###############################
    # myre.sub remove emoticon
    # .encode used to convert unicode in to text
    tweet_text = (myre.sub('', tweet.text)).encode('utf-8')
    tweet_id = tweet.id
    tweet_date =  tweet.created_at.strftime('%Y-%m-%d %H:%M:%S')
    user_id = tweet.author.screen_name
    screen_name = tweet.author.name
    language = tweet.author.lang
    location = tweet.author.location
    followers_count = tweet.author.followers_count
    friends_count = tweet.author.friends_count
    time_zone = tweet.author.time_zone
    query_type = query_type
    if query_type == "user_timeline":
        query = "user_data"
    else:
        query = twitter_id[0] + ','+twitter_id[1]
    return (tweet_id,query_type,query,tweet_text,user_id,tweet_date,\
                     language,location,screen_name,followers_count,friends_count,time_zone)

if __name__ == "__main__":
	pass
