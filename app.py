import streamlit as st
import pandas as pd
import plotly_express as px

df = pd.read_csv("vehicles_us.csv")

df = df.dropna()

#df = df.astype({'model_year': int, 'odometer': int, 'cylinder': int, 'is_4wd': int})

st.header("""
   Vehicle US
""")

#filter
st.sidebar.header("Filter Data")
selected_category = st.sidebar.selectbox("Select category". df["model"].unique())

filterred_df = df[df["model"] == selected_category]

fig = px.scatter(filtered_df, x="model_year", y="price", color="type")
fig.update_layout(title="price vs Model_year Graph")
st.plotly_chart(fig)

#histogram
hist = px.histogram(df, x="transmission", nbins=20)
hist.update_layout(title="transmission Graph")
st.plotly_chart(hist)

#scatter plot with checkbox
x = "model_year"
y = "price"
color_type = "type"

def update_scatter_plot(x, y, color_type):
    scatter = px.scatter(df, x=x, y=y, color=color_type)
    scatter.update_layout(title="{} vs {}".format(y.capitalize(), x.capitalize()))
    st.plotly_chart(scatter)

checkbox = st.checkbox("Show data table")
if checkbox:
    y = st.selectbox("Select y axis column", df.columns)
    x = st.selectbox("Select x axis column", df.columns)
    color_type = st.selectbox("Select type column", df.columns)

update_scatter_plot(x, y, color_type)
