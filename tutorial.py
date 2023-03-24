pip install plotly
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as plt


st.title('Uber Pickups in NYC')

date_column = 'date/time'
data_url = 'https://s3-us-west-2.amazonaws.com/streamlit-demo-data/uber-raw-data-sep14.csv.gz'

def load_data(nrows):
    data = pd.read_csv(data_url, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[date_column] = pd.to_datetime(data[date_column])
    return data

data = load_data(1000)

if st.checkbox('show raw data'):
    st.subheader('raw data')
    st.write(data)


st.subheader('number of pickups by hour')
st.plotly_chart(plt.histogram(data,data['date/time'].dt.hour))



hour_to_filter = st.slider('hour',0,23,17)
filtered_data = data[data['date/time'].dt.hour==hour_to_filter]
st.subheader(f'map of all pickups at {hour_to_filter}:00')
st.map(filtered_data)


