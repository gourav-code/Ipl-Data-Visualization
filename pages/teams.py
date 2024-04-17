from dash import html
import dash
import dash_bootstrap_components as dbc
from teamsComponent.TeamIntro import TeamHeading,WCteam1

dash.register_page(__name__)

layout = html.Div([
    dbc.Row([
        TeamHeading,
        WCteam1
        ]), 
], style={"padding-top": "40px"})