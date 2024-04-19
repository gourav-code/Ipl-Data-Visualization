from dash import html
import dash
import dash_bootstrap_components as dbc
from teamsComponent.TeamIntro import TeamHeading,WCteam1,WCteam1image,WCteam2image,WCteam2
from teamsComponent.teamVSteamRun import RunsscoredTeams
from teamsComponent.teamVSteamWicket import WicketTakenTeams
from teamsComponent.headToheadTeamA import headTOhead

dash.register_page(__name__)

layout = html.Div([
    dbc.Row([
        TeamHeading,
        WCteam1,
        WCteam1image,
        WCteam2,
        WCteam2image,
        headTOhead,
        RunsscoredTeams,
        WicketTakenTeams
        ]), 
], style={"padding-top": "40px"})