#Anibal Jose Angulo Cardoza
#A01654684

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

ny_lat_lon = [40.730610,-73.935242]
apptitle = 'Mapa sobre viajes en uber para NY'
descrip = 'En esta WebApp se pueden visualizar los viajes de uber en New York por hora.'

@st.cache
def load_d(nrows):
    dset_rute = 'https://s3-us-west-2.amazonaws.com/streamlit-demo-data/uber-raw-data-sep14.csv.gz'
    data_Uber = pd.read_csv(dset_rute,nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data_Uber.rename(lowercase, axis='columns', inplace=True)
    data_Uber['date/time'] = pd.to_datetime(data_Uber['date/time'])
    return data_Uber

st.title(apptitle)
st.header(descrip)
st.markdown('___')
data_Uber = load_d(1000)
data_UberC = data_Uber.copy()

optionals = st.expander('Optional config',True)
horFil = optionals.slider(
    'Hora del dia',
    min_value= int(data_Uber['date/time'].dt.hour.min()),
    max_value= int(data_Uber['date/time'].dt.hour.max())

)
data_vis = data_UberC[(data_UberC['date/time'].dt.hour == horFil)]
st.header(f'Mapa de recogias de Uber a las {horFil}:00 horas')
st.map(data_vis)

if st.checkbox('Visualizar Dataset?'):
    st.dataframe(data_vis)
