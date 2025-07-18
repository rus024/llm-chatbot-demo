import streamlit as st
import openai

openai.api_key = st.secrets["OPENAI_API_KEY"]

st.title("🤖 Ruslan's Chatbot")

if 'messages' not in st.session_state:
    st.session_state['messages'] = [
        {"role": "system", "content": "You are a helpful and strategic assistant."}
    ]

user_input = st.text_input("You:", "")

if user_input:
    st.session_state['messages'].append({"role": "user", "content": user_input})

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=st.session_state['messages'],
        max_tokens=300
    )

    reply = response.choices[0].message.content
    st.session_state['messages'].append({"role": "assistant", "content": reply})
    st.text_area("Assistant:", value=reply, height=200, max_chars=None)

if st.button("Show Conversation History"):
    for msg in st.session_state['messages']:
        st.write(f"**{msg['role'].capitalize()}**: {msg['content']}")
