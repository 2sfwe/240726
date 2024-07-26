import streamlit as st
st.title('나의 첫 웹 서비스 만들기>.<')
name = st.text_input('이름을 입력해주세요 : ')
menu = st.selectbox('좋아하는 음식을 선택해주세요 : '), ['떡볶이', '짬뽕', '마라탕', '마라샹궈', '닭발']
if st.button('인사말 생성') : #버튼이 클릭되면 참이라고 생각하면 됨
  st.write(name+'님! 당신이 좋아하는 음식은 '+menu+'이군요?!? 저도 참 좋아합니다')
