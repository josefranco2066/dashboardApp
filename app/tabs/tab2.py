import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc 
import pandas as pd
import plotly.graph_objs as go
from dash.dependencies import Input, Output
import dash_table
from app import app
from database import transforms

df = transforms.update()

layout = html.Div(
            id='table-paging-with-graph-container',
            className="five columns"
        )

@app.callback(
    Output('table-paging-with-graph-container', "children"),
    [Input('Horas', 'value'),
    Input('Sitios', 'value')])
def update_graph(horas,columns):
    dff1 = transforms.update()

    low = horas[0]
    high = horas[1]

    dff1 = dff1.loc[(dff1['Hora'] >= low) & (dff1['Hora'] <= high)]
    fig = go.Figure()
    if len(columns) == 0:
        columns=['Terminal1', 'Terminal2', 'Terminal3','Terminal4', 'Terminal5', 'Terminal6']
    for c in columns:
        fig.add_trace(go.Scatter(x = dff1['Fecha']
                            , y = dff1[c]
                            , mode='lines'
                            , opacity=0.7
                            , marker={
                                    'size': 8
                                    , 'line': {'width': 0.5, 'color': 'blue'}
                                    }
                            , name=c
                            , connectgaps=True
                        ))
    fig.update_layout(title='Ica vs tiempo',
                   xaxis_title='Fecha',
                   yaxis_title='ICA')
    return html.Div([
        dcc.Graph(
            id='rating-price'
            , figure=fig
        )
    ])
