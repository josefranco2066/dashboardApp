import dash
import plotly
import dash_core_components as dcc
import dash_html_components as html 
import dash_table
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc

import pandas as pd

from app import app
from tabs import sidepanel, tab2, tab3, tab4, navbar
from database import transforms
from datetime import date

columnas = ['Terminal1', 'Terminal2', 'Terminal3',
            'Terminal4', 'Terminal5', 'Terminal6']

app.layout = html.Div([navbar.Navbar(), sidepanel.layout])

@app.callback(Output('tabs-content', 'children'),
              [Input('tabs', 'value')])
def render_content(tab):
    if tab == 'tab-2':
       return tab2.layout
    elif tab == 'tab-3':
       return tab3.layout
    elif tab == 'tab-4':
       return tab4.layout


@app.callback([
    Output('table-sorting-filtering', 'data')
    , Output('table-sorting-filtering', "columns")]
    , [Input('table-sorting-filtering', "page_current")
     , Input('table-sorting-filtering', "page_size")
     , Input('Horas', 'value')
     , Input('my-date-picker-range', 'start_date')
     , Input('my-date-picker-range', 'end_date')
     , Input('Sitios', 'value')
     , Input('Registros', 'value')])
def update_table(page_current, page_size, horas, fechaInicio, fechaFin, sitios, registros):
    dff1 = transforms.update()
    page = page_current
    size = page_size

    #fecha filtro
    if fechaInicio is not None and fechaFin is not None:        
        dff1 = dff1.loc[(dff1['Fecha'] >= pd.to_datetime(fechaInicio)) & (dff1['Fecha'] <= pd.to_datetime(fechaFin))]
    elif fechaInicio is not None:
        dff1 = dff1.loc[dff1['Fecha'] >= pd.to_datetime(fechaInicio)]
    elif fechaFin is not None:
        dff1 = dff1.loc[dff1['Fecha'] <= pd.to_datetime(fechaFin)]

    # Horas filtro
    low = horas[0]
    high = horas[1]

    dff1 = dff1.loc[(dff1['Hora'] >= low) & (dff1['Hora'] <= high)]

    newColumns=[]
    newColumns.extend([{'name': i, 'id': i, 'deletable': False} for i in registros])
    if len(sitios)==0:
        for i in columnas:
            newColumns.append({'name': i, 'id': i, 'deletable': False})
        newColumns.append({'name': 'Fecha', 'id': 'Fecha', 'deletable': False})
    else:
        for i in sitios:
            newColumns.append({'name': i, 'id': i, 'deletable': False})
        newColumns.append({'name': 'Fecha', 'id': 'Fecha', 'deletable': False})

    return [dff1.iloc[page * size: (page + 1) * size].to_dict('records'),newColumns]

if __name__ == '__main__':
    app.run_server(host = '0.0.0.0',port=8050)