'''
Study Streamlit - Input Widgets with sidebar and columns
'''
import streamlit as st
import pandas as pd
import time


def feedback_message (message):
    message = ':blue'+ message
    st.toast(message)

# Title
st.set_page_config(page_title='Spotify Songs',
                   layout='wide')

# Read data from csv
df = pd.read_csv('01 Spotify.csv')

# Show data as chart - Charts elements - Line chart
df.set_index('Track', inplace=True)

# Input Widget - Widgets element = Selectbox - Using Sidebar
artists = df['Artist'].value_counts().index
artist = st.sidebar.selectbox('Select Artist', artists)
df_filtered = df[df['Artist'] == artist]

albuns = df_filtered['Album'].value_counts().index
album = st.sidebar.selectbox('Select Album', albuns)
df_filtered_album = df[df['Album'] == album]


# Input Widget - Widgets element = Checkbox
agree = st.checkbox('Show raw data')

# Using columns
col1, col2 = st.columns([0.7,0.3])

if agree:
    # Show Charts elements - Bar chart
    st.button(key = 'Barchart_btn',
              label=':rainbow[Click me] :left_speech_bubble:', 
              help='Click me to show raw data',
              on_click = feedback_message,
              args = ('Raw data',))
    col1.subheader('Bar chart')
    col1.bar_chart(df_filtered_album['Stream'])
    col2.subheader('Line chart')
    col2.line_chart(df_filtered_album['Danceability'])


st.write(artist + ' songs with more than 1 billion streams')

