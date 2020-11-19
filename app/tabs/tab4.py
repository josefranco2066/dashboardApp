import dash
import plotly
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_table
import pandas as pd
from dash.dependencies import Input, Output

from app import app
from database import transforms

df = transforms.df1

columnas=['Terminal1', 'Terminal2', 'Terminal3','Terminal4', 'Terminal5', 'Terminal6']
campos=['{Terminal1}', '{Terminal2}', '{Terminal3}','{Terminal4}', '{Terminal5}', '{Terminal6}']

estilos=[]
estilos.extend([{'if': {
                'filter_query': '{i} <= 150'.format(i=campos[n]),
                'column_id': i,
            },
            'backgroundColor': 'green',
            'color': 'black'} for n,i in enumerate(columnas)])
estilos.extend([{'if': {
                'filter_query': '{i} > 150 && {i} < 400'.format(i=campos[n]),
                'column_id': i,
            },
            'backgroundColor': 'yellow',
            'color': 'black'} for n,i in enumerate(columnas)])
estilos.extend([{'if': {
                'filter_query': '{i} > 400'.format(i=campos[n]),
                'column_id': i,
            },
            'backgroundColor': 'red',
            'color': 'black'} for n,i in enumerate(columnas)])

PAGE_SIZE = 50
layout = html.Div(
    dash_table.DataTable(
        id='table-sorting-filtering',
        tooltip_data=[{
            'Terminal1':{'value': 'Terminal1 \n\n Fecha: {} \n\n Hora: {}:{}'.format(row['Fecha'],row['Hora'],row['Minuto']), 'type': 'markdown'},
            'Terminal2':{'value': 'Terminal2 \n\n Fecha: {} \n\n Hora: {}:{}'.format(row['Fecha'],row['Hora'],row['Minuto']), 'type': 'markdown'},
            'Terminal3':{'value': 'Terminal3 \n\n Fecha: {} \n\n Hora: {}:{}'.format(row['Fecha'],row['Hora'],row['Minuto']), 'type': 'markdown'},
            'Terminal4':{'value': 'Terminal4 \n\n Fecha: {} \n\n Hora: {}:{}'.format(row['Fecha'],row['Hora'],row['Minuto']), 'type': 'markdown'},
            'Terminal5':{'value': 'Terminal5 \n\n Fecha: {} \n\n Hora: {}:{}'.format(row['Fecha'],row['Hora'],row['Minuto']), 'type': 'markdown'},
            'Terminal6':{'value': 'Terminal6 \n\n Fecha: {} \n\n Hora: {}:{}'.format(row['Fecha'],row['Hora'],row['Minuto']), 'type': 'markdown'},
        } for row in df.to_dict('rows')],
        style_table={'height': '750px', 'overflowX': 'scroll'},
        style_cell={
            'height': '20',
            # all three widths are needed
            'minWidth': '20px', 'width': '50px', 'maxWidth': '70px', 'textAlign': 'center', 'whiteSpace': 'normal'
        }, 
        style_data_conditional=estilos,
        page_current=0,
        page_size=PAGE_SIZE,
        page_action='native',

        filter_action='native',

        sort_action='native',
        sort_mode='multi'
    )
)
