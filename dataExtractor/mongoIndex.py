from files.configurationFile import Configurations
from files.status import status
from pymongo import MongoClient
from tweetsInsert import getAllTweets

def mongoSearchIndex(Configurations):
    client = MongoClient(Configurations().mongoDBConfig())
    
    data = getAllTweets(Configurations)
    # to check whether connected to the database
    db = client.test_df# test_df --> database name
    count = 1
    for record in data:
        count = count + 1
        _id = record[0]
        tweet = (record[1].lower()).split()# sentence in to a list
        for word in tweet:
            if db.searchIndex.find_one({'_id':word}):
                temp = db.searchIndex.find_one({'_id':word})
                tweet_ids = temp['tweet_id']#t
                tweet_ids.append(_id)
                db.searchIndex.update_many({'_id':word},{'$set':{'tweet_id':tweet_ids}})
            else:
                db.searchIndex.insert_one({'_id':word,'tweet_id':[_id]})
        status(count,len(data))

mongoSearchIndex(Configurations)
