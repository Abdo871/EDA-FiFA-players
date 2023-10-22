
import streamlit as st
import pandas as pd
import plotly.express as px

fifa = pd.read_csv('fifa_eda.csv')
quant_features = fifa.select_dtypes(include=['int64', 'float64']).columns
qualt_features = fifa.select_dtypes(include=['object']).columns

st.title('FIFA 2019')
st.markdown('''
This app performs simple EDA on FIFA 2019 data
''')
st.sidebar.header('User Input Features')
selected_column = st.sidebar.selectbox('Quantitative Features', fifa.columns)
st.header('Distribution of {}'.format(selected_column))
st.dataframe(fifa[selected_column].describe())
if fifa[selected_column].dtype == 'O':
    st.bar_chart(fifa[selected_column].value_counts())
else:
    st.bar_chart(fifa[selected_column])
st.plotly_chart(px.histogram(fifa, x=selected_column))

