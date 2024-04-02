import streamlit as st

st.title("Breathworks AI Platform 🫁")
st.sidebar.image("logo.jpg", use_column_width=True)

from agent.core_lda import ModelHandler

handler = ModelHandler()
handler.create_model_adapter(name="TestAdapter")


if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistant", "content": "Hi, I'm a Breathworks chatbot who can answer questions. How can I help you?"}
    ]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

m = st.markdown("""
    <style>
    .stChatInputContainer > div {
    textColor-color: #31659C;
    }
    </style>
    """, unsafe_allow_html=True)

if prompt := st.chat_input(placeholder="What are the benefits of meditation?"):
    # st.markdown('<style>' + open('.streamlit/style.css').read() + '</style>', unsafe_allow_html=True)
    # st.markdown(f"""
    #   <style>
    #   [class="st-af st-b5 st-b6 st-ar st-as st-b7 st-b8 st-b9 st-ba st-bb st-bc st-bd st-b1"]{{
    #         background-color: #4A55A2;
    #         color: #C5DFF8;
    #   }}
    #   </style>
    # """
    # , unsafe_allow_html=True)
    st.session_state.messages.append({"role": "user", "content": prompt})

    st.chat_message("user").write(prompt)
    print(prompt)
    # Generate and print the enhanced response using LDA topics
    enhanced_response = handler.generate_response(
        query=prompt,
        use_lda_insights=True  # Enhanced answer with LDA topics
    )
    print(f"> Enhanced Response (with LDA insights):\n{enhanced_response}\n")

    with st.chat_message("assistant"):
        st.session_state.messages.append({"role": "assistant", "content": enhanced_response})
        st.write(enhanced_response)
