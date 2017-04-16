import re
from collections import deque
from files.configurationFile import Configurations
from mysql.connector import connect, Error
from files.twitter_feed import userAuth
from files.status import status
def databaseConnect(Configurations):
    try:
        cnx = connect(**Configurations().dbApiConfig())
        cursor = cnx.cursor()
        db_connect = [cnx,cursor]
        #cursor.execute(sqlQuery)
    except Error as error:
        db_connect = None
    finally:
        cursor.close()
        cnx.close()
    return db_connect
def databaseFind(Configurations,sqlQuery,value):
    try:
        cnx = connect(**Configurations().dbApiConfig())
        cursor = cnx.cursor()
        if not value:#that is value is null -- when all of table data required
            cursor.execute(sqlQuery)
        else:# if all table data is not required  
            a = type("s")
            if type(value)==a:# that is single value
                cursor.execute(sqlQuery,(value,))
            else:
                cursor.execute(sqlQuery,value)
        _id=cursor.fetchall()
    except Error as error:
        a = error
        print(a)
    finally:
        cursor.close()
        cnx.close()
    return _id
def databaseInsert(Configurations,sqlQuery,data):
    try:
        cnx = connect(**Configurations().dbApiConfig())
        cursor = cnx.cursor()
        cursor.execute(sqlQuery,data)
        cnx.commit()
    except Error as error:
        a = error
        print('error')
        print(a)
    finally:
        cursor.close()
        cnx.close()
def FindAllTwitterIds():
    find_all= ("Select user_Twitter_id from trafficdata_user")
    return find_all
def getAllCityString():
    find_all= ("Select city_name from trafficdata_city")
    return find_all
def getAllKeyWordString():
    find_all= ("Select key_word from trafficdata_keywords")
    return find_all
def getAllKeyWord(Configurations):
    userIds = databaseFind(Configurations,getAllKeyWordString(),None)
    city_ids = []
    for ids in userIds:
        city_ids.append(str(ids[0]))
    return city_ids
    
def getAllCity(Configurations):
    userIds = databaseFind(Configurations,getAllCityString(),None)
    city_ids = []
    for ids in userIds:
        city_ids.append(str(ids[0]))
    return city_ids
def getAllTweetstring():
    find_all= ("Select tweet_id,tweet_text from trafficdata_tweets")
    return find_all
def getAllTweets(Configurations):
    data = databaseFind(Configurations,getAllTweetstring(),None)
    return data
def tweetData(tweet):
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
    return (tweet_id,tweet_text,tweet_date)
def findQueryTypeIdString():
    find_query = ("Select id from trafficdata_querytype" " WHERE query_type = %s")
    return find_query

def findcityIdString():
    find_query = ("Select id from trafficdata_city" " WHERE location = %s")
    return find_query
def findKeyWordIdString():
    find_query = ("Select id from trafficdata_keywords" " WHERE key_word = %s")
    return find_query

def findUserIdString():
    find_query = ("Select user_id from trafficdata_user" " WHERE user_Twitter_id = %s")
    return find_query

    
def insertUserString():
    insert_tweets = ("INSERT IGNORE INTO trafficdata_user"
                   "(user_id,user_Twitter_id, screen_name, followers_count, friends_count, time_zone)"
                   "VALUES (%s,%s,%s,%s,%s,%s)")
    return insert_tweets

def insertTweetString():
    insert_tweets = ("INSERT IGNORE INTO trafficdata_tweets"
                   "(tweet_id,tweet_text,tweet_date,traffic_info,location,query_id_id,user_id_id)"
                   "VALUES (%s,%s,%s,%s,%s,%s,%s)")
    return insert_tweets    

def insertQueryString():# for query table
    insert_query = ("INSERT IGNORE INTO trafficdata_query"
                   "(city_id,key_word_id,query_id)"
                   "VALUES (%s,%s,%s)")
    return insert_query
    
def findQueryIdString():
    find_query = ("Select id from trafficdata_query" " WHERE city_id = %s and key_word_id = %s and query_id = %s")
    return find_query
    
def findQueryTypeId(Configurations,value):
    value  = databaseFind(Configurations,findQueryTypeIdString(),value)
    if value:# if id is available
        return value[0][0]# because data in form of tuple like [(1,)]
    else:
        return None
def findQueryId(Configurations,value):# for query table
    value  = databaseFind(Configurations,findQueryIdString(),value)
    if value:# if id is available
        return value[0][0]# because data in form of tuple like [(1,)]
    else:
        return None
