import dash
from dash import html, dcc, Dash, callback
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go

df2008 = pd.read_csv("csvFiles/2008.csv")
data2008 = df2008.groupby('batsman')['batsman_runs'].sum().reset_index()

df2009 = pd.read_csv("csvFiles/2009.csv")
data2009 = df2009.groupby('batsman')['batsman_runs'].sum().reset_index()

df2010 = pd.read_csv("csvFiles/2010.csv")
data2010 = df2010.groupby('batsman')['batsman_runs'].sum().reset_index()

df2011 = pd.read_csv("csvFiles/2011.csv")
data2011 = df2011.groupby('batsman')['batsman_runs'].sum().reset_index()

df2012 = pd.read_csv("csvFiles/2012.csv")
data2012 = df2012.groupby('batsman')['batsman_runs'].sum().reset_index()

df2013 = pd.read_csv("csvFiles/2013.csv")
data2013 = df2013.groupby('batsman')['batsman_runs'].sum().reset_index()

df2014 = pd.read_csv("csvFiles/2014.csv")
data2014 = df2014.groupby('batsman')['batsman_runs'].sum().reset_index()

df2015 = pd.read_csv("csvFiles/2015.csv")
data2015 = df2015.groupby('batsman')['batsman_runs'].sum().reset_index()

df2016 = pd.read_csv("csvFiles/2016.csv")
data2016 = df2016.groupby('batsman')['batsman_runs'].sum().reset_index()

df2017 = pd.read_csv("csvFiles/2017.csv")
data2017 = df2017.groupby('batsman')['batsman_runs'].sum().reset_index()

data_dict = {
    2008:data2008,
    2009:data2009,
    2010:data2010,
    2011:data2011,
    2012:data2012,
    2013:data2013,
    2014:data2014,
    2015:data2015,
    2016:data2016,
    2017:data2017
}
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

season_run = html.Div([
    html.Div([html.H1("Best Batsman of different season")]),
    html.Div([
        html.P('Select seasons: ', className = 'fix_label', style = {'color': 'white'}),
        dcc.Checklist(
            id = 'checkList-For-Seasons',
            options=[2008,2009,2010,2011,2012,2013,2014,2015,2016,2017],
            value=[2008,2009],
            inline=True
        )
    ]),
    #histogram Batsman
    html.Div([
        dcc.Graph(
            id = 'highest_run_season',
            config = {'displayModeBar': 'hover'}
        ),
    ], className = "create_container three columns"),

    #histogram Bowler
    html.Div([
        dcc.Graph(
            id = 'highest_wickets_season',
            config = {'displayModeBar': 'hover'}
        ),
    ], className = "create_container three columns")

])

@callback(
    Output('highest_run_season', 'figure'),
    [Input('checkList-For-Seasons', 'value')]
)
def highest_run_per_season(yearsList):
    batsmanNameList = []
    runsList = []
    string_yearList = ', '.join([str(x) for x in yearsList])
    # print(type(string_yearList))
    for temp in yearsList:
        tmp = df_dict[temp]
        tmp1 = tmp.groupby('batsman')['batsman_runs'].sum()
        tmp1 = tmp1.reset_index()
        max_index = tmp1['batsman_runs'].idxmax()
        max_row = tmp1.loc[max_index]
        batsmanNameList.append(max_row['batsman'])
        runsList.append(max_row['batsman_runs'])

    bars = []
    for batsmanName, runs, yearListtmp in zip(batsmanNameList, runsList, yearsList):
        hover_text = (
            f'<b>Season Year</b>: {yearListtmp}<br>'
            f'<b>Batsman</b>: {batsmanName}<br>'
            f'<b>Runs</b>: {runs}<br>'
        )
        
        bar = go.Bar(
            x=[batsmanName],  # Set x to the batsman's name (can be customized if multiple bars per batsman)
            y=[runs],         # Set y to the runs scored by the batsman
            text=[runs],  # Text displayed on the bar (can be customized)
            texttemplate='%{text:.2s}',
            textposition='auto',
            textfont=dict(color='white'),
            name='Runs by ' + batsmanName,
            marker=dict(color='#9C0C38'),
            hoverinfo='text',
            hovertext=hover_text
        )
        
        bars.append(bar)

    layout = go.Layout(
        barmode='overlay',
        plot_bgcolor='#010915',
        paper_bgcolor='#010915',
        title={
            'text': f'Batting Performance: {", ".join(batsmanNameList)}<br>{string_yearList}',
            'y': 0.93,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': {
                'color': 'white',
                'size': 20
            }
        },
        hovermode='closest',
        xaxis=dict(
            title='<b>Player</b>',
            tick0=0,
            dtick=1,
            color='white',
            showline=True,
            showgrid=True,
            showticklabels=True,
            linecolor='white',
            linewidth=2,
            ticks='outside',
            tickfont=dict(
                family='Arial',
                size=12,
                color='white'
            )
        ),
        yaxis=dict(
            title='<b>Runs</b>',
            color='white',
            showline=True,
            showgrid=True,
            showticklabels=True,
            linecolor='white',
            linewidth=2,
            ticks='outside',
            tickfont=dict(
                family='Arial',
                size=12,
                color='white'
            )
        ),
        legend=dict(
            orientation='h',
            bgcolor='#010915',
            xanchor='center',
            x=0.5,
            y=-0.3
        ),
        font=dict(
            family="sans-serif",
            size=12,
            color='white'
        )
    )

    return {'data': bars, 'layout': layout}

