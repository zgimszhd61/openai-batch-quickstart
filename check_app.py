from openai import OpenAI
import os

os.environ["OPENAI_API_KEY"] = "sk-proj-"

client = OpenAI()

## 列出所有批处理任务.
print(client.batches.list(limit=10))

## 返回结果.
response = client.batches.retrieve("batch_bqZD3HHvE19WBNHsQbF2M8du")
print(response)


## 取消.
# client.batches.cancel("batch_abc123")