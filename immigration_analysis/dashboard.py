##-Running the dashboard-########
## open the terminal           ##
## cd immigration_analysis     ##
## streamlit run dashboard.py  ##
#################################

# libraries import
import streamlit as st
import pandas as pd
import os
import numpy as np
import plotly.express as px

# data loading
@st.cache_data
def load_data():
    df = pd.read_excel('data/Canada.xlsx', sheet_name=1,skiprows=20, skipfooter=2)
    # rename the columns
    df = df.rename(columns={'OdName': 'country', 'AreaName': 'continent', 'RegName': 'region', 'DevName': 'status'})
    # rename the values accordingly
    df = df.replace('United Kingdom of Great Britain and Northern Ireland','UK',)
    # drop unnecessary columns
    cols_to_drop = ['Type', 'Coverage', 'AREA', 'REG', 'DEV']
    df = df.drop(columns=cols_to_drop)
    # create a new column to display the total
    years = list(range(1980, 2014))
    df['total'] = df[years].sum(axis=1)
    # set country as index (optional & for this case only)
    df = df.set_index('country')
    return df # return the dataframe

# ui setup
st.set_page_config(
    page_icon="🌍",
    page_title="Immigration Analysis Dashboard",
    layout="wide",
    initial_sidebar_state='collapsed'
)
# calling ui functions
years = list(range(1980, 2014))

df = load_data()

st.title("Immigration Analysis Dashboard")
st.subheader("United Nations data on international migration")
c1, c2, c3, c4 = st.columns(4)
c1.write("Information for dummies")
c1.info('Select the years and countries to look at the immigration trend')
chosen_years = st.sidebar.multiselect('Select years', years, years, 
    help='Select the years to find immigration data')
chosen_countries = c2.multiselect('Select countries',df.index.tolist(),
    default=['India','China'],
    help='Select one or more country(ies)')
sort_order = c3.selectbox('Sort order', ['Ascending', 'Descending'])
graph = c4.selectbox('Graph type', ['Line', 'Bar', 'Area'])


# visualization
if chosen_years and chosen_countries:
    filtered_df = df.loc[chosen_countries, chosen_years]
    if sort_order == 'Ascending':
        filtered_df = filtered_df.sort_values(by=chosen_years, 
            ascending=True)
    else:
        filtered_df = filtered_df.sort_values(by=chosen_years, 
            ascending=False)
    with st.expander('View Data Frame'):
        st.dataframe(filtered_df)
    if graph == 'Bar':
        fig = px.bar(filtered_df.T, x=filtered_df.columns, y=filtered_df.index)
    elif graph == 'Line':
        fig = px.line(filtered_df.T, x=filtered_df.columns, y=filtered_df.index)
    elif graph == 'Area':
        fig = px.area(filtered_df.T, x=filtered_df.columns, y=filtered_df.index)
    st.plotly_chart(fig, use_container_width=True)

# grouping
st.subheader('Finding Unknown Facts')
c1, c2, c3,c4 = st.columns(4)
group = c2.selectbox('Group by', ['continent', 'region', 'status'])
agg = c3.selectbox('Aggregate', ['sum', 'mean', 'max', 'min', 'std'])

grouped_df = df.groupby(group)[years]
if agg == 'sum':
    grouped_df = grouped_df.sum()
elif agg == 'mean':
    grouped_df = grouped_df.mean()
elif agg == 'max':
    grouped_df = grouped_df.max()
elif agg == 'min':
    grouped_df = grouped_df.min()
elif agg == 'std':
    grouped_df = grouped_df.std()
with st.expander('View Grouped Data Frame'):
    st.dataframe(grouped_df)

# visualization
fig = px.bar(grouped_df.T, x=grouped_df.columns, y=grouped_df.index)
st.plotly_chart(fig, use_container_width=True)

# immigration comparison for status
c1, c2, c3 = st.columns(3)
c1.subheader('Immigration status')
status_series = df['status'].value_counts()
fig = px.pie(status_series, values=status_series.values, 
             names=status_series.index, hole=.7)
c1.plotly_chart(fig, use_container_width=True, )

c2.subheader('Immigration from continents')
status_series = df['continent'].value_counts()
fig = px.pie(status_series, values=status_series.values, 
             names=status_series.index, hole=.7)
c2.plotly_chart(fig, use_container_width=True, )

c3.subheader('Immigration from region')
status_series = df['region'].value_counts()
fig = px.pie(status_series, values=status_series.values, 
             names=status_series.index, hole=.7)
c3.plotly_chart(fig, use_container_width=True, )