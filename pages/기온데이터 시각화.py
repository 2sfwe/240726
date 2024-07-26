import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Load the data
data = pd.read_csv('daily_temp.csv')

# Clean and preprocess the data
data['날짜'] = data['날짜'].str.strip()
data['날짜'] = pd.to_datetime(data['날짜'], format='%Y-%m-%d')
data['year'] = data['날짜'].dt.year

# Group by year and calculate mean temperatures
annual_data = data.groupby('year').agg({
    '평균기온(℃)': 'mean',
    '최저기온(℃)': 'mean',
    '최고기온(℃)': 'mean'
}).reset_index()

# Streamlit UI
st.title('Annual Temperature Trends')
st.write("Select the type of chart to display the temperature trends over the years:")

chart_type = st.radio(
    "Chart Type:",
    ('Line Chart', 'Bar Chart')
)

if chart_type == 'Line Chart':
    st.write("### Line Chart of Annual Temperature Trends")
    fig, ax = plt.subplots()
    ax.plot(annual_data['year'], annual_data['평균기온(℃)'], label='Average Temperature (°C)', marker='o')
    ax.plot(annual_data['year'], annual_data['최저기온(℃)'], label='Minimum Temperature (°C)', marker='o')
    ax.plot(annual_data['year'], annual_data['최고기온(℃)'], label='Maximum Temperature (°C)', marker='o')
    ax.set_xlabel('Year')
    ax.set_ylabel('Temperature (°C)')
    ax.legend()
    st.pyplot(fig)

elif chart_type == 'Bar Chart':
    st.write("### Bar Chart of Annual Temperature Trends")
    fig, ax = plt.subplots()
    bar_width = 0.25  # Width of each bar
    index = np.arange(len(annual_data['year']))  # X locations for the groups

    # Create bars for each temperature type
    bar1 = ax.bar(index - bar_width, annual_data['평균기온(℃)'], bar_width, label='Average Temperature (°C)')
    bar2 = ax.bar(index, annual_data['최저기온(℃)'], bar_width, label='Minimum Temperature (°C)')
    bar3 = ax.bar(index + bar_width, annual_data['최고기온(℃)'], bar_width, label='Maximum Temperature (°C)')

    ax.set_xlabel('Year')
    ax.set_ylabel('Temperature (°C)')
    ax.set_xticks(index)
    ax.set_xticklabels(annual_data['year'])
    ax.legend()
    st.pyplot(fig)
