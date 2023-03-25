# 简介
本项目使用Python的streamlit模块，部署一个对openai api代理访问的web服务器。旨在帮助大家输入openai api key即可畅享ai对话。

# 部署环境
本地、云主机、docker或者app平台。

# 软件版本
Python 3.6或以上，安装依赖
```bash
pip3 install -r requirements.txt
```

# 部署
将本项目clone到本地，执行
```bash
streamlit run  app.py
```

列子：
```bash
wanlinwang@MacBook-Pro openai % streamlit run  app.py

  👋 Welcome to Streamlit!

  If you’d like to receive helpful onboarding emails, news, offers, promotions,
  and the occasional swag, please enter your email address below. Otherwise,
  leave this field blank.

  Email:  yourname@gmail.com

  You can find our privacy policy at https://streamlit.io/privacy-policy

  Summary:
  - This open source library collects usage statistics.
  - We cannot see and do not store information contained inside Streamlit apps,
    such as text, charts, images, etc.
  - Telemetry data is stored in servers in the United States.
  - If you'd like to opt out, add the following to ~/.streamlit/config.toml,
    creating that file if necessary:

    [browser]
    gatherUsageStats = false


  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://192.168.6.210:8501

  For better performance, install the Watchdog module:

  $ xcode-select --install
  $ pip install watchdog

```

# 使用
上一步骤自动唤醒浏览器，打开代理网站。输入openai api key即可访问了。
<img width="1427" alt="image" src="https://user-images.githubusercontent.com/32032219/227698436-764a79c8-4118-4a38-b023-fbff61cfdaba.png">
