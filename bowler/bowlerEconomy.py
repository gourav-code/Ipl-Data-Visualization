import dash
from dash import html, dcc, Dash, callback
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go

df = pd.read_csv("csvFiles/deliveries.csv")
allBowlerName = df['bowler'].unique().tolist()

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

slider = html.Div([
        html.Div([html.H1("Bowler economy per year")]),
        html.Div(id='output1-heading'),
        html.Div([html.Div([
            # bowler dropdown
            html.P('Select Bowler:', className = 'fix_label', style = {'color': 'white'}),
            dcc.Dropdown(id = 'bowler_name_id',
                         multi = False,
                         clearable = True,
                         disabled = False,
                         style = {'display': True},
                         value = 'Z Khan',
                         placeholder = 'Select Bowler Name',
                         options = [{'label': c, 'value': c}
                                    for c in allBowlerName], className = 'dcc_compon'),
            #years slider 
            html.P('Select Year:', className = 'fix_label', style = {'color': 'white', 'margin-left': '1%'}),
            dcc.RangeSlider(id = 'select_years_1',
                            min = 2008,
                            max = 2017,
                            step=1,
                            marks={year: str(year) for year in range(2008, 2018)},
                            value = [2008, 2017]),
                            

        ], className = "create_container three columns"),

        #histogram div
        html.Div([
            dcc.Graph(id = 'bar_line_2',
                      config = {'displayModeBar': 'hover'}),

        ], className = "create_container three columns"),

    ], className = "row flex-display")
])

#create histogram callback
@callback(
            Output('bar_line_2', 'figure'),
            [Input('bowler_name_id', 'value')],
            [Input('select_years_1', 'value')]
        )
