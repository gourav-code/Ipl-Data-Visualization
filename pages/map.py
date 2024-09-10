import dash
from dash import html, dcc, callback, Input, Output
import plotly.express as px
import pandas as pd
import json

dash.register_page(__name__, path='/')

df = pd.read_csv('csvFiles/matches.csv')

# Example: Load city data (replace with your own data)
data = {
    'City': ['Hyderabad', 'Pune', 'Rajkot', 'Indore', 'Bangalore', 'Mumbai',
       'Kolkata', 'Delhi', 'Chandigarh', 'Kanpur', 'Jaipur', 'Chennai',
       'Ahmedabad', 'Cuttack', 'Nagpur', 'Dharamsala', 'Kochi',
       'Visakhapatnam', 'Raipur', 'Ranchi'],
    'Latitude': [17.4065, 18.5204, 22.3039, 22.7196, 12.9716, 19.0760, 22.5726, 28.7041, 30.7333, 26.4499, 26.9124, 13.0827, 23.0225, 20.4625, 21.1458, 32.2190, 9.9312, 17.6868, 21.2514, 23.3441],
    'Longitude': [78.491684, 73.8567, 70.8022, 75.8577, 77.5946, 72.8777, 88.3639, 77.1025, 76.7794, 80.3319, 75.7873, 80.2707, 72.5714, 85.8828, 79.0882, 76.3234, 76.2673, 83.2185, 81.6296, 85.3096],
    'toss-win-bat-percentage': [46.93877551020408, 53.125, 30.0, 20.0, 13.636363636363637, 40.0, 45.90163934426229, 43.333333333333336, 34.78260869565217, 0.0, 42.42424242424242, 70.83333333333333, 50.0, 28.571428571428573, 66.66666666666667, 11.11111111111111, 40.0, 45.45454545454545, 50.0, 42.857142857142854],
    'toss-win-match-win-percentage': [34.69387755102041, 59.375, 40.0, 80.0, 54.54545454545455, 50.588235294117645, 55.73770491803279, 51.666666666666664, 43.47826086956522, 100.0, 45.45454545454545, 52.083333333333336, 50.0, 71.42857142857143, 33.333333333333336, 55.55555555555556, 40.0, 36.36363636363637, 50.0, 57.142857142857146]
}

df_cities = pd.DataFrame(data)

# Create the map figure
fig = px.scatter_geo(
    df_cities,
    lat='Latitude',
    lon='Longitude',
    hover_name='City',
    title='Indian Cities',
    center={'lat':20.5937, 'lon': 78.9629},
    width=1500,
    height=1000,
    hover_data=['City', 'toss-win-bat-percentage', 'toss-win-match-win-percentage']
    
)
fig.update_geos(
    projection_type='natural earth',  # Set map projection
    showcountries=True,  # Show country borders
    countrycolor='gray',  # Country border color
    showland=True,  # Show land masses
    showocean=True,
    landcolor='lightgray',  # Land color
    center={'lat': 20.5937, 'lon': 78.9629},
    lataxis_range=[5, 40],            # Latitude range for zooming on India
    lonaxis_range=[65, 100] 
)
# Add country highlighting (India)
fig.add_trace(
    px.scatter_geo(df_cities).update_traces(marker=dict(size=10, color='red')).data[0]
)

layout = html.Div([
    html.H1('Indian Cities Map'),
    dcc.Graph(
        id='indian-map',
        figure=fig,
        style={'backgroundColor':'blue'}
    )
    ],
    style={'width': '49%', 'display': 'inline-block'}
)
