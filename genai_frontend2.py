import streamlit as st
import genai_backend as back

st.title("ChatBot Demo")

if "chats" not in st.session_state:
    st.session_state.chats = {}

if "current_chat" not in st.session_state:
    st.session_state.current_chat = None

if "memories" not in st.session_state:
    st.session_state.memories = {}

# ---------------- Sidebar (ChatGPT-like) ----------------
with st.sidebar:
    st.markdown("## 💬 Chats")

    # ---- New Chat Button ----
    if st.button("➕ New Chat", use_container_width=True):
        chat_id = f"Chat {len(st.session_state.chats) + 1}"
        st.session_state.chats[chat_id] = []
        st.session_state.memories[chat_id] = back.chat_memory()
        st.session_state.current_chat = chat_id
        st.rerun()

    st.markdown("---")

    # ---- Existing Chats ----
    for chat_id in st.session_state.chats:
        if st.button(chat_id, use_container_width=True):
            st.session_state.current_chat = chat_id
            st.rerun()

# Create default chat ONLY ON FIRST LOAD
if not st.session_state.chats:
    chat_id = "Chat 1"
    st.session_state.chats[chat_id] = []
    st.session_state.memories[chat_id] = back.chat_memory()
    st.session_state.current_chat = chat_id

# Active chat
chat_id = st.session_state.current_chat
chat_history = st.session_state.chats[chat_id]
memory = st.session_state.memories[chat_id]

for message in chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["text"])

input_text = st.chat_input("Chatbot Powered by BedRock & Nova-lite")

if input_text:
    chat_history.append({"role": "user", "text": input_text})
    with st.chat_message("user"):
        st.markdown(input_text)

    chat_response = back.chat_conversation(input_text=input_text,memory=memory)

    chat_history.append({"role": "assistant", "text": chat_response})
    with st.chat_message("assistant"):
        st.markdown(chat_response)