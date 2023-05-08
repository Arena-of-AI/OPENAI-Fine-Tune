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

# 上傳檔案
uploaded_file = st.file_uploader("上傳Excel檔案", type=["xlsx"])

# 轉換格式
if uploaded_file is not None:
    st.text("格式轉換中...")
    try:
        # 讀取Excel檔案
        df = pd.read_excel(uploaded_file)

        # 將每一行轉換成JSONL格式
        with jsonlines.open("training_data.jsonl", mode="w") as writer:
            for index, row in df.iterrows():
                writer.write({"text": row["text"], "label": row["label"]})
        
        st.success("檔案轉換已完成")
    except Exception as e:
        st.error(f"轉換檔案時發生錯誤：{e}")
