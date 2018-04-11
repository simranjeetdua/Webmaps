import folium
import pandas

map=folium.Map(location=[40.7128,-74.0060],zoom_start=6,tiles="Stamen Terrain") #created a map object

fg=folium.FeatureGroup(name="My Map") #FeatureGroup to turn the layer on and off easily

data=pandas.read_csv("Volcanoes_USA.csv") #converted the csv file of volacanoes to a panda dataframe

latitude=list(data["LAT"]) #made a series(list) of dataframe of latitudes
longitude=list(data["LON"]) #made a series (list ) of dataframe of longitudes
elevation=list(data["ELEV"])

def color_producer(el): #used this function to give different marker color according to elevation
    if el in range(0,2000):
        return "green"
    elif el in range(2000,3000):
        return "orange"
    else:
        return "red"


for lat,lon,el in zip(latitude,longitude,elevation): #forloop to add multiple markers using zip function

    fg.add_child(folium.CircleMarker(location=[lat,lon],radius=6,popup=str(el)+" metres",fill_color=color_producer(el),color='black',fill=True,fill_opacity=1)) #added a marker



map.add_child(fg) #added FeatureGroup layer to the map

map.save("MyLoc.html") #saved map object as html, javascript used to display map. using Leaflet library
