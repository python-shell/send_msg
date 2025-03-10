from openai import OpenAI
from sendmail import sendmail

# 请确保您已将 API Key 存储在环境变量 ARK_API_KEY 中
# 初始化Openai客户端，从环境变量中读取您的API Key
client = OpenAI(
    # 此为默认路径，您可根据业务所在地域进行配置
    base_url="https://ark.cn-beijing.volces.com/api/v3/bots",
    # 从环境变量中获取您的 API Key
    api_key='93f85a1e-edbf-4fc0-b012-0d2d25059f52'
)

# Non-streaming:
print("----- standard request -----")
completion = client.chat.completions.create(
    model="bot-20250305224914-475rc",  # bot-20250305224914-475rc 为您当前的智能体的ID，注意此处与Chat API存在差异。差异对比详见 SDK使用指南
    messages=[
        {"role": "system", "content": "你是豆包，是由字节跳动开发的 AI 人工智能助手"},
        {"role": "user", "content": "请帮我联网搜索今日全球最新的对买入基金有影响的财经新闻并总结给我"},
    ],
)
res = completion.choices[0].message.content

# 邮件发送
sendmail(res)
