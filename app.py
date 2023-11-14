import time
import streamlit as st

st.set_page_config(
        page_title="Echo Bot",
)
st.title("Echo Bot")

# with st.spinner('Wait for it...'):
#     time.sleep(5)
# st.success('Done!')

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("Enter your message here..."):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Add user message to chat history
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    response = f"Echo: {prompt}"

    # Display assistance response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)

    # Add assistant response to chat history
    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })
