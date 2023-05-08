import re
import streamlit as st

# 正则表达式模式，用于验证OpenAI API Key格式
API_KEY_REGEX = r"^[a-z0-9]{32}$"

# 创建文本框组件
api_key_input = st.text_input("Enter your OpenAI API Key:")

# 验证API Key格式
if api_key_input:
    if not re.match(API_KEY_REGEX, api_key_input):
        st.error("Invalid OpenAI API Key format!")
    else:
        st.success("OpenAI API Key is valid!")

