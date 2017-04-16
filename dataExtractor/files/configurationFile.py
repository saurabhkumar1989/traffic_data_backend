# This file will contain all database configuration, also the key for twitter api

class Configurations:
    #db configuration
    userName = 'sXXXr'#user name for database
    password = 'XXXXXXX36'
    hostIP ='sXXXXXXXXamazonaws.com'
    databaseName = 'trafficdata'
    raise_on_warnings = True

    dbconfig = {
        'user': userName,
        'password': password,
        'host': hostIP,
        'database': databaseName,
        'raise_on_warnings': True,
    }
    def dbApiConfig(self):
        # return db configuration
        return self.dbconfig


    #twitter api configuration
    consumer_key = "HXXXXXXXXXXXXcn"
    consumer_secret = "wIPsXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXm6D2TtHyUPk"
    access_token = "24915XXXXXXXXXXXXXXXXXXXXXXrmChO"
    access_token_secret = "qBTozbXXXXXXXXXXXXXXXXXXXXXXXXXXXxjNZYl"
    
    twitter_config = {
                   'consumer_key' : consumer_key,
                   'consumer_secret': consumer_secret,
                   'access_token': access_token,
                   'access_token_secret': access_token_secret
                   }

    def twitterApiConfig(self):
        # return twitter api configuration
        return self.twitter_config
    def mongoDBConfig(self):
        # return twitter api configuration
        return 'mongodb://XXXXXXX:XXXXXX@XXXXX.mlab.com:XXXXXXX/test_df'

if __name__ == "__main__":
    config = Configurations()
    a = config.twitterApiConfig()
