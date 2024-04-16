import dash
from dash import html, dcc, Dash, callback
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px

df2008 = pd.read_csv("csvFiles/2008.csv")
df2009 = pd.read_csv("csvFiles/2009.csv")
df2010 = pd.read_csv("csvFiles/2010.csv")
df2011 = pd.read_csv("csvFiles/2011.csv")
df2012 = pd.read_csv("csvFiles/2012.csv")
df2013 = pd.read_csv("csvFiles/2013.csv")
df2014 = pd.read_csv("csvFiles/2014.csv")
df2015 = pd.read_csv("csvFiles/2015.csv")
df2016 = pd.read_csv("csvFiles/2016.csv")
df2017 = pd.read_csv("csvFiles/2017.csv")

df_dict = {
    2008:df2008,
    2009:df2009,
    2010:df2010,
    2011:df2011,
    2012:df2012,
    2013:df2013,
    2014:df2014,
    2015:df2015,
    2016:df2016,
    2017:df2017
}
years = []
for tmp in range(2008,2018):
    years.append(tmp)

winners = ['Rajasthan Royals', 'Deccan Chargers','Chennai Super Kings','Chennai Super Kings','Kolkata Knight Riders','Mumbai Indians','Kolkata Knight Riders','Mumbai Indians','Sunrisers Hyderabad','Mumbai Indians' ]
runnerUp = ['Chennai Super Kings','Royal Challengers Bangalore','Mumbai Indians','Royal Challengers Bangalore','Chennai Super Kings','Chennai Super Kings','Kings XI Punjab','Chennai Super Kings','Royal Challengers Bangalore','Rising Pune Supergiant']

winner_runs = []
runner_runs = []
for win, runn, year in zip(winners, runnerUp, years):
    tmp = df_dict[year]
    temp = tmp.groupby('batting_team')['total_runs'].sum().reset_index()
    tmp1 = temp.query(f"batting_team == '{win}'")
    tmp1 = list(tmp1['total_runs'])
    winner_runs.append(tmp1[0])
    tmp1 = temp.query(f"batting_team == '{runn}'")
    tmp1 = list(tmp1['total_runs'])
    runner_runs.append(tmp1[0])

df_winn_runn = pd.DataFrame({'year':years,'winner':winner_runs, 'runner_up':runner_runs, 'winners_name':winners, 'runner_name':runnerUp})

#wickets by winner and runner
# df.loc[:, 'Wicket'] =1 
winner_wickets = []
runner_wickets = []
condition = "not (dismissal_kind == 'retired_hurt' or dismissal_kind == 'run out' or dismissal_kind.isna())"
for win, runn, year in zip(winners, runnerUp, years):
    tmp = df_dict[year]
    tmp.loc[:, 'Wicket']=1
    temp = tmp.query(condition)
    wickets_by_teams = temp.groupby('bowling_team')['Wicket'].sum().reset_index()
    wickets_by_winner = wickets_by_teams.query(f"bowling_team == '{win}'")
    winner_wickets.append(list(wickets_by_winner['Wicket'])[0])
    wickets_by_runn = wickets_by_teams.query(f"bowling_team == '{runn}'")
    runner_wickets.append(list(wickets_by_runn['Wicket'])[0])

df_winn_runn_wickets = pd.DataFrame({'year':years,'winner':winner_wickets, 'runner_up':runner_wickets, 'winners_name':winners, 'runner_name':runnerUp})

def create_card(fig, class_name, title="Title"):
    return html.Div(
        html.Div(
            className="card-chart",
            children=[
                html.H4(title,
                        className="card-m-0 pt-2 pb-3 text-center", style={"font-size": "1.8vw", "align-text": "center"}),
                dcc.Graph(
                    figure=fig.update_layout(
                        paper_bgcolor="rgb(0,0,0,0)",
                        plot_bgcolor="rgb(0,0,0,0)",
                        legend=dict(bgcolor = "#fff"),
                        font_family = "Public Sans, Amiri, Qatar2022, Poppins,",
                    ),
                    config={"displayModeBar": False},
                )
            ],
        ), className=class_name
    )

WinnerAndRunnerBar = create_card(class_name="card-chart-container col-lg-12 col-md-12 col-sm-12",
                                title="Winner and Runner-Up Runs For whole IPL",
                                fig=px.histogram(df_winn_runn, x=df_winn_runn["year"],
                                y=["winner", "runner_up"],
                                barmode="group", labels={"year": "Year","value":"Runs", "variable": "Team"},
                                color_discrete_sequence= ["#0084d6", "#F0E68C","rgb(113,221,55)", "#8592a3",
                                                    "rgba(105, 108, 255, 0.85)", "rgba(3, 195, 236, 0.85)"],
                                height= 350,
                                ).update_layout(yaxis_title="Runs").update_xaxes(type='category').update_traces(
                                    hovertemplate='<b>Year: %{x}</b><br>' +
                                    'Winner :''%{customdata[0]}<br>' +
                                    'Runner up: %{customdata[1]}<br>'+
                                    '%{y} runs<br>',
                                    customdata=df_winn_runn[['winners_name', 'runner_name']].values
                                )
                                )


WinnerAndRunnerWicketsBar = create_card(class_name="card-chart-container col-lg-12 col-md-12 col-sm-12",
                                title="Winner and Runner-Up Wickets For whole IPL",
                                fig=px.histogram(df_winn_runn_wickets, x=df_winn_runn_wickets["year"],
                                y=["winner", "runner_up"],
                                barmode="group", labels={"year": "Year","value":"Wickets", "variable": "Team"},
                                color_discrete_sequence= ["#0084d6", "#F0E68C","rgb(113,221,55)", "#8592a3",
                                                    "rgba(105, 108, 255, 0.85)", "rgba(3, 195, 236, 0.85)"],
                                height= 350,
                                ).update_layout(yaxis_title="Wickets").update_xaxes(type='category').update_traces(
                                    hovertemplate='<b>Year: %{x}</b><br>' +
                                    'Winner :''%{customdata[0]}<br>' +
                                    'Runner up: %{customdata[1]}<br>'+
                                    '%{y} wicket<br>',
                                    customdata=df_winn_runn_wickets[['winners_name', 'runner_name']].values
                                ))