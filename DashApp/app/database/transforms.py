import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import sqlite3
import dash
from dash.dependencies import Input, Output
import dash_table
import json

firebase={
    "10-01-2020 10:30": {"Terminal 1":201, "Terminal 2":206, "Terminal 3":212, "Terminal 4":212, "Terminal 5":206, "Terminal 6":212},
    "10-24-2020 10:35": {"Terminal 1":205, "Terminal 2":200, "Terminal 3":217, "Terminal 4":216, "Terminal 5":200, "Terminal 6":217},
    "11-23-2020 10:40": {"Terminal 1":209, "Terminal 2":204, "Terminal 3":217, "Terminal 4":246, "Terminal 5":196, "Terminal 6":217},
    "10-27-2020 10:45": {"Terminal 1":202, "Terminal 2":204, "Terminal 3":212, "Terminal 4":243, "Terminal 5":196, "Terminal 6":212},
    "11-21-2020 10:50": {"Terminal 1":205, "Terminal 2":205, "Terminal 3":213, "Terminal 4":215, "Terminal 5":194, "Terminal 6":213},
    "11-12-2020 10:55": {"Terminal 1":202, "Terminal 2":202, "Terminal 3":213, "Terminal 4":220, "Terminal 5":193, "Terminal 6":213},
    "10-23-2020 11:00": {"Terminal 1":201, "Terminal 2":204, "Terminal 3":216, "Terminal 4":216, "Terminal 5":195, "Terminal 6":216},   
    "10-24-2020 11:05": {"Terminal 1":201, "Terminal 2":204, "Terminal 3":216, "Terminal 4":212, "Terminal 5":192, "Terminal 6":216},   
    "10-15-2020 11:10": {"Terminal 1":201, "Terminal 2":204, "Terminal 3":216, "Terminal 4":202, "Terminal 5":192, "Terminal 6":216},   
    "11-04-2020 11:15": {"Terminal 1":201, "Terminal 2":204, "Terminal 3":216, "Terminal 4":190, "Terminal 5":190, "Terminal 6":216},   
    "10-02-2020 11:20": {"Terminal 1":201, "Terminal 2":204, "Terminal 3":216, "Terminal 4":192, "Terminal 5":187, "Terminal 6":216},   
    "11-20-2020 12:20": {"Terminal 1":201, "Terminal 2":204, "Terminal 3":216, "Terminal 4":196, "Terminal 5":188, "Terminal 6":216},   
    "10-14-2020 13:20": {"Terminal 1":201, "Terminal 2":204, "Terminal 3":216, "Terminal 4":180, "Terminal 5":193, "Terminal 6":216},   
    "11-18-2020 14:20": {"Terminal 1":201, "Terminal 2":204, "Terminal 3":216, "Terminal 4":185, "Terminal 5":192, "Terminal 6":216},   
    "10-10-2020 15:20": {"Terminal 1":201, "Terminal 2":204, "Terminal 3":216, "Terminal 4":176, "Terminal 5":197, "Terminal 6":216},   
}
firebase=json.dumps(firebase)
df1 = pd.read_json(firebase, orient='index')
def Fecha(row):
    return row.name
def Anho(row):
    return row.name.strftime('%Y')
def Dia(row):
    return row.name.strftime('%d')
def Mes(row):
    return row.name.strftime('%m')
def Hora(row):
    return float(row.name.strftime('%H'))
def Minuto(row):
    return float(row.name.strftime('%M'))
df1['Fecha'] = df1.apply(Fecha, axis=1)
df1['Hora'] = df1.apply(Hora, axis=1)
df1['Minuto'] = df1.apply(Minuto, axis=1)
df1['Dia'] = df1.apply(Dia, axis=1)
df1['Mes'] = df1.apply(Mes, axis=1)
df1['Año'] = df1.apply(Anho, axis=1)

df1 = df1[['Año','Mes','Dia','Minuto','Fecha','Hora','Terminal 1','Terminal 2','Terminal 3','Terminal 4','Terminal 5','Terminal 6']]
df1 = df1.sort_values(by=['Fecha'])
