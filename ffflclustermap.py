import pandas as pd
import folium
from folium.plugins import MarkerCluster
import json
import sys


data_file = "fffl_data.json"
try:
   with open(data_file, "r") as file:
       rawdata = json.load(file)
except FileNotFoundError:
    print(f"{data_file} - json data file not found")
    sys.exit(1)
except json.JSONDecodeError as jde:
    print(f"There was an error docoding json from file {data_file}. {jde}")
    sys.exit(1)
except Exception as e:
    print(f"An unknown exception occured. {e}")
    sys.exit(1)

df = pd.DataFrame(rawdata["Teams"])

# Create a map centered roughly on the Fairview Inn
m = folium.Map(location=[42.08741, -70.64042], zoom_start=6)

# Add a cluster layer
marker_cluster = MarkerCluster().add_to(m)

# Add each team as a marker
style = "<div style='font-size: 1.3em;'>"
for _, row in df.iterrows():
    #popup_text = f"<div style='font-size: 1.3em;'>{row['Team']}<br>Championships: {row['Championships']}<br>({row['Years']})</div>"
    years = ""
    num_championships = len(row['Championships'])
    txt = row['Team']
    if num_championships > 0:
        separator = ", "
        years = separator.join(map(str, row['Championships']))
        txt = "".join([txt, "<br>FFFL Champion: ", years])
    
    popup_text = "".join([style, txt,"</div>"])
    ffflpopup = folium.Popup(popup_text, max_width=400, min_width=200)
    if row["icon_url"] == "default":

        folium.Marker(
            location=[row['Latitude'], row['Longitude']],
            popup=ffflpopup
        ).add_to(marker_cluster)
    else:
        # Use custom icon
        icon_path = f"{row['icon_url']}" 
        custom_icon = folium.features.CustomIcon(
            icon_image=icon_path,
            icon_size=(48, 48) # Adjust size as needed
        )

        folium.Marker(
            location=[row['Latitude'], row['Longitude']],
            popup=ffflpopup,
            icon=custom_icon
        ).add_to(marker_cluster)

        
# Save or display
m.save('fffl_cluster_map.html')
m
