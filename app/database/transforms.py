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
import random
from datetime import datetime
import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate('database/firebase-sdk.json')
firebase_admin.initialize_app(cred)

db = firestore.client()
# doc_ref = db.collection('Registros').document(id)

transaction = db.transaction()
doc_ref = db.collection('Registros')
# doc_ref = db.collection('Registros').document(u'11-19-2020 00:00')
# doc_ref.update({
#     'Terminal1':15
# })
docs = doc_ref.stream()
fire={}
for doc in docs:
    fire[doc.id]=doc.to_dict()
firebase=json.dumps(fire)
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

df1 = df1[['Año','Mes','Dia','Minuto','Fecha','Hora','Terminal1','Terminal2','Terminal3','Terminal4','Terminal5','Terminal6']]
df1 = df1.sort_values(by=['Fecha'])

def update():  
    docs = doc_ref.stream()
    fire={}
    for doc in docs:
        fire[doc.id]=doc.to_dict()
    firebase=json.dumps(fire)
    df1 = pd.read_json(firebase, orient='index')
    df1['Fecha'] = df1.apply(Fecha, axis=1)
    df1['Hora'] = df1.apply(Hora, axis=1)
    df1['Minuto'] = df1.apply(Minuto, axis=1)
    df1['Dia'] = df1.apply(Dia, axis=1)
    df1['Mes'] = df1.apply(Mes, axis=1)
    df1['Año'] = df1.apply(Anho, axis=1)

    df1 = df1[['Año','Mes','Dia','Minuto','Fecha','Hora','Terminal1','Terminal2','Terminal3','Terminal4','Terminal5','Terminal6']]
    return df1.sort_values(by=['Fecha'])
