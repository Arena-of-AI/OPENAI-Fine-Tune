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

# 讀取現有的模型列表
def get_model_list():
    model_list = openai.Model.list()
    return [model.id for model in model_list["data"]]

# 建立自訂模型
def create_custom_model(model_name):
    model = openai.Model.create(
        id=model_name,
        language="en",
        training_data=[],
        max_documents=10000,
        n_epochs=1,
        model="text-davinci-002",
    )
    return model.id

# Streamlit App
def app():
    st.title("OpenAI Fine Tune Training")
    st.write("")

    # 使用者輸入OpenAI API Key
    api_key = st.text_input("Enter OpenAI API Key")

    # 驗證OpenAI API Key格式是否正確
    if validate_api_key(api_key):
        st.write("API Key format is valid")
        openai.api_key = api_key
    else:
        st.write("Invalid API Key format")

    # 確認API Key
    if st.button("Confirm API Key"):
        if openai.api_key != "":
            st.write("API Key confirmed")
        else:
            st.write("Please enter a valid API Key")
