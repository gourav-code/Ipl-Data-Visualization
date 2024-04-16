import plotly.express as px
import pandas as pd
from dash import html, dcc
import dash_bootstrap_components as dbc

def create_card(fig, class_name, title="Title"):
    return html.Div(
        html.Div(
            className="card-chart",
            children=[
                html.H4(title,
                        className="card-m-0 mt-1 pt-2 pb-3 text-center", style={"font-size": "1.8vw", "align-text": "center"}),
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

winners = ['Rajasthan Royals', 'Deccan Chargers','Chennai Super Kings','Chennai Super Kings','Kolkata Knight Riders','Mumbai Indians','Kolkata Knight Riders','Mumbai Indians','Sunrisers Hyderabad','Mumbai Indians' ]
runnerUp = ['Chennai Super Kings','Royal Challengers Bangalore','Mumbai Indians','Royal Challengers Bangalore','Chennai Super Kings','Chennai Super Kings','Kings XI Punjab','Chennai Super Kings','Royal Challengers Bangalore','Rising Pune Supergiant']
years = []
for tmp in range(2008,2018):
    years.append(tmp)

df_winn_runn = pd.DataFrame({'year':years, 'winners_name':winners, 'runner_name':runnerUp})

WCWinnersBar = create_card(class_name="card-chart-container col-lg-12 col-md-12 col-sm-12",
                title="IPL Winner",
                fig=px.bar(
                df_winn_runn.groupby("winners_name", as_index=False).size(),
                    x="winners_name",
                    y="size",
                    height=350,
                    text="size",
                    color_discrete_sequence=["#0084d6", "#F0E68C", "rgb(113,221,55)", "#8592a3",
                                                    "rgba(105, 108, 255, 0.85)", "rgba(3, 195, 236, 0.85)"],
                    labels={"value": "Team",
                                "size": "", "winner": "Winner"},
                                ).update_xaxes(categoryorder="total descending",
                                ).update_layout(margin={"r": 20, "l": 30}))

IPLRunnerBar = create_card(class_name="card-chart-container col-lg-12 col-md-12 col-sm-12",
                title="IPL Runner Up",
                fig=px.bar(
                df_winn_runn.groupby("runner_name", as_index=False).size(),
                    x="runner_name",
                    y="size",
                    height=350,
                    text="size",
                    color_discrete_sequence=["#0084d6", "#F0E68C", "rgb(113,221,55)", "#8592a3",
                                                    "rgba(105, 108, 255, 0.85)", "rgba(3, 195, 236, 0.85)"],
                    labels={"value": "Team",
                                "size": "", "winner": "Winner"},
                                ).update_xaxes(categoryorder="total descending",
                                ).update_layout(margin={"r": 20, "l": 30}))