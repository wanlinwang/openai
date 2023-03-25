import openai
import streamlit as st
import public_ip as ip

# 创建 Streamlit 应用程序
st.set_page_config(
        page_title="OpenAI Proxy",
)
st.title("OpenAI Proxy")
# 设置子标题
st.subheader('To use OpenAI smoothly')

def display_msg(text):
    msg_str = [ f"{entry['role'].replace('user', '🤔').replace('system', '💻')} {entry['content']}" for entry in st.session_state['messages'][1:] ]
    text.text_area("Messages", value=str("\n\n".join(msg_str)), height=500)

INITIAL_PROMPT = [{"role": "system", "content": "You are an ai chatbot."}]

if 'messages' not in st.session_state:
    st.session_state['messages'] = INITIAL_PROMPT

# 设置 OpenAI API 密钥
openai.api_key = st.text_input("Paste openai api key here:", value="", type="password")

# 设置模型
model = st.selectbox(
    'Which AI model would you like to use?',
    ('gpt-3.5-turbo',))

# 用户输入 prompt
prompt = st.text_input("Prompt:", value='')

# 将两个按钮放在同一行
col1, col2 = st.columns([1,1])

# 生成回答
with col1:
    if st.button("Generate"):
        with st.spinner("Generating..."):
            st.session_state['messages'] += [{"role": "user", "content": prompt}]
            response = openai.ChatCompletion.create(
                model=model,
                messages=st.session_state['messages'],
            )

            # public_ip = ""
            # try:
            #     public_ip = ip.get()
            # except ValueError as e:
            #     pass
            # public_ip_notice = ""
            # if len(public_ip) != 0:
            #     public_ip_notice = f"(Proxy ip: {public_ip})"

            msg_response = response["choices"][0]["message"]["content"]
            st.session_state["messages"] += [
                # {"role": "system", "content": msg_response + public_ip_notice}
                {"role": "system", "content": msg_response}
            ]
with col2:
    if st.button("Flush"):
        st.session_state["messages"] = INITIAL_PROMPT

text = st.empty()
display_msg(text)

st.text("Github repo address: https://github.com/wanlinwang/openai")
