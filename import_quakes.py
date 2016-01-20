

def csv_loader(mag,time):
    import csv
    import urllib2 
    urlbase = 'http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/'
    url= urlbase+mag+'_'+time+'.csv' 
    response = urllib2.urlopen(url)
    cr = csv.reader(response)



