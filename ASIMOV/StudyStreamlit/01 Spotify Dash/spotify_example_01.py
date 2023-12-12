'''
Study Streamlit - Spotify Dashboard
Use the bar chat to see the number of streams of the songs with more than 1 billion streams. 

'''

import streamlit as st
import pandas as pd


# Read data from csv
df = pd.read_csv('01 Spotify.csv')

# Input Widget - Widgets elements 
# Input text
df.set_index('Track', inplace=True)
st.bar_chart(df[df['Stream'] > 1000000000]['Stream'])


# Show data as table - Data elements - Dataframe functions - Write data = Simple DataFrame
st.write(df[df['Stream'] > 1000000000])
