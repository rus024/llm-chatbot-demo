import streamlit as st
import openai

client = openai.OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.title("🤖 Ruslan's Chatbot")

if 'messages' not in st.session_state:
    st.session_state['messages'] = [
        {"role": "system", "content": "You are a helpful and strategic assistant."}
    ]

user_input = st.text_input("You:", "")

if user_input:
    st.session_state['messages'].append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
<<<<<<< HEAD
        model="gpt-4",
        messages=st.session_state['messages'],
        max_tokens=300
    )
=======
        model="gpt-3.5-turbo",
    messages=st.session_state['messages'],
    max_tokens=300
)

>>>>>>> 89f3179 (Project completed: Streamlit chatbot functional with OpenAI API. Ready for demo and deployment.)

    reply = response.choices[0].message.content
    st.session_state['messages'].append({"role": "assistant", "content": reply})
    st.text_area("Assistant:", value=reply, height=200, max_chars=None)

<<<<<<< HEAD
if st.button
=======
if st.button("Show Conversation History"):
    for msg in st.session_state['messages']:
        st.write(f"**{msg['role'].capitalize()}**: {msg['content']}")
>>>>>>> 89f3179 (Project completed: Streamlit chatbot functional with OpenAI API. Ready for demo and deployment.)
