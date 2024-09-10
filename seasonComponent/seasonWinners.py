from dash import html
import dash_bootstrap_components as dbc
from collections import deque

def build_component(title="", src=""):
    return dbc.Col([html.Img( src=src,
                    style={"height": "7em", "width": "7em"},
                    role="img"
                    ),
                    html.H3(title)], width="auto")

years = [2008,2009,2010,2011,2012,2013,2014,2015,2016,2017]
teams = ["rr", "dc", "csk", "csk", "kkr", "mi", "kkr", "mi", "srh", "mi"]
icons = [f"./assets/img/{team}.svg" for team in teams]

winners = deque()
for title,flag in (zip(years, icons)):
    winners.appendleft(build_component(title, flag))

test = list(winners)

    
WCHeaderCard = html.Div(className="col-md-12 col-lg-3 mb-md-0 mb-4  card-chart-container", children=[
    html.Div(className="card-chart", children=[
        html.Div(className="card-m-0 mt-1 pt-3 pb-3", children=[
            html.H1("IPL Winners",
                    className="card-title text-center m-0 mt-1 ", style={"font-size": "2.5vw", "align-text": "center"}),
        ]),
        dbc.Row(
            id="winners-first-row",
            children=test[:],  # Display all components in a single row
            justify="center",  # Optional: center the components horizontally
            style={'overflow-x': 'auto'}  # Prevent wrapping and allow horizontal scrolling
        ),
    ])
])