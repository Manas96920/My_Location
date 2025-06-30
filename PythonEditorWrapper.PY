import geopandas as gpd
from shapely.geometry import Point
import folium

# List of landmarks in Bangalore: (Name, Latitude, Longitude)
landmarks = [
    ("G 703, Sipani Bliss, 1, Taluk, Thirumagondanahalli, Bengaluru, Madivala, Karnataka 562106", 12.780642228805606, 77.72380576988287)
]

# Create GeoDataFrame
gdf = gpd.GeoDataFrame(
    {'Name': [x[0] for x in landmarks]},
    geometry=[Point(x[2], x[1]) for x in landmarks],
    crs='EPSG:4326'
)
# Center map on Bangalore
map_center = [12.9716, 77.5946]
m = folium.Map(location=map_center, zoom_start=12, tiles="OpenStreetMap")

# Add all landmarks to the map
for name, point in zip(gdf["Name"], gdf.geometry):
    folium.Marker(
        location=[point.y, point.x],  # lat, lon
        popup=folium.Popup(f"<b>{name}</b>", max_width=300),
        icon=folium.Icon(color='blue', icon='info-sign')
    ).add_to(m)

# Optional: add GeoJSON layer for overlays
folium.GeoJson(gdf, name="Landmarks").add_to(m)

# Add layer control for interactivity
folium.LayerControl().add_to(m)

# Save and show map
m.save("bangalore_landmarks_interactive.html")
print("Interactive map with Bangalore landmarks saved as 'bangalore_landmarks_interactive.html'")

import webbrowser
webbrowser.open("bangalore_landmarks_interactive.html")