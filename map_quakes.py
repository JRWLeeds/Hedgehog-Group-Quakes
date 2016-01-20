#Importing initial functions
from import_quakes import csv_loader
##Importing plotting function

#Asking whether the user wants one data set or access to all
print('Magnitude options: all, 1.0, 2.5, 4.5, significant')
print('(Magnitude values are greater than or equal to ranges)')
print('Time options: hour, day, week, month')
#whichset = input('Do you want a specific dataset, or access to all of them? (answer spec/all): ')
whichset = 'spec'
#If one specific dataset
if whichset == 'spec':
    #specmag = input('Please input magnitude from options above: ')
    #spectime = input('Please input time from options above: ')
    specmag = '4.5'
    spectime = 'hour'
    
	##Call function for downloading data here, followed by plotting
    dataset = csv_loader(specmag,spectime)
	
#else
    ##Call function in loop to download all data, then call to plot 