import pandas as pd
import folium
from folium.plugins import MarkerCluster
import json
import sys

# Example dataset
# data = {
#     "Team": ["Stitchface", "Dread Knights", "Team Testa", "Team Testa", "Blank Willows", "DMZs", "Fish People", "Team Hearthrob", "Capitol Punishment",  "Brady's Bunch", "Clownboyz", "Wardome", "Spice Girls", "Grogan's Heroes",  "Dave and The Detours", "Tie-Dye Warriors", "Portugese Men-o-War"],
#     "City": ["Sandwich", "Lake Worth" , "North Brookfield", "Marshfield", "Accokeek", "Kingston", "Accokeek", "Weymouth", "Herndon", "Los Angeles", "Pembroke", "Walpole", "Quincy", "Florida", "Seattle", "Beverly", "North Andover"],
#     'Championships': [2, 4, 1, 1, 2, 3, 3, 1, 1, 2, 3, 2, 1, 2, 0, 0, 1],
#     "Years": ["2024, 2023", "2022, 2018, 2008, 2004", "2021", "2021", "2020, 2010", "2019, 2017, 2015", "2016, 2014, 2013", "2012", "2011", "2009, 2002", "2007, 2005, 1999", "2006, 1998", "2003", "2001, 2000", "-", "-", "1997"],
#     "Latitude": [41.7558, 26.6168, 42.2686, 42.09089, 38.67065, 42.0034, 38.67509, 42.2151, 38.96430, 34.05502, 42.0715, 42.1417, 42.2555, 28.5384, 47.6205, 42.5584, 42.6986],
#     "Longitude": [-70.5029, -80.0684, -72.0850, -70.70969, -77.03563, -70.7252, -76.9900, -70.9518, -77.3890, -118.41356, -70.8092, -71.2495, -71.0026, -81.3789, -122.3493, -70.8801,  -71.1318],
#     "icon_url": ["img/sf.jpg", "img/dk.jpg", "img/tt.jpg", "img/tt.jpg", "img/bw.jpg", "img/dmzs.jpg", "img/fp.jpg", "img/th.jpg", "img/cp.gif", "default", "img/cb.jpg", "img/wd.jpg", "img/sg.jpg", "default", "img/dd.jpg", "img/tdw.png", "img/pmow.jpg"]
# }

# df = pd.DataFrame(data)

