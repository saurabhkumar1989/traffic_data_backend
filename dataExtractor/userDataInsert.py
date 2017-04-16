from files.configurationFile import Configurations
from files.twitter_feed import userAuth
from files.rawData import keyWord_
from mysql.connector import connect, Error
from collections import deque

## Insert All the user in to database
def getUserInfo(user_ids,Configurations):
    #user_ids = keyWord_().userList()
    api = userAuth(Configurations().twitterApiConfig())
    user_info = []
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

def insertUserString():
    insert_tweets = ("INSERT IGNORE INTO trafficdata_user"
                   "(user_id,user_Twitter_id, screen_name, followers_count, friends_count, time_zone)"
                   "VALUES (%s,%s,%s,%s,%s,%s)")
    return insert_tweets
    
def insertKeyWordString():
    insert_tweets = ("INSERT IGNORE INTO trafficdata_keywords"
                   "(key_word)"
                   "VALUES (%s)")
    return insert_tweets
    
def insertCityString():
    insert_tweets = ("INSERT IGNORE INTO trafficdata_city"
                   "(location,city_name)"
                   "VALUES (%s,%s)")
    return insert_tweets
def databaseInsert(Configurations,sqlQuery,data):
    try:
        cnx = connect(**Configurations().dbApiConfig())
        cursor = cnx.cursor()
        cursor.execute(sqlQuery,data)
        cnx.commit()
    except Error as error:
        a = error
        print(a)
    finally:
        cursor.close()
        cnx.close()
        
def insertUser(Configurations,user_info):
    if user_info:
        for user in user_info:
            data = (user.id,'@'+user.screen_name,user.screen_name,user.followers_count,user.friends_count,user.time_zone)
            databaseInsert(Configurations,insertUserString(),data)
def insertKeyWords(Configurations,keyWord_):
    for word in keyWord_().wordsList():#all the key words
        databaseInsert(Configurations,insertKeyWordString(),(word,))
def insertCity(Configurations,keyWord_):
    for city,geoLocation in keyWord_().geoLocations().iteritems():#all the city
        databaseInsert(Configurations,insertCityString(),(city,geoLocation))    
####
user_list = keyWord_().userList()
insertUser(Configurations,getUserInfo(user_list,Configurations))
insertKeyWords(Configurations,keyWord_)
insertCity(Configurations,keyWord_)
#then insert none value for keyword and location
####








