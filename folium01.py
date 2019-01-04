# import library
import folium
from folium.plugins import MarkerCluster
import pandas as pd

# Load Data
data = pd.read_csv("Volcanoes_USA.txt", error_bad_lines=False)
lat = data['LAT']
lon = data['LON']
elevation = data['ELEV']

#Function to change colors
def color_change(elev):
    if(elev < 1000):
        return('green')
    elif(1000 <= elev <3000):
        return('orange')
    else:
        return('red')


# create base map
map = folium.Map(location=[38.6780,-121.1761], zoom_start=8, tiles = "CartoDB dark_matter")

# add markers
folium.Marker(location=[38.680209,-121.127418], popup="Home", icon=folium.Icon(color='blue')).add_to(map)

#Create Cluster
marker_cluster = MarkerCluster().add_to(map)


# add multiple markers
# Multiple Markers
for lat, lon, elevation in zip(lat, lon, elevation):
    folium.CircleMarker(location=[lat, lon], radius = 9, popup=str(elevation)+" m", fill_color=color_change(elevation), color="gray", fill_opacity = 0.9).add_to(marker_cluster)

#Save the map
map.save("map1.html")

#save the map
map.save("map1.html")
