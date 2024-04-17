import plotly.express as px
import pandas as pd
from dash import html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import dash_loading_spinners as dls
from dash import callback
import plotly.graph_objects as go

TeamHeading = html.Div(className="card-chart-container col-lg-15 ",
                    children=[
                        html.Div(
                            className="card-chart",
                            style={"font-size": "1.5vw", "text-align" : "center",},
                            children=[
                                html.H4("Team Analysis",
                                    className=" card-chart-container", style={"font-size": "2.3vw", "text-align" : "center", 'padding-top': '15px'}),
                            ]
                        )

                    ],
                    style={"min-height" :"0.25rem"}, 
                    )
df = pd.read_csv("csvFiles/deliveries.csv")
team_names = list(df['batting_team'].unique())
WCteam1 = html.Div(className="col-lg-3 col-md-3 col-sm-3 card-chart-container", children=[html.Div(className="card-chart", children=[
        html.Div(className="card-chart",style={'padding-top': '25px'}, children=[
            html.Div(className="card-chart-container", style={'margin-left': '52px'},children=[
                html.Div(className="card-m-3 me-5 pb-3",
                        children=[
                            dbc.Select(
                                id="query-team1",
                                value="Brazil",
                                options=[
                                    {"label": l, "value": l} for l in team_names
                                ],
                                style={"width": "12rem"}
                            ),
                        ]),

            ])

        ])
    ], style={"min-height": "5rem"})]
    )                    