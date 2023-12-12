'''
Study Streamlit - Spotify with checkbox and selectbox nested 
'''
import streamlit as st
import pandas as pd


# Title
st.set_page_config(page_title='Spotify Songs',
                   layout='wide')

# Read data from csv
df = pd.read_csv('01 Spotify.csv')

# Show data as chart - Charts elements - Line chart
df.set_index('Track', inplace=True)

# Input Widget - Widgets element = Selectbox
artists = df['Artist'].value_counts().index
artist = st.selectbox('Select Artist', artists)
df_filtered = df[df['Artist'] == artist]

albuns = df_filtered['Album'].value_counts().index
album = st.selectbox('Select Album', albuns)
df_filtered_album = df[df['Album'] == album]


# Input Widget - Widgets element = Checkbox
agree = st.checkbox('Show raw data')

if agree:
    # Show Charts elements - Bar chart
    st.bar_chart(df_filtered_album['Stream'])

st.write(artist + ' songs with more than 1 billion streams')

