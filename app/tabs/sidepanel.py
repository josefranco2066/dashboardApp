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

columnas = ['Terminal1', 'Terminal2', 'Terminal3',
            'Terminal4', 'Terminal5', 'Terminal6']

layout = html.Div([
    html.H1('MIO Dash')
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
        ,html.Div([
            dbc.Button("Agregar datos",id="add-data", color="Danger", className="mr-1")
            ,html.Div(id='otro') 
        ])

        ], style={'marginBottom': 50, 'marginTop': 25, 'marginLeft':15, 'marginRight':15}
        )#end div
    , width=3) # End col

    ,dbc.Col(html.Div([
            dcc.Tabs(id="tabs", value='tab-4', children=[
                    dcc.Tab(label='Tabla Registros', value='tab-4'),
                    dcc.Tab(label='Grafico de lineas', value='tab-2'),
                    dcc.Tab(label='Grafico de barras', value='tab-3'),
                    
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

@app.callback(
    Output("otro", "children"), 
    [Input("add-data", "n_clicks")],prevent_initial_call=True
)
def on_button_click(n):
    from datetime import datetime
    from database.transforms import db
    from index import update_table
    import random
    hoy = datetime.today()
    id = '{m}-{d}-{y} {h}:{M}'.format(
        y=hoy.strftime('%Y'),
        m=hoy.strftime('%m'),
        d=hoy.strftime('%d'),
        h=hoy.strftime('%H'),
        M=hoy.strftime('%M')
        )
    doc_ref = db.collection('Registros').document(id)
    doc_ref.set({
        'Terminal1':random.randrange(10, 100),
        'Terminal2':random.randrange(50, 100),
        'Terminal3':random.randrange(80, 120),
        'Terminal4':random.randrange(90, 100),
        'Terminal5':random.randrange(10, 500),
        'Terminal6':random.randrange(250, 450),
    })
    return 'Enviados'