def findcityId(Configurations,value):
    value  = databaseFind(Configurations,findcityIdString(),value)
    if value:# if id is available
        return value[0][0]# because data in form of tuple like [(1,)]
    else:
        return None
    
def findKeyWordId(Configurations,value):
    value  = databaseFind(Configurations,findKeyWordIdString(),value)
    if value:
        return value[0][0]# because data in form of tuple like [(1,)]
    else:
        return None
def findUserId(Configurations,value):
    value  = databaseFind(Configurations,findUserIdString(),value)
    if value:
        return value[0][0]# because data in form of tuple like [(1,)]
    else:
        return None
def getAllTwitterIds(Configurations):
    userIds = databaseFind(Configurations,FindAllTwitterIds(),None)
    twitter_ids = deque()
    for ids in userIds:
        twitter_ids.append(str(ids[0]))
    return twitter_ids
def insertUser(Configurations,user_info):
    if user_info:
        for user in user_info:
            data = (user.id,'@'+user.screen_name,user.screen_name,user.followers_count,user.friends_count,user.time_zone)
            databaseInsert(Configurations,insertUserString(),data)
            
def insertTweet(Configurations,tweet,twitter_id,location,key_words,city,query_type):
    tweet_id,tweet_text,tweet_date = tweetData(tweet)
    
    userId = findUserId(Configurations,twitter_id)# user id wrt to give ID
    #By default traffic info and location will be NA
    traffic_info = 'NA'
    location = 'NA'
    query_type_id = findQueryTypeId(Configurations,query_type)
    
    city_id = findcityId(Configurations,city)
    keyword_id = findKeyWordId(Configurations,key_words)
    data = (city_id,keyword_id,query_type_id)
    query_id = findQueryId(Configurations,data)# query id wrt
    
    values = (tweet_id,tweet_text,tweet_date,traffic_info,location,query_id,userId)
    databaseInsert(Configurations,insertTweetString(),values)
    
def insertQuery(Configurations,city,keyword,query_type):# for query table
    city_id = findcityId(Configurations,city)
    keyword_id = findKeyWordId(Configurations,keyword)
    query_id = findQueryTypeId(Configurations,query_type)
    databaseInsert(Configurations,insertQueryString(),(city_id,keyword_id,query_id))# duplicate record inserted   
def getUserInfo(user_ids,Configurations):
    #user_ids = keyWord_().userList()
    api = userAuth(Configurations().twitterApiConfig())
    user_info = deque()
    for x in user_ids:
        print x
        try:
            user = api.get_user(id=x)
            user_info.append(user)
        except:
            print("Error")
        finally:
            pass
    return user_info
    
def inserUserTimelineInfo(Configurations):#save infomation on the basis of twitter ids
    query_type = 'userTimeline'
    #when query_type == userTimeline then city and keyword is not relevant so its going to be Non
    keyword = 'None'
    city = 'None'
    count = 1
    allTwitterIds = getAllTwitterIds(Configurations)
    
    for twitter_id in allTwitterIds:
        
        api = userAuth(Configurations().twitterApiConfig())
        a = api.user_timeline(id = twitter_id,count = 200)
        count = count + 1
        for tweet in a:
            status(count,len(a))
            insertQuery(Configurations,city,keyword,query_type)
            if tweet: #if data available
                # insert all the data in to a tweet table location is none 
                insertTweet(Configurations,tweet,twitter_id,None,keyword,city,query_type)
    
        
#For geoloation based extraction
#try:
#        cnx = connect(**Configurations().dbApiConfig())
#        cursor = cnx.cursor()
#        cursor.execute(getAllKeyWordString())
#        data=cursor.fetchall()
#        print data
#except Error as error:
#        print("Error occour")
#        print(error)    
#finally:
#        cursor.close()
#        cnx.close()
#
#
#        
## In  since_id pass recent tweets
#chicago = "41.881832,-87.627760,30km"
#chennai = "13.083162,80.282758,30km"
#New_york = "40.714264,-73.978499,30km"
#london = "51.505234,-0.111244,30km"
#newdelhi = "28.612952,77.211953,30km"
#indianapolis = "39.767927,-86.158749,30km"
#bombay ="19.110914,72.885140,30km"
#new_jersey = "40.279865,-74.517549,30km"
#words = ['#traffic','traffic','road','road accidents','accidents','congestion','construction']
#userAuth(Configurations().twitterApiConfig())
#a = api.search(q='construction', geocode=chennai)
#
#
#
if __name__ == "__main__":
    inserUserTimelineInfo(Configurations)