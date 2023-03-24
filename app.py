import openai
import streamlit as st
import public_ip as ip

# 创建 Streamlit 应用程序
st.title("OpenAI Proxy")
# 设置子标题
st.subheader('To use OpenAI smoothly')

def display_msg(text):
    msg_str = [ f"{entry['role']}: {entry['content']}" for entry in st.session_state['messages'][1:] ]
    text.text_area("Messages", value=str("\n\n".join(msg_str)), height=500)

ROLE_PROMPT = [{"role": "AI", "content": "You are a life assistant."}]

if 'messages' not in st.session_state:
    st.session_state['messages'] = ROLE_PROMPT

# 设置 OpenAI API 密钥
openai.api_key = st.text_input("Please enter your openai api key", value="", type="password")

# 用户输入 prompt
prompt = st.text_input("Prompt", value='')

# 将两个按钮放在同一行
col1, col2 = st.columns([1,1])

# 生成回答
with col1:
    if st.button("Generate"):
        with st.spinner("Generating..."):
            public_ip = ip.get()
            st.session_state['messages'] += [{"role": "user", "content": prompt}]
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=st.session_state['messages'],
            )
            msg_response = response["choices"][0]["message"]["content"]
            st.session_state["messages"] += [
                {"role": "AI", "content": msg_response + f"\nYour public ip address is {public_ip}."}
            ]
with col2:
    if st.button("Refresh"):
        st.session_state["messages"] = ROLE_PROMPT

text = st.empty()
display_msg(text)