# data = [{   
#         "Team": "Stitchface",
#         "Location": "Foxborough, MA",
#         "Latitude": 41.7558,
#         "Longitude": -70.5029,
#         "State": "MA",
#         "Championships": [2024, 2023],
#         "LastChampionshipYear": 2024,
#         "icon_url": "img/sf.jpg"
#     },
#     {
#         "Team": "Dread Knights",
#         "Location": "Miami, FL",
#         "Latitude": 26.6168,
#         "Longitude": -80.0684,
#         "State": "FL",
#         "Championships": [2022, 2018, 2008, 2004],
#         "LastChampionshipYear": 2022,
#         "icon_url": "img/dk.jpg"
#     },
#     {
#         "Team": "Team Testa",
#         "Location": "Northborough, MA",
#         "Latitude": 42.2686,
#         "Longitude": -72.0850,
#         "State": "MA",
#         "Championships": [2021],
#         "LastChampionshipYear": 2021,
#         "icon_url": "img/tt.jpg"
#     },
#     {
#         "Team": "Team Testa",
#         "Location": "Northborough, MA",
#         "Latitude": 42.09089,
#         "Longitude": -70.70969,
#         "State": "MA",
#         "Championships": [2021],
#         "LastChampionshipYear": 2021,
#         "icon_url": "img/tt.jpg"
#     },
#     {
#         "Team": "Blank Willows",
#         "Location": "Accokeek, MD",
#         "Latitude": 38.67065,
#         "Longitude": -77.03563,
#         "State": "MD",
#         "Championships": [2020, 2010],
#         "LastChampionshipYear": 2020,
#         "icon_url": "img/bw.jpg"
#     },
#     {
#         "Team": "DMZs",
#         "Location": "Kingston, MA",
#         "Latitude": 42.0034,
#         "Longitude": -70.7252,
#         "State": "MA",
#         "Championships": [2019, 2017, 2015],
#         "LastChampionshipYear": 2019,
#         "icon_url": "img/dmzs.jpg"
#     },
#     {
#         "Team": "Fish People",
#         "Location": "Accokeek, MD",
#         "Latitude": 38.67509,
#         "Longitude": -76.9900,
#         "State": "MD",
#         "Championships": [2016, 2014, 2013],
#         "LastChampionshipYear": 2016,
#         "icon_url": "img/fp.jpg"
#     },
#     {
#         "Team": "Team Hearthrob",
#         "Location": "Weymouth, MA",
#         "Latitude": 42.2151,
#         "Longitude": -70.9518,
#         "State": "MA",
#         "Championships": [2012],
#         "LastChampionshipYear": 2012,
#         "icon_url": "img/th.jpg"
#     },
#     {
#         "Team": "Capitol Punishment",
#         "Location": "Herndon, VA",
#         "Latitude": 38.96430,
#         "Longitude": -77.3890,
#         "State": "VA",
#         "Championships": [2011],
#         "LastChampionshipYear": 2011,
#         "icon_url": "img/cp.gif"
#     },
#     {
#         "Team": "Brady's Bunch",
#         "Location": "Los Angeles, CA",
#         "Latitude": 34.05502,
#         "Longitude": -118.41356,
#         "State": "CA",
#         "Championships": [2009, 2002],
#         "LastChampionshipYear": 2009,
#         "icon_url": "img/bradys.png"
#     },
#     {
#         "Team": "Clownboyz",
#         "Location": "Pembroke, MA",
#         "Latitude": 42.0715,
#         "Longitude": -70.8092,
#         "State": "MA",
#         "Championships": [2007, 2005, 1999],
#         "LastChampionshipYear": 2007,
#         "icon_url": "img/cb.jpg"
#     },
#     {
#         "Team": "Wardome",
#         "Location": "Walpole, MA",
#         "Latitude": 42.1417,
#         "Longitude": -71.2495,
#         "State": "MA",
#         "Championships": [2006, 1998],
#         "LastChampionshipYear": 2006,
#         "icon_url": "img/wd.jpg"
#     },
#     {
#         "Team": "Spice Girls",
#         "Location": "Quincy, MA",
#         "Latitude": 42.2555,
#         "Longitude": -71.0026,
#         "State": "MA",
#         "Championships": [2003],
#         "LastChampionshipYear": 2003,
#         "icon_url": "img/sg.jpg"
#     },
#     {
#         "Team": "Grogan's Heroes",
#         "Location": "Daytona, FL",
#         "Latitude": 28.5384,
#         "Longitude": -81.3789,
#         "State": "FL",
#         "Championships": [2001,2000],
#         "LastChampionshipYear": 2001,
#         "icon_url": "img/grogans.jpg"
#     },
#     {
#         "Team": "Dave and The Detours",
#         "Location": "Seattle, WA",
#         "Latitude": 47.6205,
#         "Longitude": -122.3493,
#         "State": "WA",
#         "Championships": [],
#         "LastChampionshipYear": 0,
#         "icon_url": "img/dd.jpg"
#     },
#     {
#         "Team": "Tie-Dye Warriors",
#         "Location": "Charlotte, NC",
#         "Latitude": 42.5584,
#         "Longitude": -70.8801,
#         "State": "NC",
#         "Championships": [],
#         "LastChampionshipYear": 0,
#         "icon_url": "img/tdw.png"
#     },
#     {
#         "Team": "Portugese Men-o-War",
#         "Location": "North Andover, MA",
#         "Latitude": 42.6986,
#         "Longitude": -71.1318,
#         "State": "MA",
#         "Championships": [1997],
#         "LastChampionshipYear": 1997,
#         "icon_url": "img/pmow.jpg"
#     },
#     {
#         "Team": "Fubar",
#         "Location": "defaul",
#         "Latitude": 41.97845,
#         "Longitude": -70.28187,
#         "State": "MA",
#         "Championships": [1996, 1995],
#         "LastChampionshipYear": 1996,
#         "icon_url": "img/fubar.png"
#     },
#     {
#         "Team": "Bud Bowl Bound",
#         "Location": "defaul",
#         "Latitude": 42.08052,
#         "Longitude": -70.31986,
#         "State": "MA",
#         "Championships": [1994],
#         "LastChampionshipYear": 1994,
#         "icon_url": "img/budbowl.png"
#     },
#     {
#         "Team": "Jack's Packers",
#         "Location": "defaul",
#         "Latitude": 42.16808,
#         "Longitude": -70.39354,
#         "State": "MA",
#         "Championships": [1993],
#         "LastChampionshipYear": 1993,
#         "icon_url": "img/jackspack.png"
#     },
#     {
#         "Team": "Copenhagens",
#         "Location": "defaul",
#         "Latitude": 42.26820,
#         "Longitude": -70.47473,
#         "State": "MA",
#         "Championships": [1992],
#         "LastChampionshipYear": 1992,
#         "icon_url": "img/copenhagen.png"
#     }
# ]
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
