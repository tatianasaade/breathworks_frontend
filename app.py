import streamlit as st

# with st.sidebar:
#     openai_api_key = st.text_input(
#         "OpenAI API Key", key="langchain_search_api_key_openai", type="password"
#     )
#     "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"
#     "[View the source code](https://github.com/streamlit/llm-examples/blob/main/pages/2_Chat_with_search.py)"
#     "[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/streamlit/llm-examples?quickstart=1)"

#Inject custom CSS to change background color
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("style.css")

st.title("🫁 Breathworks-AI Platform 🫁")
st.sidebar.image("logo.jpg", use_column_width=True)
# prompt = st.text_input('Prompt')
# """
# Some text explaining what Breathworks does etc.
# """

if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistant", "content": "Hi, I'm a chatbot who can search the web. How can I help you?"}
    ]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input(placeholder="What are the benefits of meditation?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    # if not openai_api_key:
    #     st.info("Please add your OpenAI API key to continue.")
    #     st.stop()

#     llm = ChatOpenAI(model_name="gpt-3.5-turbo", openai_api_key=openai_api_key, streaming=True)
#     search = DuckDuckGoSearchRun(name="Search")
#     search_agent = initialize_agent(
#         [search], llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, handle_parsing_errors=True
#     )
    # with st.chat_message("assistant"):
    #     st_cb = StreamlitCallbackHandler(st.container(), expand_new_thoughts=False)
    #     response = search_agent.run(st.session_state.messages, callbacks=[st_cb])
    #     st.session_state.messages.append({"role": "assistant", "content": response})
    #     st.write(response)
