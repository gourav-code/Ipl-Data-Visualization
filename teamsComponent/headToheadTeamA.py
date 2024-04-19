import pandas as pd
from dash import html, dcc, callback
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import plotly.graph_objs as go
import plotly.express as px

data = pd.read_csv("csvFiles/deliveries.csv")

headTOhead = html.Div([
    html.Div([
        html.H1("Head-to-Head Statistics"),
        dcc.Graph(id='statsOutput'),
        dcc.Graph(
            id='titleWinner',
            config={"displayModeBar": False},
        )
    ])
])

@callback(
    Output("statsOutput", 'figure'),
    [Input("query-team1", "value")],
    [Input("query-team2", "value")]
)

def headToheadstat(teamName1, teamName2):
    df = data.query(f"batting_team == '{teamName1}'").reset_index()
    df1 = data.query(f"batting_team == '{teamName2}'").reset_index()
    runs1 = df.groupby("match_id")['total_runs'].sum().reset_index()
    runs2 = df1.groupby("match_id")['total_runs'].sum().reset_index()

    merged_df = pd.merge(runs1, runs2, on='match_id', suffixes=('_df1', '_df2'), how='inner')
    win1_count = 0
    win2_count = 0
    for tmp in range(merged_df.shape[0]):
        if merged_df['total_runs_df1'][tmp] > merged_df['total_runs_df2'][tmp]:
            win1_count +=1
        if merged_df['total_runs_df1'][tmp] < merged_df['total_runs_df2'][tmp]:
            win2_count += 1

    labels = [teamName1, teamName2]
    values_stat1 = [win1_count, win2_count]
    values_stat2 = [win2_count, win1_count]
    trace1 = go.Pie(labels=labels, values=values_stat1, name='Stat1', hole=0.4)
    trace2 = go.Pie(labels=labels, values=values_stat2, name='Stat2', hole=0.4)
    
    # Create layout for the pie chart
    layout = go.Layout(title=f'Teams Statistics Comparison played {merged_df.shape[0]} matches',
                    hovermode='closest')
    
    # Create figure containing both pie charts
    fig = go.Figure(data=[trace1, trace2], layout=layout)
    
    return fig

@callback(
    Output("titleWinner", 'figure'),
    [Input("query-team1", "value")],
    [Input("query-team2", "value")]
)

def headToheadWinpie(teamName1, teamName2):
    df = pd.read_csv("csvFiles/result.csv")
    tmp = df.query(f"Team == '{teamName1}'").reset_index()
    temp = df.query(f"Team == '{teamName2}'").reset_index()
    appended_df = pd.concat([tmp, temp], axis=0)
    fig=px.sunburst(
            appended_df,
            path=["Qualify", "Team"],
            values="IPL_winner",
            height=350,
            color_discrete_sequence=["#0084d6" , "rgb(3,195,236)", "rgb(113,221,55)", "#8592a3",
                                            "rgba(105, 108, 255, 0.85)", "rgba(3, 195, 236, 0.85)"],
        ).update_layout(
            title = f"Team {teamName1}, Qualify = {list(tmp['Qualify'])[0]} IPL Win = {list(tmp['IPL_winner'])[0]} Team {teamName2}, Qualify = {list(temp['Qualify'])[0]} IPL Win = {list(temp['IPL_winner'])[0]}",
            paper_bgcolor="rgb(0,0,0,0)",
            plot_bgcolor="rgb(0,0,0,0)",
            legend=dict(bgcolor = "#fff"),
            font_family="Public Sans, Amiri, Qatar2022, Poppins,",
            margin={"t": 35, "l": 0, "r": 0, "b": 30}
        )
    
    return fig