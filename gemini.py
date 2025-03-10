import google.generativeai as genai

from sendmail import sendmail

# 设置 API Key
genai.configure(api_key="AIzaSyDh7LYrvPiqUf30NKVGN4v1HRqBRbfOpRQ")

# 选择 Gemini 模型
model = genai.GenerativeModel("gemini-2.0-flash")

# 发送请求并获取响应
response = model.generate_content(contents="请帮我搜索今日全球最新的对买入基金有影响的财经新闻并总结给我")

# 邮件发送
sendmail(response.text)