def update_bower_histogram_graph(bowler_name, selected_years):
    start_year = selected_years[0]
    end_year = selected_years[1]
    wickets_list = []
    number_overs_list = []
    runs_conceded_list = []
    economy_list = []
    number_matches_list = []
    years = []
    while(start_year <= end_year):
        tmp = df_dict[start_year]
        bowlerPerform = tmp.query(f"bowler == '{bowler_name}'")
        if bowlerPerform.shape[0] == 0:
            start_year += 1
            continue
        #number_of_overs
        number_over = 0
        fix_parameter = 0
        for temp in bowlerPerform['over']:
            if int(temp) != fix_parameter:
                number_over += 1
                fix_parameter = int(temp)
        number_overs_list.append(number_over)
        #runs_conceded or economy
        runs_byBowler = bowlerPerform.groupby("match_id")['wide_runs', 'noball_runs', 'batsman_runs'].sum()
        all_runs_byBowler_in_matches = runs_byBowler['wide_runs']+runs_byBowler['noball_runs']+runs_byBowler['batsman_runs']
        all_runs_byBowler = all_runs_byBowler_in_matches.sum()
        runs_conceded_list.append(all_runs_byBowler)
        economy_list.append(round(all_runs_byBowler/number_over,2))
        number_matches_list.append(len(all_runs_byBowler_in_matches))
        #wickets
        wickets = 0
        for temp in bowlerPerform['dismissal_kind']:
            if (not(pd.isna(temp) or temp == 'retired_hurt' or temp == 'run out')):
                wickets += 1
        wickets_list.append(wickets)
        years.append(start_year)
        start_year += 1

    return_var = {
        "data" : [
            go.Bar(
                x = years,
                y = wickets_list,
                text = wickets_list,
                texttemplate = '%{text:.2s}',
                textposition = 'auto',
                textfont = dict(
                    color = 'white'
                ),
                name = 'Wickets by '+str(bowler_name),
                marker = dict(color = '#9C0C38'),
                hoverinfo = 'text',
                hovertext =
                '<b>Year</b>: ' + str(selected_years[0])+ '-'+ str(selected_years[1]) + '<br>' +
                '<b>Bowler</b>: ' + bowler_name + '<br>'+
                '<b>Wickets'
            ),
            go.Bar(
                x = years,
                y = economy_list,
                text = economy_list,
                texttemplate = '%{text:.2s}',
                textposition = 'auto',
                textfont = dict(
                    color = 'white'
                ),
                name = 'Economy by '+str(bowler_name),
                marker = dict(color = 'orange'),
                hoverinfo = 'text',
                hovertext =
                '<b>Year</b>: ' + str(selected_years[0])+ '-'+ str(selected_years[1]) + '<br>' +
                '<b>Bowler</b>: ' + bowler_name + '<br>' + 
                '<b>Economy'
            ),
            go.Bar(
                x = years,
                y = number_matches_list,
                text = number_matches_list,
                texttemplate = '%{text:.2s}',
                textposition = 'auto',
                textfont = dict(
                    color = 'white'
                ),
                name = 'Number of matches by '+str(bowler_name),
                marker = dict(color = 'blue'),
                hoverinfo = 'text',
                hovertext =
                '<b>Year</b>: ' + str(selected_years[0])+ '-'+ str(selected_years[1]) + '<br>' +
                '<b>Bowler</b>: ' + bowler_name + '<br>' + 
                '<b>matches'
            )
        ],
        'layout': go.Layout(
                    barmode = 'group',
                    plot_bgcolor = '#010915',
                    paper_bgcolor = '#010915',
                    title = {
                        'text': 'Bowling Performance : ' + (bowler_name) + '  ' + '<br>' + ' - '.join( [str(y) for y in years]) + '</br>',
                        'y': 0.93,
                        'x': 0.5,
                        'xanchor': 'center',
                        'yanchor': 'top'
                        },
                    titlefont = {
                        'color': 'white',
                        'size': 20
                        },
                    hovermode = 'x',
                    xaxis = dict(title = '<b>Year</b>',
                                tick0 = 0,
                                dtick = 1,
                                color = 'white',
                                showline = True,
                                showgrid = True,
                                showticklabels = True,
                                linecolor = 'white',
                                linewidth = 2,
                                ticks = 'outside',
                                tickfont = dict(
                                    family = 'Arial',
                                    size = 12,
                                    color = 'white'
                                )
                                ),

                    yaxis = dict(title = '<b>Runs by '+ bowler_name+'</b>',
                                color = 'white',
                                showline = True,
                                showgrid = True,
                                showticklabels = True,
                                linecolor = 'white',
                                linewidth = 2,
                                ticks = 'outside',
                                tickfont = dict(
                                    family = 'Arial',
                                    size = 12,
                                    color = 'white'
                                )
                                ),
                    legend = {
                        'orientation': 'h',
                        'bgcolor': '#010915',
                        'xanchor': 'center', 'x': 0.5, 'y': -0.3
                        },
                    font = dict(
                    family = "sans-serif",
                    size = 12,
                    color = 'white'
                    ),
                )

    }
    return return_var

@callback(
    Output('output1-heading', 'children'),
    [Input('bowler_name_id', 'value')]
)
def bowler_relation(bowlerName):
    df1 = df.query(f"bowler == '{bowlerName}'").reset_index()
    condition = "not (dismissal_kind == 'retired_hurt' or dismissal_kind == 'run out' or dismissal_kind.isna())"
    dataBowler = df1.query(condition)  
    dataBowler.loc[:, 'Wicket'] = 1
    tmp = dataBowler.groupby('batsman')['Wicket'].sum().reset_index()
    index = tmp['Wicket'].idxmax()
    max_wicket_row = tmp.loc[index]

    #strike rate
    batsmanName = max_wicket_row['batsman']
    temp = df1.query(f"batsman == '{batsmanName}'").reset_index()
    totalRun = temp['total_runs'].sum()
    totalBall = temp.shape[0]
    
    input_text = f"{bowlerName} has taken wicket of {max_wicket_row['batsman']} wicket, about {max_wicket_row['Wicket']} times and with strike rate of {round((totalRun*100)/totalBall,2)} and runs {totalRun}"

    return html.H2(input_text)
