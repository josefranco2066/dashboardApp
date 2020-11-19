import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd

from app import app 
from database import transforms

df = transforms.df1

layout = html.Div(
            id='bar-promedio',
            className="five columns"
        )
@app.callback(
    Output("bar-promedio", "children"),
    [Input('Horas', 'value'),
    Input('Sitios', 'value')])
def update_figure(horas,columns):
    dff1 = df

    low = horas[0]
    high = horas[1]

    dff1 = dff1.loc[(dff1['Hora'] >= low) & (dff1['Hora'] <= high)]
    if len(columns) == 0:
        columns=['Terminal1', 'Terminal2', 'Terminal3','Terminal4', 'Terminal5', 'Terminal6']
    fig = go.Figure(go.Bar(
        x=columns,
        y=[sum(dff1[c])/float(len(dff1[c])) for c in columns]
    ))
    fig.update_layout(title='Promedio',
                   xaxis_title='Ubicacion',
                   yaxis_title='ICA promedio')
    return html.Div([
        dcc.Graph(
            id='promedio'
            , figure=fig
        )
    ])