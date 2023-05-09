import streamlit as st
import openai
import pandas as pd
import jsonlines

# 設定OpenAI API Key
openai.api_key = st.text_input("請輸入OpenAI API Key：")

# 檢查API Key是否有效
try:
    models = openai.Model.list()
except Exception as e:
    st.error(f"無法連接OpenAI API，請檢查API Key是否正確：{e}")
    st.stop()


# 設置好fine-tune的相關參數
fine_tune_config = {
    "train_file": "path/to/train_data.jsonl",
    "validation_file": "path/to/validation_data.jsonl",
    "output_directory": "path/to/output_directory",
    "model": "text-davinci-002",
    "num_epochs": 5,
    "batch_size": 16,
    "learning_rate": 1e-5
}

# 調用prepare_data來轉換訓練數據的格式
openai.FineTune.prepare_data(**fine_tune_config)

# 讓使用者上傳自己的training data（使用excel格式）
uploaded_file = st.file_uploader("Upload Excel File", type=["xlsx"])

if uploaded_file is not None:
    try:
        # 讀取excel檔案
        df = pd.read_excel(uploaded_file)
        # 轉換成jsonl格式
        jsonl = openai.FineTune.prepare_data(df=df)
        # 顯示檔案轉換已完成
        st.success('File conversion completed!')
        # 下載jsonl檔案
        href = f'<a href="data:application/jsonl;base64,{jsonl}">Download jsonl file</a>'
        st.markdown(href, unsafe_allow_html=True)
        st.download_button(label="Download jsonl", data=jsonl, file_name="training_data.jsonl", mime="application/jsonl")
    except errors.AuthenticationError:
        st.error("Invalid OpenAI API key")
    except Exception as e:
        st.error(f"Error: {e}")
