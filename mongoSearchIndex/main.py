data = [[1,'first tweet1'],[2,'second tweet2'],[3,'first tweet']]

from pymongo import MongoClient
a ='mongodb://saukumar:1234@ds135680.mlab.com:35680/test_df'
client = MongoClient(a)
# to check whether connected to the database
#print(client.server_info())
db = client.test_df# test_df --> database name
#==========table name is = 'searchIndex' =======
#db.searchIndex.insert({'_id':'test_2u2ser1'})# search index is collection (table)
for record in data:
    _id = record[0]
    tweet = record[1].split()# sentence in to a list
    for word in tweet:
        if db.searchIndex.find_one({'_id':word}):
            temp = db.searchIndex.find_one({'_id':word})
            tweet_ids = temp['tweet_id']#t
            tweet_ids.append(_id)
            db.searchIndex.update({'_id':word},{'$set':{'tweet_id':tweet_ids}})
        else:
            db.searchIndex.insert({'_id':word,'tweet_id':[_id]})
