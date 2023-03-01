import streamlit as st
import pandas as pd
import plotly_express as px

df = pd.read_csv("vehicles_us.csv")

st.header("""
   Vehicle US
""")

model_year_median = df.groupby('model')['model_year'].median()
df['model_year'] = df.apply(lambda row: model_year_median[row['model']] if pd.isna(row['model_year']) else row['model_year'], axis=1)
#fill model_year with median filling

odometer_mean = df.groupby('model_year')['odometer'].mean()
df['odometer'] = df.apply(lambda row: odometer_mean[row['model_year']] if pd.isna(row['odometer']) else row['odometer'], axis=1)
#fill odometer with mean filling

cylinders_median = df.groupby('model')['cylinders'].median()
df['cylinders'] = df.apply(lambda row: cylinders_median[row['model']] if pd.isna(row['cylinders']) else row['cylinders'], axis=1)
#fill cylinders with median filling


df['paint_color'].fillna('no info', inplace=True)
#fill paint_color with no info
df['is_4wd'].fillna(0, inplace=True)
#fill is_4wd by 0


show_model = st.checkbox('model')
if not show_model:
    df = df[df.model!='model']
model = df['model'].unique()
make_choice = st.selectbox('model:',model)
min_year, max_year=int(df['model_year'].min()), int(df['model_year'].max())

year_range = st.slider(
     "Choose years",
     value=(min_year,max_year),min_value=min_year,max_value=max_year )
st.markdown('<font color=red>creating slider  min and max years as limits for sliders</font>', unsafe_allow_html=True)

filtered_type=df[(df.model==make_choice)&(df.model_year.isin(list(year_range)))]
st.table(filtered_type)

#---------------------------------------------
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
hist_list =['transmission', 'condition', 'fuel', 'type', 'paint_color']
hist_choice = st.selectbox('Split for price distribution', hist_list)
hist = px.histogram(df, x='price', color=hist_choice, nbins=20)
hist.update_layout(title="<b> Split of price by {}</b>".format(hist_choice))
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

st.markdown('<font color=blue>conclusions creating and managing python virtual environments, developing a web application, and deploying it to a cloud service and make it accessible to the public</font>', unsafe_allow_html=True)
st.markdown('<font color=blue>the target to achieve web app accessible via a browser, and can be visualize more easier with check box the graph, compare the graph model and transmission</font>', unsafe_allow_html=True)

