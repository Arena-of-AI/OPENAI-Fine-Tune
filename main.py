import streamlit as st
import pandas as pd
import json

def excel_to_jsonl(file):
    # 讀取Excel檔案，並將數據轉換為DataFrame格式
    data = pd.read_excel(file)

    # 將DataFrame轉換為JSON格式
    json_data = json.loads(data.to_json(orient='records'))

    # 將JSON格式寫入JSONL文件
    with open('data.jsonl', 'w', encoding='utf-8') as f:
        for record in json_data:
            f.write(json.dumps(record, ensure_ascii=False) + '\n')

# 主要程式碼
st.title('Training Data Converter')

# 讓使用者上傳Excel檔案
uploaded_file = st.file_uploader('Upload Training Data', type=['xlsx'])

# 如果有上傳檔案，則進行格式轉換
if uploaded_file:
    st.write('Converting file...')
    excel_to_jsonl(uploaded_file)
    st.write('File conversion completed!')
