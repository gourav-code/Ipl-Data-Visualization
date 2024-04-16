from dash import html
import dash
import dash_bootstrap_components as dbc
from seasonComponent.seasonRuns import season_run
from seasonComponent.seasonWinners import WCHeaderCard

dash.register_page(__name__)

layout = dbc.Container([
    dbc.Row([
        WCHeaderCard,
        dbc.Col([
            season_run
        ])
    ])
])