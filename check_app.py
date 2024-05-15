#coding:utf-8
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()


client = OpenAI()

## 列出所有批处理任务.
# print(client.batches.list(limit=10))

## 返回结果.
response = client.batches.retrieve("batch_gUwDs8Sdhw6DBEBp6JyPPXZa")
print(response.id)
print(response.status)

## 取消.
# client.batches.cancel("batch_abc123")


# 使用Batch ID来检索批处理状态
batch_status = client.batches.retrieve("batch_gUwDs8Sdhw6DBEBp6JyPPXZa")

# 检查批处理是否完成
if batch_status.status == 'completed':
    # 使用output_file_id来下载结果
    output = client.files.content(batch_status.output_file_id)
    with open('output.json|', 'w') as file:
      file.write(str(output.content.decode('utf-8')))