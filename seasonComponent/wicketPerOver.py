import plotly.express as px
import pandas as pd
from dash import html, dcc
import dash_bootstrap_components as dbc

df = pd.read_csv("csvFiles/deliveries.csv")
df.loc[:, 'Wicket'] = 1 

condition = "not (dismissal_kind == 'retired_hurt' or dismissal_kind == 'run out' or dismissal_kind.isna())"
tmp = df.query(condition)
wicket_per_over = tmp.groupby('over')['Wicket'].sum().reset_index()

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


iplWicketperOver = create_card(class_name="card-chart-container col-lg-12 col-md-12 col-sm-12",
                    title="Wickets per Over",
                    fig= px.histogram(wicket_per_over, x = wicket_per_over["over"],y=wicket_per_over["Wicket"], labels={'value': 'over'}, nbins=40,
                        color_discrete_sequence=["#0084d6", "#F0E68C", "rgb(113,221,55)", "#8592a3",
                                                    "rgba(105, 108, 255, 0.85)",
                            "rgba(3, 195, 236, 0.85)"]).update_layout(margin={"r": 20, "t": 10}, 
                        showlegend=False, height = 350).update_yaxes(title_text='Wicket')
                    )