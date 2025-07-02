import streamlit as st
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

load_dotenv()

# 専門家の種類とシステムメッセージ
EXPERTS = {
    "医療専門家": "あなたは優秀な医療専門家です。専門的かつ分かりやすく回答してください。",
    "法律専門家": "あなたは経験豊富な法律専門家です。法律的観点から丁寧に回答してください。",
    "ITエンジニア": "あなたは熟練したITエンジニアです。技術的な観点から分かりやすく回答してください。"
}

def get_llm_response(user_input: str, expert_type: str) -> str:
    """入力テキストと専門家タイプを受け取り、LLMからの回答を返す"""
    llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)
    messages = [
        SystemMessage(content=EXPERTS[expert_type]),
        HumanMessage(content=user_input)
    ]
    result = llm(messages)
    return result.content

# --- Streamlit UI ---
st.title("専門家AIチャットアプリ")
st.write("""
このアプリは、あなたの質問に対して選択した分野の専門家になりきったAIが回答します。  
1. 専門家の種類を選択  
2. 質問を入力  
3. 「送信」ボタンを押してください
""")

expert_type = st.radio("専門家の種類を選択してください", list(EXPERTS.keys()))
user_input = st.text_area("質問を入力してください", height=100)
submit = st.button("送信")

if submit and user_input.strip():
    with st.spinner("AIが回答中です..."):
        answer = get_llm_response(user_input, expert_type)
    st.markdown("#### 回答")
    st.write(answer)
