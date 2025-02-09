#%%
print("Hello World")

#%%
print(2+2)

#%%
print(f"Hello World did you know that 2+2 is {2+2}")

#%%
import plotly.express as px
import numpy as np
import pandas as pd


#%%
df = pd.read_csv('sales.csv')

# %%
#%%
# Line Plot
fig1 = px.line(df, x='Date', y='Sales', title='Sales Over Time')
fig1.show()

#%%
# Bar Chart
fig2 = px.bar(df, x='Date', y='Sales', title='Daily Sales')
fig2.show()

#%%
# Scatter Plot
fig3 = px.scatter(df, x='Date', y='Sales', title='Sales Scatter Plot')
fig3.show()

#%%
# Replicate the Line Chart using Graph Objects
import plotly.graph_objects as go

# Create a line chart with Graph Objects
fig_line_go = go.Figure()

# Add a trace for the line chart
fig_line_go.add_trace(go.Scatter(x=df['Month'], y=df['#Passengers'], mode='lines', name='Passengers'))

# Update layout for the line chart
fig_line_go.update_layout(title='Air Passengers Over Time', xaxis_title='Month', yaxis_title='Passengers')

# Show the line chart
fig_line_go.show()


#%%
# Replicate the Bar Chart using Graph Objects
# Create a bar chart with Graph Objects
fig_bar_go = go.Figure()

# Add a trace for the bar chart
fig_bar_go.add_trace(go.Bar(x=df['Month'], y=df['#Passengers'], name='Passengers'))

# Update layout for the bar chart
fig_bar_go.update_layout(title='Number of Passengers per Month', xaxis_title='Month', yaxis_title='Passengers')

# Show the bar chart
fig_bar_go.show()


#%%
# Replicate the Scatter Plot using Graph Objects
# Create a scatter plot with Graph Objects
fig_scatter_go = go.Figure()

# Add a trace for the scatter plot
fig_scatter_go.add_trace(go.Scatter(x=df['Month'], y=df['#Passengers'], mode='markers', name='Passengers'))

# Update layout for the scatter plot
fig_scatter_go.update_layout(title='Scatter Plot of Passengers per Month', xaxis_title='Month', yaxis_title='Passengers')

# Show the scatter plot
fig_scatter_go.show()