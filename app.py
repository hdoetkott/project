import streamlit as st
import pandas as pd
import plotly_express as px

df = pd.read_csv("vehicles_us.csv")

st.header("""
   Vehicle US
""")

df = df.dropna()
st.markdown('<font color=red>found missing value</font>', unsafe_allow_html=True)

df1 = df.isnull().sum()
st.markdown('<font color=red>no missing value found in column model_year, paint_color, cylinders, is_4wd, odometer in the eda4project (1).ipynb</font>', unsafe_allow_html=True)

#df = df.astype({'model_year': int, 'odometer': int, 'cylinder': int, 'is_4wd': int})



#filter
st.sidebar.header("Filter Data")
selected_category = st.sidebar.selectbox("Select category", df["model"].unique())

filtered_df = df[df["model"] == selected_category]

fig = px.scatter(filtered_df, x="model_year", y="price", color="type")
fig.update_layout(title="price vs Model_year Graph")
st.plotly_chart(fig)
st.markdown('<font color=red>Filter scatter base on model_year and price</font>', unsafe_allow_html=True)
st.markdown('<font color=red>description with px plotting the scatter, with x model year and y for price and color for differences the type of the car, after build the scatter need to display with plotly chart</font>', unsafe_allow_html=True)

#histogram
hist = px.histogram(df, x="transmission", nbins=20)
hist.update_layout(title="transmission Graph")
st.plotly_chart(hist)
st.markdown('<font color=red>Filter histogram base on transmission</font>', unsafe_allow_html=True)
st.markdown('<font color=red>description with px plotting the histogram, with x transmission, after build the histogram need to display with plotly chart</font>', unsafe_allow_html=True)

st.markdown('<font color=red>checkbox scatter plot to active sellection</font>', unsafe_allow_html=True)
st.markdown('<font color=red>description with checkbox, to more easier with drop down to choose to display the graph, after build the scatter need to display with plotly chart</font>', unsafe_allow_html=True)


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

st.markdown('<font color=red>conclusions creating and managing python virtual environments, developing a web application, and deploying it to a cloud service and make it accessible to the public</font>', unsafe_allow_html=True)
st.markdown('<font color=red>the target to achieve web app accessible via a browser, and can be visualize more easier with check box the graph, compare the graph model and transmission</font>', unsafe_allow_html=True)