#For Bowler
@callback(
    Output('highest_wickets_season', 'figure'),
    [Input('checkList-For-Seasons', 'value')]
)
def highest_wicket_per_season(yearsList):
    bowlerName = []
    wicketList = []
    condition = "not (dismissal_kind == 'retired_hurt' or dismissal_kind == 'run out' or dismissal_kind.isna())"
    string_yearList = ', '.join([str(x) for x in yearsList])
    for tmp in yearsList:
        temp = df_dict[tmp]
        dataBowler = temp.query(condition)
        dataBowler.loc[:, 'Wicket'] = 1
        data_wicket_bowler = dataBowler.groupby('bowler')['Wicket'].sum()
        data_wicket_bowler = data_wicket_bowler.reset_index()
        max_index = data_wicket_bowler['Wicket'].idxmax()
        max_row = data_wicket_bowler.loc[max_index]
        bowlerName.append(max_row['bowler'])
        wicketList.append(max_row['Wicket'])

    # print(f"bowler Name: {bowlerName}")
    # print(f"bowler Name: {wicketList}")
    bars = []
    for batsmanName, runs, yearListtmp in zip(bowlerName, wicketList, yearsList): # This is for bowlers
        hover_text = (
            f'<b>Season Year</b>: {yearListtmp}<br>' #batsman is bowlerName
            f'<b>Bowler</b>: {batsmanName}<br>' #runs is wickets
            f'<b>Wicket</b>: {runs}<br>'
        )
        
        bar = go.Bar(
            x=[batsmanName],  # Set x to the batsman's name (can be customized if multiple bars per batsman)
            y=[runs],         # Set y to the runs scored by the batsman
            text=[runs],  # Text displayed on the bar (can be customized)
            texttemplate='%{text:.2s}',
            textposition='auto',
            textfont=dict(color='white'),
            name='Wickets by ' + batsmanName,
            marker=dict(color='#9C0C38'),
            hoverinfo='text',
            hovertext=hover_text
        )
        
        bars.append(bar)

    layout = go.Layout(
        barmode='overlay',
        plot_bgcolor='#010915',
        paper_bgcolor='#010915',
        title={
            'text': f'Bowling Performance: {", ".join(bowlerName)}<br>{string_yearList}',
            'y': 0.93,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': {
                'color': 'white',
                'size': 20
            }
        },
        hovermode='closest',
        xaxis=dict(
            title='<b>Player</b>',
            tick0=0,
            dtick=1,
            color='white',
            showline=True,
            showgrid=True,
            showticklabels=True,
            linecolor='white',
            linewidth=2,
            ticks='outside',
            tickfont=dict(
                family='Arial',
                size=12,
                color='white'
            )
        ),
        yaxis=dict(
            title='<b>Wickets</b>',
            color='white',
            showline=True,
            showgrid=True,
            showticklabels=True,
            linecolor='white',
            linewidth=2,
            ticks='outside',
            tickfont=dict(
                family='Arial',
                size=12,
                color='white'
            )
        ),
        legend=dict(
            orientation='h',
            bgcolor='#010915',
            xanchor='center',
            x=0.5,
            y=-0.3
        ),
        font=dict(
            family="sans-serif",
            size=12,
            color='white'
        )
    )
    # print(bars)
    return {'data': bars, 'layout': layout}

