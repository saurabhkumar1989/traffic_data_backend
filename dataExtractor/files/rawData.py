class keyWord_:
    def __init__(self):
        self.twitter_account = ["@SarahJindra","@wazetrafficchi","@GetRaasta","@dtptraffic","@TrafflineDEL","@TrafflineCHN","@TrafflineIndore","@TotalTrafficCHI","@TfL","@HighwaysSEAST","@BillWest5","@John_Kass","@iKartikRao","@shelvieana_prat",
"@prats_09","@94_294_tollway","@DildineMedia","@CrazyRicardo","@TotalTrafficNYC","@WazeTrafficNYC","@Traffic4NY","@NYTrafficAlert","@NYC_DOT","@511NYC","@NYPD_Traffic",
"@NYCityAlerts","@TotalTrafficNYC",]
        self.words = ['#traffic','marriage','happy','rain','water','drain','traffic','road','block','road accidents','accidents','congestion','construction',"frustated","stuck"]
    
        #city list
        chicago = "41.881832,-87.627760,30km"
        chennai = "13.083162,80.282758,30km"
        new_york = "40.714264,-73.978499,30km"
        london = "51.505234,-0.111244,30km"
        newdelhi = "28.612952,77.211953,30km"
        indianapolis = "39.767927,-86.158749,30km"
        bombay ="19.110914,72.885140,30km"
        new_jersey = "40.279865,-74.517549,30km"
        self.geo_locations = [chicago,chennai,new_york,london,newdelhi,indianapolis,bombay,new_jersey]
        self.city_name = ['chicago','chennai','new_york','london','newdelhi','indianapolis','bombay','new_jersey']
    
    
    def userList(self):
        return self.twitter_account
    def wordsList(self):
        return self.words
    def geoLocations(self):
        _locations = dict()
        for data in zip(self.city_name,self.geo_locations):
            _locations[data[0]]= data[1]
        return _locations
    
if __name__ =='__main__':
    dataObj = keyWord_()
    a = dataObj.geoLocations()
    print(a)
    
    