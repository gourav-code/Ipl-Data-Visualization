import plotly.express as px
import pandas as pd
from dash import html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import dash_loading_spinners as dls
from dash import callback
import plotly.graph_objects as go

data = pd.read_csv("csvFiles/deliveries.csv")
team_names = list(data['batting_team'].unique())
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

RunsscoredTeams = html.Div(className="card-chart-container col-lg-15 md-1 sm-1",
                    children=[
                        html.Div(
                            className="card-chart",
                            children=[
                                html.H4(id = 'my-head4', children = "Goals scored by Country in WCs",
                                    className=" card-chart-container", style={"font-size": "1.5vw", "text-align" : "center", 'padding-top': '25px'}),
                                        dls.Roller(
                                            id="team-g3",
                                            children=[
                                    ], debounce=0
                                )
                            ]
                        )

                    ],
                    style={"min-height" :"20.25rem"}
                    )

@callback(
    Output("team-g3", "children"),
    Output("my-head4", "children"),
    [Input("query-team1", "value")],
    [Input("query-team2", "value")]
)

def teamVSteamRunCompare(teamName1, teamName2):
    df = data.query(f"batting_team == '{teamName1}' and bowling_team == '{teamName2}'").reset_index()
    df1 = data.query(f"batting_team == '{teamName2}' and bowling_team == '{teamName1}'").reset_index()
    runs1 = df.groupby("over")['total_runs'].sum().reset_index()
    runs2 = df1.groupby("over")['total_runs'].sum().reset_index()
    runs2.rename(columns={'total_runs': 'total_runs1'}, inplace=True)
    merged_run = pd.merge(runs1,runs2, on='over', how='inner')

    fig = px.histogram(merged_run, x='over', y=["total_runs", "total_runs1"],
                       barmode="group", labels={"over": "Overs", "value": "Runs", "variable": "Team"},
                       color_discrete_sequence=["#0084d6", "#F0E68C"],
                       height=350, nbins=40)

    fig.update_xaxes(title='Overs')
    fig.update_yaxes(title='Runs scored')
    fig.for_each_trace(lambda t: t.update(name=teamName1 if t.name == 'total_runs' else teamName2))
    fig.update_traces(
        hovertemplate='<b>Overs: %{x}</b><br>' +
                      f'{teamName1}'+': %{customdata[0]}<br>' +
                      f'{teamName2}:'+' %{customdata[1]}<br>',
        customdata=merged_run[['total_runs', 'total_runs1']].values
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
    ), f'Runs scored by {teamName1} and {teamName2} in IPL'
