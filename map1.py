import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
name = list(data["NAME"])
loc = list(data["LOCATION"])
elev = list(data["ELEV"])

def color(elevation):
    if elevation < 1500:
        return 'green'
    elif 1500<= elevation < 3000:
        return 'orange'
    else:
        return 'red' 

map = folium.Map(location=[38.58, -99.09], zoom_start=6)

fg = folium.FeatureGroup(name="My Map")

for lt, ln, na, lo, el in zip(lat, lon, name, loc, elev):
    fg.add_child(folium.Marker(location=[lt, ln], popup=str(na)+" "+str(lo)+" "+str(el)+" m", icon=folium.Icon(color=color(el))))

map.add_child(fg)

map.save("Map1.html")