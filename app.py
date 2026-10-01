import streamlit as st
import ollama

st.title("AI Chatbot")
st.caption("hiii")

text = st.text_input("Ask me anything")

if st.button("Send"):
    if text:
        response = ollama.chat(
            model="llama3.2",
            messages=[
                {
                    "role": "user",
                    "content": text
                }
            ]
        )

        st.write(response["message"]["content"])
    else:
        st.warning("Please enter a question.")