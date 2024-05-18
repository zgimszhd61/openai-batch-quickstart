#coding:utf-8
from openai import OpenAI
from dotenv import load_dotenv
import json

load_dotenv()


client = OpenAI()

## 列出所有批处理任务.
# print(client.batches.list(limit=10))

## 返回结果.
response = client.batches.retrieve("batch_mCBPWpNwm68dNEz7vOkBSqgw")
print(response.id)
print(response.status)

## 取消.
# client.batches.cancel("batch_abc123")


# 使用Batch ID来检索批处理状态
batch_status = client.batches.retrieve("batch_mCBPWpNwm68dNEz7vOkBSqgw")

# # 检查批处理是否完成
if batch_status.status == 'completed':
    # 使用output_file_id来下载结果
    output = client.files.content(batch_status.output_file_id)
    with open('output.json|', 'w') as file:
      file.write(str(output.content.decode('utf-8')))

# 读取JSON Lines文件
with open('output.json|', 'r') as file:
    for line in file:
        data = json.loads(line)  # 解析每一行的JSON数据
        # 处理每个JSON对象
        print(data['response']['body']['choices'][0]['message']['content'])