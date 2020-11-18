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

columnas=['Terminal 1', 'Terminal 2', 'Terminal 3','Terminal 4', 'Terminal 5', 'Terminal 6']
campos=['{Terminal 1}', '{Terminal 2}', '{Terminal 3}','{Terminal 4}', '{Terminal 5}', '{Terminal 6}']

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
            'Terminal 1':{'value': 'Terminal 1 \n\n Fecha: {} \n\n Hora: {}:{}'.format(row['Fecha'],row['Hora'],row['Minuto']), 'type': 'markdown'},
            'Terminal 2':{'value': 'Terminal 2 \n\n Fecha: {} \n\n Hora: {}:{}'.format(row['Fecha'],row['Hora'],row['Minuto']), 'type': 'markdown'},
            'Terminal 3':{'value': 'Terminal 3 \n\n Fecha: {} \n\n Hora: {}:{}'.format(row['Fecha'],row['Hora'],row['Minuto']), 'type': 'markdown'},
            'Terminal 4':{'value': 'Terminal 4 \n\n Fecha: {} \n\n Hora: {}:{}'.format(row['Fecha'],row['Hora'],row['Minuto']), 'type': 'markdown'},
            'Terminal 5':{'value': 'Terminal 5 \n\n Fecha: {} \n\n Hora: {}:{}'.format(row['Fecha'],row['Hora'],row['Minuto']), 'type': 'markdown'},
            'Terminal 6':{'value': 'Terminal 6 \n\n Fecha: {} \n\n Hora: {}:{}'.format(row['Fecha'],row['Hora'],row['Minuto']), 'type': 'markdown'},
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
