# openai-batch-quickstart
## 应用场景
 - 批量任务效果验证.
 - 要求时效性不高的（譬如24小时内返回也可以）

## 其他限制
 - 每批次限制：单个批次最多可包含 50,000 个请求，批次输入文件的大小最多可达 100 MB。请注意，/v1/embeddings批次中所有请求的嵌入输入数也被限制为最多 50,000 个。
 - 每个模型的排队提示令牌：每个模型都有允许批处理的最大排队提示令牌数。您可以在平台设置页面上找到这些限制。
