import streamlit as st
import json

HISTORY_FILE = "chat_history_mp3.json"

st.title("🧳 여행친구 🚀")

# 1) 기존에 저장된 대화 불러오기
with open(HISTORY_FILE, "r", encoding="utf-8") as f:
    chat_history = json.load(f)

# 2) 대화 내역 출력
for msg in chat_history:
    if msg.startswith("[사용자]"):
        st.markdown(f"**🗣️ {msg}**")
    elif msg.startswith("[가이드 🎧]"):
        # 파일명 추출
        mp3_file = msg.replace("[가이드 🎧] ", "").strip()
        st.markdown("**🤖 가이드 음성 메시지:**")
        st.audio(mp3_file)
    else:
        st.markdown(msg)
