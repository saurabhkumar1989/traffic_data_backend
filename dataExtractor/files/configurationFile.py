# This file will contain all database configuration, also the key for twitter api

class Configurations:
    #db configuration
    userName = 'saukumar'#user name for database
    password = 'rmtdl0680036'
    hostIP ='saukumar.cqjtz8mbwexb.us-west-2.rds.amazonaws.com'
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
    consumer_key = "Hol90i780joDoqDzWS32tR2cn"
    consumer_secret = "wIPsoeGyHbqfmHNcCdATs8GOlPOx9HeU5OlekcGm6D2TtHyUPk"
    access_token = "249152008-zYoxFHAVeDzlWNasuaqxOXBOZpihHCYxi0frmChO"
    access_token_secret = "qBTozbbXA10mdI57sEhOoiYrIE18E2GHg8qCwKnkjNZYl"
    
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
        return 'mongodb://saukumar:1234@ds062059.mlab.com:62059/test_df'

if __name__ == "__main__":
    config = Configurations()
    a = config.twitterApiConfig()
