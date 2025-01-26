import folium
import pandas as pd

# Load the geocoded dataset
file_path = '../data/london_pharmacies_geocoded.csv'
df = pd.read_csv(file_path)

# Initialize a map centered around London
london_map = folium.Map(location=[51.5074, -0.1278], zoom_start=11)

# Add each pharmacy to the map
for _, row in df.iterrows():
    if not pd.isnull(row['Latitude']) and not pd.isnull(row['Longitude']):
        folium.Marker(
            location=[row['Latitude'], row['Longitude']],
            popup=f"<b>{row['Name']}</b><br>{row['Address']}<br>{row['Phone']}",
            icon=folium.Icon(color='blue', icon='info-sign')
        ).add_to(london_map)

# Save the map to an HTML file
map_file_path = '../data/london_pharmacies_map.html'
london_map.save(map_file_path)

print(f"Map saved to '{map_file_path}'. Open this file in your browser to view the map!")
