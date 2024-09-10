import plotly.express as px
import pandas as pd
from dash import html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import dash_loading_spinners as dls
from dash import callback


TeamHeading = html.Div(className="card-chart-container col-lg-15 ",
                    children=[
                        html.Div(
                            className="card-chart",
                            style={"font-size": "1.5vw", "text-align" : "center",},
                            children=[
                                html.H4("Team Analysis v/s Team Analysis",
                                    className=" card-chart-container", style={"font-size": "2.3vw", "text-align" : "center", 'padding-top': '15px'}),
                            ]
                        )

                    ],
                    style={"min-height" :"0.25rem"}, 
                    )
df = pd.read_csv("csvFiles/deliveries.csv")
team_names = list(df['batting_team'].unique())
team_name_dict = {
    'Sunrisers Hyderabad' : 'srh',
    'Royal Challengers Bangalore': 'rcb',
    'Mumbai Indians' : 'mi',
    'Rising Pune Supergiant' : 'rpsg',
    'Gujarat Lions' : 'gl',
    'Kolkata Knight Riders' : 'kkr',
    'Kings XI Punjab' : 'kxip',
    'Delhi Daredevils' : 'dd',
    'Chennai Super Kings' : 'csk',
    'Rajasthan Royals' : 'rr',
    'Deccan Chargers' : 'dc',
    'Kochi Tuskers Kerala' : 'ktk',
    'Pune Warriors' : 'pwi'
}

#First Team

WCteam1 = html.Div(className="col-lg-3 col-md-3 col-sm-3 card-chart-container", children=[html.Div(className="card-chart", children=[
        html.Div(className="card-chart",style={'padding-top': '25px'}, children=[
            html.Div(className="card-chart-container", style={'margin-left': '52px'},children=[
                html.Div(className="card-m-3 me-5 pb-3",
                        children=[
                            dbc.Select(
                                id="query-team1",
                                value="Chennai Super Kings",
                                options=[
                                    {"label": l, "value": l} for l in team_name_dict.keys()
                                ],
                                style={"width": "12rem"}
                            ),
                        ]),

            ])

        ])
    ], style={"min-height": "5rem"})]
    )  


WCteam1image = html.Div(className="col-lg-3 col-md-3 col-sm-3 card-chart-container", children=[html.Div(className="card-chart", children=[
        html.Div(className="card-chart",style={'padding-top': '25px'}, children=[
            html.Div(className="card-chart-container", style={'margin-left': '62px'},children=[
                html.Div(className="card-m-3 me-5 pb-3",
                        children=[
                            dls.Roller(
                        html.Img(className="img-fluid bx-lg",
                                id="team-flag1",
                                src = '',
                                style={
                                    "height": "15em","width": "15em", 'margin-top':'30px', 'margin-bottom':'20px', 'margin-left':'5px',
                                    "box-shadow": "2px 2px 6px 0 rgb(67 89 113 / 20%)"}
                                ),
                        debounce=0
                    )
                        ]),

            ])

        ])
    ], style={"min-height": "5rem"})]
)    

@callback(
    Output("team-flag1", "src"),
    [Input("query-team1", "value")]
)
def insert_image(teamName):
    firstTeamName = teamName
    team_logo = f"assets/img/{team_name_dict[teamName]}.svg"
    return team_logo

#Second Team                  
WCteam2 = html.Div(className="col-lg-3 col-md-3 col-sm-3 card-chart-container", children=[html.Div(className="card-chart", children=[
        html.Div(className="card-chart",style={'padding-top': '25px'}, children=[
            html.Div(className="card-chart-container", style={'margin-left': '52px'},children=[
                html.Div(className="card-m-3 me-5 pb-3",
                        children=[
                            dbc.Select(
                                id="query-team2",
                                value="Mumbai Indians",
                                options=[
                                    {"label": l, "value": l} for l in team_name_dict.keys()
                                ],
                                style={"width": "12rem"}
                            ),
                        ]),

            ])

        ])
    ], style={"min-height": "5rem"})]
    )
#Second Team logo
WCteam2image = html.Div(className="col-lg-3 col-md-3 col-sm-3 card-chart-container", children=[html.Div(className="card-chart", children=[
        html.Div(className="card-chart",style={'padding-top': '25px'}, children=[
            html.Div(className="card-chart-container", style={'margin-left': '62px'},children=[
                html.Div(className="card-m-3 me-5 pb-3",
                        children=[
                            dls.Roller(
                        html.Img(className="img-fluid bx-lg",
                                id="team-flag2",
                                src = '',
                                style={
                                    "height": "15em", "width": "15em", 'margin-top':'30px', 'margin-bottom':'20px', 'margin-left':'5px',
                                    "box-shadow": "2px 2px 6px 0 rgb(67 89 113 / 20%)"}
                                ),
                        debounce=0
                    )
                        ]),

            ])

        ])
    ], style={"min-height": "5rem"})]
)    

@callback(
    Output("team-flag2", "src"),
    [Input("query-team2", "value")]
)
def insert_image1(teamName):
    team_logo = f"assets/img/{team_name_dict[teamName]}.svg"

    return team_logo

# Parent container to hold both teams' components
WCteamsContainer = html.Div(
    className="d-flex justify-content-center",  # Flexbox to align side by side
    style={"display": "flex", "flex-wrap": "wrap", "justify-content": "center"},
    children=[
        html.Div(children=[WCteam1, WCteam1image], style={"flex": "1", "margin": "10px"}),  # First team and image
        html.Div(children=[WCteam2, WCteam2image], style={"flex": "1", "margin": "10px"}),  # Second team and image
    ]
)
