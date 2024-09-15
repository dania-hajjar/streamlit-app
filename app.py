import streamlit as st
import plotly.express as px
import pandas as pd
import plotly as pt 


st.title('Data Visualization & Communication')
st.write('This is a web app to show visualizations made on plotly.')
st.write('In this web app we have 3 different visualizations in which two of them have interactive features to make this experience fun!')


#plot

file_path = 'https://linked.aub.edu.lb/pkgcube/data/4a0321bc971cc2f793d3367fd0b55a34_20240905_102823.csv'
df = pd.read_csv(file_path)

st.title("COVID-19 Cases by Area in Lebanon")
st.write("Below there's a table representing the areas and their corresponding COVID-19 cases.")

with st.expander("COVID-19 Cases Data"):
    st.write(df)

bar_chart = px.bar(df, x='refArea', y='Nb of Covid-19 cases', 
                   title='Number of COVID-19 Cases by Area',
                   labels={'Nb of Covid-19 cases': 'COVID-19 Cases', 'refArea': 'Area'},
                   color='Nb of Covid-19 cases')

st.plotly_chart(bar_chart)


#new plot


url = 'https://linked.aub.edu.lb/pkgcube/data/4a0321bc971cc2f793d3367fd0b55a34_20240905_102823.csv'
df = pd.read_csv(url)

st.title("comparison of COVID-19 Cases by Area")
st.write("below you can compare the percentage of covid-19 cases between any two ares of your choice")
areas = df['refArea'].unique()

selected_areas = st.multiselect("Select two areas to compare:", areas, default=[areas[0], areas[1]])

if len(selected_areas) == 2:
    
    filtered_df = df[df['refArea'].isin(selected_areas)]

    
    pie_chart = px.pie(filtered_df, values='Nb of Covid-19 cases', names='refArea', 
                       title='Comparison of COVID-19 Cases')


    st.plotly_chart(pie_chart)
else:
    st.warning("Please select exactly two areas to compare.")

    
    
    #new plot 

url = 'https://linked.aub.edu.lb/pkgcube/data/4a0321bc971cc2f793d3367fd0b55a34_20240905_102823.csv'
df = pd.read_csv(url)

st.title('COVID-19 Cases Analysis out of National Total')
st.write("Below you can build your own line chart that shows the percentages of COVID-19 cases out of national total belonging to areas of your choice.")
st.write("i have added the possibility for users to switch between each part of the chart's visibility for a better interactive experience")

areas = df['refArea'].unique()
selected_areas = st.multiselect('Select Areas:', areas, default=areas, key='area_selection')
filtered_df = df[df['refArea'].isin(selected_areas)]
line_chart = px.line(
    filtered_df,
    x='refArea',
    y='Percentage of cases out of national total ',
    title='Percentage of Cases out of National Total by Area',
    labels={
        'Percentage of cases out of national total ': '% of Total Cases',
        'refArea': 'Area'
    },
    markers=True  
)
line_chart.update_traces(selector=dict(mode='lines+markers'), hoverinfo='text')
st.plotly_chart(line_chart, use_container_width=True)