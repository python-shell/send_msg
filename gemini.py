import google.generativeai as genai

# 设置 API Key
genai.configure(api_key="AIzaSyDh7LYrvPiqUf30NKVGN4v1HRqBRbfOpRQ")

# 选择 Gemini 模型
model = genai.GenerativeModel("gemini-2.0-flash")

# 发送请求并获取响应
response = model.generate_content(contents="请帮我搜索一下当前的对股票有影响的实事新闻并总结给我")

# 输出结果
print(response.text)
