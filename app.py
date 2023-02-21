import streamlit as st
import pandas as pd
import plotly_express as px

df = pd.read_csv("vehicles_us.csv")

df = df.dropna()

#df = df.astype({'model_year': int, 'odometer': int, 'cylinder': int, 'is_4wd': int})

st.header("""
   Vehicle US
""")

hist = px.histogram(df, x="transmission", nbins=20)
st.plotly_chart(hist)

x = "model_year"
y = "price"
color_type = "type"

def update_scatter_plot(x, y, color_type):
    scatter = px.scatter(df, x=x, y=y, color=color_type)
    st.plotly_chart(scatter)

checkbox = st.checkbox("Show data table")
if checkbox:
    x = st.selectbox("Select x axis column", df.columns)
    y = st.selectbox("Select y axis column", df.columns)
    color_type = st.selectbox("Select type column", df.columns)

update_scatter_plot(x, y, color_type)