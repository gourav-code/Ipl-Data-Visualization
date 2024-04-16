from dash import html
import dash_bootstrap_components as dbc
from collections import deque

def build_component(title="", src=""):
    return dbc.Col([html.Img(
                    className="img-fluid m-2 rounded", src=src,
                    style={"box-shadow": "0 2px 6px 0 rgb(67 89 113 / 20%)"}
                    ),
                    html.Center(html.H6(title, className="m-0"))], className="col-lg-1 col-md-2 col-sm-4")

years = [2008,2009,2010,2011,2012,2013,2014,2015,2016,2017]
teams = ["rr", "dc", "csk", "csk", "kkr", "mi", "kkr", "mi", "srh", "mi"]
icons = []
for team in teams:
    icons.append(f"./assets/img/{team}.svg")
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
        dbc.Col([
            
        
        dbc.Col(html.Div(
            id="winners-first-row",
                className=" mb-2 p-4 justify-content-center", children=test[:], style={'width':'905%'})),
        # dbc.Col(id="winners-second-row",
        #         className="mt-1 mb-2 p-3 justify-content-center", children=test[11:]),
        
    ])

    ], style={"align-text": "center", "padding-left" :'35px'})
])