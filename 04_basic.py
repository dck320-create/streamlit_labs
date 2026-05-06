import streamlit as st
from PIL import Image

image = Image.open('input/egg.png')

# 이미지 불러오기
st.image(image, caption='egg_image')
st.image(image, caption="width(너비)->100", width=100)
st.image(image, caption="width(너비)->200", width=200)

# 화면 채우기
st.image(image, caption="전체 너비", width="stretch")

# 이미지 원본 크기
st.image(image, caption="원본 크기", width="content")

# 이미지 작게 새로운 변수에 저장
small_image = image.resize((200, 200))  # 강제로 작게

st.image(small_image, caption="stretch - 전체너비", width="stretch")
st.image(small_image, caption="content - 원본크기(200px)", width="content")