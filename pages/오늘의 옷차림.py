import pandas as pd
import streamlit as st

# Load and preprocess data
data = pd.read_csv('daily_temp.csv')
data['날짜'] = data['날짜'].str.strip()
data['날짜'] = pd.to_datetime(data['날짜'], format='%Y-%m-%d')

# Define clothing recommendations based on temperature
def clothing_recommendation(temp):
    if temp <= 0:
        return "Very cold: Wear heavy winter clothing, a warm coat, and thermal wear."
    elif 0 < temp <= 10:
        return "Cold: Wear a winter jacket, sweaters, and layered clothing."
    elif 10 < temp <= 20:
        return "Cool: Light jackets, long sleeves, and possibly a sweater."
    elif 20 < temp <= 25:
        return "Warm: T-shirts, light shirts, and comfortable pants."
    elif 25 < temp <= 30:
        return "Hot: Wear short sleeves, shorts, and stay hydrated."
    else:
        return "Very hot: Wear light clothing, hats, and drink plenty of water."

# Streamlit UI
st.title('Clothing Recommendation Based on Temperature')

# Date input
date_input = st.date_input("Select a date", pd.to_datetime('2023-01-01'))
selected_date = pd.to_datetime(date_input)

# Filter data for the selected date
selected_data = data[data['날짜'] == selected_date]

if not selected_data.empty:
    # Extract the average temperature
    avg_temp = selected_data['평균기온(℃)'].iloc[0]
    # Get clothing recommendation
    recommendation = clothing_recommendation(avg_temp)
    
    st.write(f"Average temperature on {selected_date.strftime('%Y-%m-%d')}: {avg_temp}°C")
    st.write(f"Recommendation: {recommendation}")
else:
    st.write("No data available for the selected date.")
