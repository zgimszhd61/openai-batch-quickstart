from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()
batch_input_file = client.files.create(
  file=open("batchinput.jsonl", "rb"),
  purpose="batch"
)

batch_input_file_id = batch_input_file.id

response = client.batches.create(
    input_file_id=batch_input_file_id,
    endpoint="/v1/chat/completions",
    completion_window="24h",
    metadata={
      "description": "nightly eval job"
    }
)

print(response.id)