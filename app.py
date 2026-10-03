import streamlit as st
from chatbot import create_chat, get_response


st.set_page_config(
    page_title="StudyMate",
    page_icon="📚"
)


st.title("StudyMate")
st.write("A simple AI study assistant")


# Start a new chat
if "messages" not in st.session_state:
    st.session_state.messages = []

if "chat" not in st.session_state:
    st.session_state.chat = create_chat()


# Clear chat
if st.button("Clear Chat"):
    st.session_state.messages = []
    st.session_state.chat = create_chat()
    st.rerun()


# Show previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])


# User input
question = st.chat_input("Ask your study question...")


if question:

    # Show user question
    st.session_state.messages.append({
        "role": "user",
        "content": question
    })

    with st.chat_message("user"):
        st.write(question)


    # Generate response
    with st.chat_message("assistant"):

        try:
            answer = get_response(
                st.session_state.chat,
                question
            )

            if not answer:
                answer = "I could not generate an answer."

            st.write(answer)

        except Exception as e:
            st.error("Something went wrong while generating the response.")
            st.code(str(e))

            answer = "Sorry, I could not generate a response."

            st.write(answer)


    # Save assistant response
    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })