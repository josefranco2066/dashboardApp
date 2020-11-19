import random
from datetime import datetime
import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate('firebase-sdk.json')
firebase_admin.initialize_app(cred)

db = firestore.client()
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