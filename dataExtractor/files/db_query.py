# Queries for data insertion in classifiedTweet, processedTweet, tweets
# heavy traffic at newyork street

# Query for inserting data to tweets table
from mysql.connector import connect, Error
from configurationFile import Configurations
from twitter_feed import twitterData,tweetData
import sys
# DB Configuration
config = Configurations()
#Twitter Config
def status(i,num_passe):
    barLength = 20 
    status = ""
    progress = (float(i)/(num_passe))
    block = int(round(barLength*progress))
    sys.stdout.write('\r')
    text = "[{0}] Tweets {1}% Saved.".format( "#"*block + "-"*(barLength-block), format(progress*100,".2f"),status)
    sys.stdout.write(text)
    sys.stdout.flush()

def saveTweetsQery():
    insert_tweets = ("INSERT INTO trafficdata_socialmediadata "
                   "(tweet_id, query_type, query, tweet_text, user_id, tweet_data,language, location, screen_name, followers_count, friends_count, time_zone)"
                   "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")

    return insert_tweets
def saveTweetsQery1():
    insert_tweets = ("INSERT INTO trafficdata_tweetdata "
                   "(tweet_id, tweet_text, user, tweet_date)"
                   "VALUES (%s,%s,%s,%s)")
    return insert_tweets
def mostRecentTweetIdQuery():
    find_max_tweet_id = ("Select max(tweet_id) from trafficdata_socialmediadata" " WHERE user_id = %s ")
    
    return find_max_tweet_id

def mostRecentTweetId(twitter_id):
    # use to find out the mosr recent tweet id
    since_id = 0 
    try:
        cnx = connect(**config.dbApiConfig())
        cursor = cnx.cursor()
        cursor.execute(mostRecentTweetIdQuery(),(twitter_id[1:],))
        data=cursor.fetchall()
        if(data[0][0]):
            since_id = data[0][0]
        else:
            print "No archive tweets available in Database"
            since_id = 700000000000000000 # Initilization number to get started
            #print(since_id) 
    except Error as error:
        print "Error occour"
        print(error)    
    finally:
        cursor.close()
        cnx.close()
    return since_id
    
def saveTweets(query_type,twitter_id,numbr_of_tweets):
    if query_type == "user_timeline":
        since_id = mostRecentTweetId(twitter_id)
    else:
        since_id =  700000000000000000#to do
    #print "Last Tweet ID is %s",since_id
    configurations= config.twitterApiConfig()
    tweets = twitterData(query_type,configurations,twitter_id,numbr_of_tweets,since_id)
    if(tweets):
        for index,tweet in enumerate(tweets):
            try:
                cnx = connect(**config.dbApiConfig())
                cursor = cnx.cursor()
                tweet_data = tweetData(query_type,twitter_id,tweet)
                # Enforce UTF-8 for the connection.
                cursor.execute(saveTweetsQery(), tweet_data)   
                cursor.execute(saveTweetsQery1(), (tweet_data[0],tweet_data[3],tweet_data[4],tweet_data[5]))
                #to make sure data is committed to DB
                cnx.commit()
                status(index+1,len(tweets))
            except Error as error:
                    a = error
                    #print a
            finally:
                    cursor.close()
                    cnx.close()
    else:
    	print"No relevant tweeter feed"

if __name__ == "__main__":
        pass
