import openai
import streamlit as st

# 创建 Streamlit 应用程序
st.set_page_config(
        page_title="OpenAI Proxy",
)
st.title("OpenAI Proxy")
# 设置子标题
st.subheader('To use OpenAI smoothly')

def display_msg(text):
    msg_str = [f"{entry['role'].replace('user', '🤔').replace('system', '💻')} {entry['content']}" for entry in st.session_state['messages'][1:]]
    text.text_area("Messages", value=str("\n\n".join(msg_str)), height=500)

def clear_prompt():
    st.session_state["prompt_input"] = ""


INITIAL_PROMPT = [{"role": "system", "content": "You are an ai chatbot."}]

# 在session状态里设置会话信息
if 'messages' not in st.session_state:
    st.session_state['messages'] = INITIAL_PROMPT
if 'prompt_input' not in st.session_state:
    st.session_state["prompt_input"] = ""

# 设置 OpenAI API密钥
openai.api_key = st.text_input("Paste openai api key here:", value="", type="password")

# 设置模型
model = st.selectbox(
    'Which AI model would you like to use?',
    ('gpt-3.5-turbo',))

# 用户输入 prompt
prompt = st.text_input("Prompt:", value='', key="prompt_input")

# 将两个按钮放在同一行
col1, col2, col3, _, _ = st.columns(5, gap="small")

# 生成回答
with col1:
    # 按了Generate之后，执行生成
    if st.button("Generate"):
        with st.spinner("Generating..."):
            st.session_state['messages'] += [{"role": "user", "content": prompt}]
            
            response = openai.ChatCompletion.create(
                model=model,
                messages=st.session_state['messages'],
            )

            msg_response = response["choices"][0]["message"]["content"]
            st.session_state["messages"] += [
                {"role": "system", "content": msg_response}
            ]

# 清空prompt输入框
with col2:
    if st.button("Clear Prompt", on_click=clear_prompt):
        st.write(prompt)

# 清空所有对话
with col3:
    if st.button("Clear All"):
        st.session_state["messages"] = INITIAL_PROMPT

text = st.empty()
display_msg(text)

st.markdown("""
[Github repo address](https://github.com/wanlinwang/openai)
""")
