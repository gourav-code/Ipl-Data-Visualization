from dash import html
import dash_bootstrap_components as dbc
from collections import deque

def build_component(title="", src=""):
    return html.Div([
        html.Img(
            src=src,
            style={
                "height": "5em",
                "width": "5em",
                "margin": "0 auto",
                "display": "block"
            }
        ),
        html.H3(
            title, 
            style={
                "font-size": "1em",
                "text-align": "center",
                "margin-top": "0.5em"
            }
        )
    ], style={
        "display": "inline-block",
        "width": "20%",
        "padding": "10px",
        "box-sizing": "border-box",
        "vertical-align": "top"
    })


years = [2008,2009,2010,2011,2012,2013,2014,2015,2016,2017]
teams = ["rr", "dc", "csk", "csk", "kkr", "mi", "kkr", "mi", "srh", "mi"]
icons = [f"./assets/img/{team}.svg" for team in teams]

winners = deque()
for title,flag in (zip(years, icons)):
    winners.appendleft(build_component(title, flag))

test = list(winners)

    
WCHeaderCard = html.Div(className="col-md-12 col-lg-12 mb-md-0 mb-4 card-chart-container", children=[
    html.Div(className="card-chart", children=[
        html.Div(className="card-m-0 mt-1 pt-3 pb-3", children=[
            html.H1("IPL Winners",
                    className="card-title text-center m-0 mt-1", 
                    style={"font-size": "2.5rem", "text-align": "center"}),
        ]),
        
            dbc.Col([
                dbc.Row(
                    children=list(winners)[:5],  # First row with 5 items
                    justify="center",
                    className="mb-3"
                ),
                dbc.Row(
                    children=list(winners)[5:],  # Second row with remaining items
                    justify="center"
                )
            ], width=12)
    ])
])