import dash
from dash import html, dcc, Dash, callback
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go

dash.register_page(__name__)

df = pd.read_csv("csvFiles/deliveries.csv")
data = df.groupby('batsman')['batsman_runs'].sum().reset_index()
allBatsmanName = data['batsman'].unique().tolist()

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

layout = html.Div([
    html.Div([html.H1("Batsman runs per year")]),
    html.Div(id='output-heading'),
    html.Div([html.Div([
            # batsman dropdown
            html.P('Select Batsman:', className = 'fix_label', style = {'color': 'white'}),
            dcc.Dropdown(id = 'batsman_name_id',
                         multi = False,
                         clearable = True,
                         disabled = False,
                         style = {'display': True},
                         value = 'V Kohli',
                         placeholder = 'Select Batsman Name',
                         options = [{'label': c, 'value': c}
                                    for c in allBatsmanName], className = 'dcc_compon'),
            #years slider 
            html.P('Select Year:', className = 'fix_label', style = {'color': 'white', 'margin-left': '1%'}),
            dcc.RangeSlider(id = 'select_years',
                            min = 2008,
                            max = 2017,
                            step=1,
                            marks={year: str(year) for year in range(2008, 2018)},
                            value = [2008, 2017]),
                            

        ], className = "create_container three columns"),

        #histogram div
        html.Div([
            dcc.Graph(id = 'bar_line_1',
                      config = {'displayModeBar': 'hover'}),

        ], className = "create_container three columns"),

    ], className = "row flex-display")
])

#create histogram callback
@callback(
            Output('bar_line_1', 'figure'),
            [Input('batsman_name_id', 'value')],
            [Input('select_years', 'value')]
        )
def update_histogram_graph(batsman_name, selected_years):
    result = []
    years = []
    avg  = []
    start_year = selected_years[0]
    end_year = selected_years[1]
    while(start_year <= end_year):
        tmp = data_dict[start_year]
        temp = tmp.loc[tmp['batsman'] == batsman_name]
        tmp_matches = df_dict[start_year]
        tmp1_matches = tmp_matches.query(f"batsman == '{batsman_name}'")
        matches_list = tmp1_matches['match_id'].unique()
        temp_run_list = temp['batsman_runs'].tolist()
        if temp_run_list:
            result.append(temp_run_list[-1])
            if len(matches_list):
                avg.append(temp_run_list[-1]/len(matches_list))
                # print(f"matches: {len(matches_list)}")
            else:
                avg.append(0)
            years.append(start_year)
        start_year += 1


    return {
        'data': [go.Bar(x = years,
                        y = result,
                        text = result,
                        texttemplate = '%{text:.2s}',
                        textposition = 'auto',
                        textfont = dict(
                            color = 'white'
                        ),
                        name = 'Runs by '+str(batsman_name),
                        marker = dict(color = '#9C0C38'),
                        hoverinfo = 'text',
                        hovertext =
                        '<b>Year</b>: ' + str(selected_years[0])+ '-'+ str(selected_years[1]) + '<br>' +
                        '<b>Batsman</b>: ' + batsman_name + '<br>'
                    ),
                go.Bar(
                     x = years,
                     y = avg,
                     text = avg,
                     texttemplate = '%{text:.2s}',
                     textposition = 'auto',
                     name = 'Average by '+str(batsman_name),

                     marker = dict(color = 'orange'),

                     hoverinfo = 'text',
                     hovertext =
                            '<b>Batsman</b>: ' + batsman_name + '<br>' +
                            '<b>Year</b>: ' + str(selected_years[0]) + '-' + str(selected_years[1]) + '<br>' +
                            '<b>Average</b>: ' + ', '.join([f'{x:,.0f}' for x in avg]) + '<br>'

                 ),
                ],

        'layout': go.Layout(
                    barmode = 'overlay',
                    plot_bgcolor = '#010915',
                    paper_bgcolor = '#010915',
                    title = {
                        'text': 'Batting Performance : ' + (batsman_name) + '  ' + '<br>' + ' - '.join( [str(y) for y in years]) + '</br>',
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

                    yaxis = dict(title = '<b>Runs by '+ batsman_name+'</b>',
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

@callback(
    Output('output-heading', 'children'),
    [Input('batsman_name_id', 'value')]
)
def batsman_bowler_relation(batsmanName):
    df1 = df.query(f"batsman == '{batsmanName}'").reset_index()
    temp = df1.groupby('bowler')['total_runs'].sum().reset_index()
    index = temp['total_runs'].idxmax()
    max_run_row = temp.loc[index]

    df1.loc[:,'balls'] = 1

    temp1 = df1.groupby('bowler')['balls'].sum().reset_index()
    index_ball = temp1['balls'].idxmax()
    max_ball_row = temp1.loc[index_ball]

    # strike rate
    totalRun = df1['total_runs'].sum()
    totalBall = df1.shape[0]

    input_text = f"{batsmanName} played {max_ball_row['bowler']}, {max_ball_row['balls']} balls exact and made most runs of {max_run_row['bowler']}, {max_run_row['total_runs']} runs exact and {batsmanName} has strike rate of {round((totalRun*100)/totalBall,2)}"
    return html.H2(input_text)

