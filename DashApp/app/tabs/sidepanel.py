import dash
import plotly
import dash_core_components as dcc
import dash_html_components as html 
import dash_bootstrap_components as dbc 
import dash_table
import pandas
from dash.dependencies import Input, Output

from app import app

from database import transforms

from datetime import date

df1 = transforms.df1
min_h=df1.Hora.min()
max_h=df1.Hora.max()

columnas = ['Terminal 1', 'Terminal 2', 'Terminal 3',
            'Terminal 4', 'Terminal 5', 'Terminal 6']

layout = html.Div([
    html.H1('Wine Dash')
    ,dbc.Row([dbc.Col(
        html.Div([
         html.H2('Filters')
        ,html.Div([html.P()
                ,html.H5('Horas')
                ,html.Div(id='output-container-Horas')                        
                ,dcc.RangeSlider(id='Horas'
                            ,min = 0
                            ,max= 24
                            ,value = [0,24]
                            ,marks={
                                0: '0',
                                4: '4',
                                8: '8',
                                12: '12',
                                16: '16',
                                20: '20',
                                24: '24'}
                            )
                            ])
        ,html.Div([html.H5('Rango de fechas'),
            dcc.DatePickerRange(
                id='my-date-picker-range',
                min_date_allowed=date(2020, 11, 5),
                max_date_allowed=date(2021, 12, 31),
                initial_visible_month=date.today()
            ),
            html.Div(id='output-container-date-picker-range')
        ])
        ,html.Div([html.P()
            ,html.H5('Puntos')
            , dcc.Dropdown(id = 'Sitios'
                        ,options=[
                             {'label': i, 'value': i} for i in columnas
                        ],
                        value=[],
                        multi=True
                    )  
        ])
        ,html.Div([html.P()
            ,html.H5('Columnas')
            , dcc.Dropdown(id = 'Registros'
                        ,options=[
                             {'label': i, 'value': i} for i in ['Dia','Mes','Año','Hora','Minuto']
                        ],
                        value=['Dia','Mes','Año','Hora','Minuto'],
                        multi=True
                    )  
        ])

        ], style={'marginBottom': 50, 'marginTop': 25, 'marginLeft':15, 'marginRight':15}
        )#end div
    , width=3) # End col

    ,dbc.Col(html.Div([
            dcc.Tabs(id="tabs", value='tab-4', children=[
                    dcc.Tab(label='Tabla Registros', value='tab-4'),
                    dcc.Tab(label='Scatter Plot', value='tab-2'),
                    dcc.Tab(label='Heatmap Plot', value='tab-3'),
                    
                ])
            , html.Div(id='tabs-content')
        ]), width=9)
        ]) #end row
    
    ])#end div

@app.callback(
    dash.dependencies.Output('output-container-Horas', 'children'),
    [dash.dependencies.Input('Horas', 'value')])
def update_output(value):
    return 'Entre {} y {}'.format(value[0],value[1])