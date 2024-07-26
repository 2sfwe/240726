import pandas as pd
import streamlit as st

# Load and preprocess data
data = pd.read_csv('daily_temp.csv')
data['날짜'] = data['날짜'].str.strip()
data['날짜'] = pd.to_datetime(data['날짜'], format='%Y-%m-%d')

# Define clothing recommendations based on temperature
def clothing_recommendation(temp):
    if temp <= 0:
        return "매우 추워요ㅠㅠ: 두꺼운 겨울 내피와 따듯한 코트, 보온성 의류를 입으세요."
    elif 0 < temp <= 10:
        return "추워요: 겨울 자켓, 스웨터와 함께 레이어드 스타일로 입어 보세요."
    elif 10 < temp <= 20:
        return "시원해요~: 얇은 자켓, 긴 소매옷, 혹은 얇은 스웨터를 입어 보세요."
    elif 20 < temp <= 25:
        return "살짝 더워요~: 티셔츠, 얇은 옷과 편한 바지를 입어 보세요."
    elif 25 < temp <= 30:
        return "더워요~.~: 짧은 소매의 상의, 반바지를 입고 물을 자주 마셔주세요!"
    else:
        return "쪄죽어요ㅠㅠ: 얇은 옷과 햇살을 막을 모자를 추천해요! 물을 충분히 마셔주세요~"

# Streamlit UI
st.title('날짜별 옷차림 추천')

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
