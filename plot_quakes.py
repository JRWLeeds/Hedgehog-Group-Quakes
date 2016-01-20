"""Program to plot earthquake data, allowing changes between datasets"""

import csv

# Open the earthquake data file.
filename = 'datasets/earthquake_data.csv'

# Create empty lists for the latitudes, longitudes and magnitudes.
lats, lons, mag = [], [], []

# Read through the entire file, skip the first line,
#  and pull out just the lats, lons and mag.
with open(filename) as f:
    # Create a csv reader object.
    reader = csv.reader(f)
    
    # Ignore the header row.
    next(reader)
    
    # Store the latitudes, longitudes and magnitudes in the appropriate lists.
    for row in reader:
        lats.append(float(row[1]))
        lons.append(float(row[2]))
        mag.append(float(row[4]))
 
# --- Build Map ---
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
 
eq_map = Basemap(projection='robin', resolution = 'l', area_thresh = 1000.0,
              lat_0=0, lon_0=-130)
eq_map.drawcoastlines()
eq_map.drawcountries()
eq_map.fillcontinents(color = 'gray')
eq_map.drawmapboundary()
eq_map.drawmeridians(np.arange(0, 360, 30))
eq_map.drawparallels(np.arange(-90, 90, 30))
 
x,y = eq_map(lons, lats)
i=0

# Plot the data with different size markers for earthquakes of different magnitudes
for magnitude in mag:
    if magnitude < 3.0:
        eq_map.plot(x[i], y[i], 'go', markersize=4) # plots magnitude up to 3
    elif magnitude < 5.0:
        eq_map.plot(x[i], y[i], 'yo', markersize=6) # plots magnitude 3 and 4
    elif magnitude < 6.5:
        eq_map.plot(x[i], y[i], 'ro', markersize=8) # plots magnitude 5-6.5
    else:
        eq_map.plot(x[i], y[i], 'bo', markersize=10) # plots magnitude 6.5 and higher
    i=i+1

plt.show()