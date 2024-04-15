from dash import html
import dash
import dash_bootstrap_components as dbc
from seasonComponent.seasonRuns import season_run

dash.register_page(__name__)

layout = html.Div([
    dbc.Row([season_run])
])