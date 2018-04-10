import folium

map=folium.Map(location=[28.6656074,77.1197519],zoom_start=6,tiles="Mapbox Bright") #created a map object

fg=folium.FeatureGroup(name="My Map") #FeatureGroup to turn the layer on and off easily
for coordinates in [28.6656074,77.1197519],[29.6656074,76.1197519]: #forloop to add multiple markers
    fg.add_child(folium.Marker(location=coordinates,popup="My Home",icon=folium.Icon(color='blue'))) #added a marker



map.add_child(fg) #added FeatureGroup layer to the map

map.save("MyLoc.html") #saved map object as html, javascript used to display map. using Leaflet library
