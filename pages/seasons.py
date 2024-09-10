from dash import html
import dash
import dash_bootstrap_components as dbc
from seasonComponent.seasonRuns import season_run
from seasonComponent.seasonWinners import WCHeaderCard
from seasonComponent.seasonWinRun import WinnerAndRunnerBar
from seasonComponent.runsPerOver import iplRunperOver
from seasonComponent.wicketPerOver import iplWicketperOver
from seasonComponent.seasonWinRun import WinnerAndRunnerWicketsBar
from seasonComponent.iplWinnerRunnerUP import WCWinnersBar, IPLRunnerBar

dash.register_page(__name__)

layout = dbc.Container([
    dbc.Row([WCHeaderCard]),
        dbc.Col([
            season_run,
            WinnerAndRunnerBar,
            WinnerAndRunnerWicketsBar,
            iplRunperOver,
            iplWicketperOver,
            WCWinnersBar,
            IPLRunnerBar
        ])
], fluid = True)
