

def csv_loader(mag,time):
    import csv
    import urllib.request
    import numpy 
    urlbase = 'http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/'
    url= urlbase+mag+'_'+time+'.csv' 
    response = urllib.request.urlopen(url)
    data = numpy.loadtxt(response, delimiter=',')
#    cr = csv.reader(response.read().decode('utf-8'), delimiter=',')

    return cr 


