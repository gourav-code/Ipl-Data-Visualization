import dash
from dash import html, dcc, Dash
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go


app = Dash(__name__, use_pages=True)

app.layout = html.Div([html.Div([
        html.Div(
            dcc.Link(f"{page['name']} - {page['path']}", href=page["relative_path"])
        ) for page in dash.page_registry.values()
        ]),
    dash.page_container
])

if __name__ == '__main__':
    app.run_server(debug = True, port=1998)