import plotly.express as px
import pandas as pd
from dash import html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import dash_loading_spinners as dls
from dash import callback


data = pd.read_csv("csvFiles/deliveries.csv")
condition = "not (dismissal_kind == 'retired_hurt' or dismissal_kind == 'run out' or dismissal_kind.isna())"

WicketTakenTeams = html.Div(className="card-chart-container col-lg-15 md-1 sm-1",
                    children=[
                        html.Div(
                            className="card-chart",
                            children=[
                                html.H4(id = 'my-head5', children = "Goals scored by Country in WCs",
                                    className=" card-chart-container", style={"font-size": "1.5vw", "text-align" : "center", 'padding-top': '25px'}),
                                        dls.Roller(
                                            id="team-g4",
                                            children=[
                                    ], debounce=0
                                )
                            ]
                        )

                    ],
                    style={"min-height" :"20.25rem"}
                    )

@callback(
    Output("team-g4", "children"),
    Output("my-head5", "children"),
    [Input("query-team1", "value")],
    [Input("query-team2", "value")]
)

def teamVSteamWicketCompare(teamName1, teamName2):
    df = data.query(f"bowling_team == '{teamName1}'").reset_index()
    df.loc[:, 'Wicket']=1
    df1 = data.query(f"bowling_team == '{teamName2}'").reset_index()
    df1.loc[:, 'Wicket']=1
    runs1 = df.groupby("over")['Wicket'].sum().reset_index()
    runs2 = df1.groupby("over")['Wicket'].sum().reset_index()
    runs2.rename(columns={'Wicket': 'Wicket1'}, inplace=True)
    merged_run = pd.merge(runs1,runs2, on='over', how='inner')

    fig = px.histogram(merged_run, x='over', y=["Wicket", "Wicket1"],
                       barmode="group", labels={"over": "Overs", "value": [teamName1, teamName2], "variable": "Team"},
                       color_discrete_sequence=["#0084d6", "#F0E68C"],
                       height=350, nbins=40)

    fig.update_xaxes(title='Overs')
    fig.update_yaxes(title='Wicket taken')
    fig.update_traces(
        hovertemplate='<b>Overs: %{x}</b><br>' +
                      f'{teamName1}'+': %{customdata[0]}<br>' +
                      f'{teamName2}:'+' %{customdata[1]}<br>',
        customdata=merged_run[['Wicket', 'Wicket1']].values
    )

    return dcc.Graph(
        figure=fig.update_layout(
            paper_bgcolor="rgba(0, 0, 0, 0)",
            plot_bgcolor="rgba(0, 0, 0, 0)",
            showlegend=True,
            font_family="Public Sans, Amiri, Qatar2022, Poppins",
        ),
        config={"displayModeBar": False},
        style={"height": "25.875rem"}
    ), f'Wicket taken by {teamName1} and {teamName2} in IPL'
