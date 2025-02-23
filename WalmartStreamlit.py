#----------Import Packages----------#
import pandas as pd 
import streamlit as st 
import plotly.express as px

# set page size
st.set_page_config(layout='wide')

#----------Import Data----------#
#import data
df = pd.read_csv('/Users/alexziegler/Downloads/Walmart_Sales.csv')


#----------Initial Data Wrangling----------#

# Transform order date to a datetime and fix the datetime formatting issues
df['Date'] = pd.to_datetime(df['Date'], format='mixed')


# Add Year, Month, Day to dataframe
df['Year']= df['Date'].dt.year
df['Month']= df['Date'].dt.month
df['Day']= df['Date'].dt.day


# Drop non essential columns


# Divide the columns into keep and drop
columns_to_keep = ['Store', 'Date', 'Weekly_Sales','Year','Day', 'Month']
columns_to_drop = ['Holiday_Flag', 'Temperature', 'Fuel_Price', 'CPI','Unemployment']

# Save refined dataframe
df = df[columns_to_keep]



#----------Create Streamlit App----------#



#create a title
st.title('Walmart Sales Dashboard')
st.divider()

# add in columns formatting
col1, col2 = st.columns([1,1])

#st.dataframe(df)

#-----Data Selector-----#
#grab unique store, month, year
store = df['Store'].unique()
year = df['Year'].unique()




#assign selected store, month, year to a variable
year_selected = col1.selectbox('Select Year', year)
store_selected = col2.selectbox('Select Store', store)


#-----Data Filtering-----#
#filter data based on selected store, month, year
selected_store_df = df[df['Store'] == store_selected]
selected_year_df = df[df['Year'] == year_selected]




#create dataframe with summed sales for each store
df_summed_store = selected_store_df.groupby('Store').agg({'Weekly_Sales': 'sum'}).reset_index()
df_summed_store['Store Average Sales'] = round(df_summed_store['Weekly_Sales'] /36, 0)

#create dataframe with summed sales for year
df_summed_year = selected_year_df.groupby('Year').agg({'Weekly_Sales': 'sum'}).reset_index()
df_summed_year['Store Yearly Sales'] = round(df_summed_year['Weekly_Sales'] /3, 0)






#-----Metrics-----#
#create subheader and columns
st.subheader('Main Metrics', divider='blue')

# Create a container to add a border
with st.container(border= True):
    col1, col2, col3 = st.columns(3)


# metrics showing: total sales, average store sales, and store
col1.metric('Store Number', "{:.0f}".format(df_summed_store['Store'].values[0]))
col2.metric('Total Sales', '${:,.2f}'.format(df_summed_store['Weekly_Sales'].values[0]))
col3.metric('Store Average Sales', '${:,.0f}'.format(df_summed_store['Store Average Sales'].values[0]))



st.header("") #for spacing purposes

#-----Graphs-----#
#create subheader and tabs
st.subheader('Graphs', divider='blue')
tab1, tab2 = st.tabs([' Store Sales', 'Yearly Sales'])



#sum sales by store and build tab1 bar graphs
df_by_store = selected_year_df.groupby('Store')['Weekly_Sales'].sum().reset_index()
with tab1:
    fig = px.bar(df_by_store, x = 'Store', y = 'Weekly_Sales') 
    fig.update_layout(xaxis_title= 'Store', yaxis_title= 'Sales') 
    fig.update_layout(xaxis_tickformat='d')
    st.plotly_chart(fig, use_container_width=True)  


#sum sales by year and build tab2 bar graphs
df_by_year = df.groupby('Year')['Weekly_Sales'].sum().reset_index()
with tab2:
    fig2 = px.bar(df_by_year, x = 'Year', y = 'Weekly_Sales')
    fig2.update_layout(xaxis_title= 'Year', yaxis_title= 'Sales')
    fig2.update_layout(xaxis_tickformat='d', hoverlabel=dict(namelength=-1))
    st.plotly_chart(fig2, use_container_width=True)

