

def csv_loader(mag,time):
    import csv
    import urllib 
    urlbase = 'http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/'
    url= urlbase+mag+'_'+time+'.csv' 
    response = urllib.request.urlopen(url)
    cr = csv.reader(response)



