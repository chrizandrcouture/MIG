import pdb
import requests
import aiohttp
import asyncio
import json
import dill


async def code_llama():
    data = {
        "model": "codellama/CodeLlama-70b-Instruct-hf",
        "messages": [
            {"role": "system", "content": "You are a helpful and honest code assistant expert in Python. Please, provide all answers to programming questions in Python"},
            {"role": "user", "content": "create a python notebook that uses langchain to do a structured report generation for a document!"}
            ]
        }
    data_str = json.dumps(data, ensure_ascii=False)

    url = "http://localhost:8000/v1/chat/completions"
    async with aiohttp.ClientSession(json_serialize=json.dumps) as session:
        outputs = []
        for i in range(10):
            outputs.append(session.post(url, json=data))
        out = await asyncio.gather(*outputs, return_exceptions=True)
    return out

async def llm_test():
    data = {
        # "model": "mistralai/Mixtral-8x7B-Instruct-v0.1",
        # "model": "mistralai/Mistral-7B-Instruct-v0.2",
        "model": "HuggingFaceH4/zephyr-7b-gemma-v0.1",
        "messages": [
        {"role": "user", "content": "create a python notebook that uses langchain to do a structured report generation for a document!"}
      ]
    }

    data_str = json.dumps(data, ensure_ascii=False)

    url = "http://localhost:8000/v1/chat/completions"
    async with aiohttp.ClientSession(json_serialize=json.dumps) as session:
        outputs = []
        for i in range(10):
            outputs.append(session.post(url, json=data))
        out = await asyncio.gather(*outputs, return_exceptions=True)
    return out


async def phi_test():
    data = {
        "model": "microsoft/phi-2",
        "messages": [
        {"role": "user", "content": "create a python notebook that uses langchain to do a structured report generation for a document!"}
      ]
    }

    data_str = json.dumps(data, ensure_ascii=False)

    url = "http://localhost:8000/v1/chat/completions"
    async with aiohttp.ClientSession(json_serialize=json.dumps) as session:
        outputs = []
        for i in range(10):
            outputs.append(session.post(url, json=data))
        out = await asyncio.gather(*outputs, return_exceptions=True)
    return out

async def sqlcoder_test():
    table = """
        CREATE TABLE Books
        (
        Id INT PRIMARY KEY IDENTITY(1,1),
        Name VARCHAR (50) NOT NULL,
        Price INT
        )
    """
    question = "Find all the books whose price is more than 500."

    prompt = f"""### Task
        Generate a SQL query to answer [QUESTION]{question}[/QUESTION]

        ### Database Schema
        The query will run on a database with the following schema:
        {table}

        ### Answer
        Given the database schema, here is the SQL query that [QUESTION]{question}[/QUESTION]
        [SQL]
    """
    data = {
        "model": "defog/sqlcoder-7b-2",
        "messages": [
        {"role": "user", "content": prompt}
      ]
    }

    data_str = json.dumps(data, ensure_ascii=False)

    url = "http://localhost:8000/v1/chat/completions"
    async with aiohttp.ClientSession(json_serialize=json.dumps) as session:
        outputs = []
        for i in range(10):
            outputs.append(session.post(url, json=data))
        out = await asyncio.gather(*outputs, return_exceptions=True)
    return out



# outputs = asyncio.run(phi_test())
# breakpoint()

# table = """
#         CREATE TABLE Books
#         (
#         Id INT PRIMARY KEY IDENTITY(1,1),
#         Name VARCHAR (50) NOT NULL,
#         Price INT
#         )
#     """
# question = "Find all the books whose price is more than 500."

# prompt = f"""### Task
#     Generate a SQL query to answer [QUESTION]{question}[/QUESTION]

#     ### Database Schema
#     The query will run on a database with the following schema:
#     {table}

#     ### Answer
#     Given the database schema, here is the SQL query that [QUESTION]{question}[/QUESTION]
#     [SQL]
# """
# data = {
#     "model": "defog/sqlcoder-7b-2",
#     "messages": [
#     {"role": "user", "content": prompt}
#   ]
# }
# data = {
#         # "model": "mistralai/Mixtral-8x7B-Instruct-v0.1",
#         # "model": "mistralai/Mistral-7B-Instruct-v0.2",
#         "model": "HuggingFaceH4/zephyr-7b-gemma-v0.1",
#         "messages": [
#         {"role": "system", "content": ""},
#         # {"role": "user", "content": "create a python notebook that uses langchain to do a structured report generation for a document!"}
#         {"role": "user", "content": "How many helicopters can a human eat in one sitting?"}
#       ]
#     }
# data_str = json.dumps(data, ensure_ascii=False)
# response = requests.post("http://localhost:8000/v1/chat/completions", data=json.dumps(data))
# breakpoint()

text = "def print_hello_world():"
data = {"data": dill.dumps({
            "data": text
            })
        }
response = requests.post("http://localhost:8080/predictions/torchserve_dill_llm_auto", data=data)
breakpoint()

# data = {
#         "model": "microsoft/phi-2",
#         "messages": [
#             # {"role": "system", "content": "You are a helpful and honest code assistant expert in Python. Please, provide all answers to programming questions in Python"},
#             {"role": "user", "content": "create a python notebook that uses langchain to do a structured report generation for a document!"}
#             ]
#         }
# import requests
# response = requests.post("http://localhost:8001/v1/chat/completions", data=json.dumps(data))
# output = json.loads(response.text)["choices"][0]["message"]["content"]
# print(output)
# breakpoint()


# from openai import OpenAI
# client = OpenAI(
#     base_url="http://localhost:8000/v1",
#     api_key="token-abc123",
# )
# completion = client.chat.completions.create(
#   model="mistralai/Mixtral-8x7B-Instruct-v0.1",
#   messages=[
#     {"role": "user", "content": "create a python notebook that uses langchain to do a structured report generation for a document!"}
#   ]
# )
# print(completion.choices[0].message)

# docker run --runtime nvidia --gpus all \
#     -v ~/.cache/huggingface:/root/.cache/huggingface \
#     --env "HUGGING_FACE_HUB_TOKEN=<secret>" \
#     -p 8000:8000 \
#     --ipc=host \
#  vllm/vllm-openai:latest \
#  --model mistralai/Mistral-7B-Instruct-v0.2 --dtype half --gpu-memory-utilization 1


# $MIG_DEVICES="device=MIG-f665593c-0d36-5f04-80df-b357a0e298ca,MIG-fd165a8a-0209-57a4-80d0-0484e95589d9,MIG-d5a923ad-e0a3-53df-adcb-3ecb8bc801cb,MIG-a9aa7947-3a10-5646-8da6-3c2d820b95d6"
# docker run --runtime nvidia --gpus  '$MIG_DEVICES'   \
#     -v ~/.cache/huggingface:/root/.cache/huggingface     --env "HUGGING_FACE_HUB_TOKEN=<secret>"     -p 8000:8000     --ipc=host  vllm/vllm-openai:latest  --model mistralai/Mixtral-8x7B-Instruct-v0.1 --dtype half --gpu-memory-utilization 1 --worker-use-ray --tensor-parallel-size 4

# nvidia-smi -i 0 -mig 1
# nvidia-smi -i 1 -mig 1
# nvidia-smi -i 2 -mig 1
# nvidia-smi -i 3 -mig 1
# nvidia-smi --gpu-reset

# nvidia-smi mig -cgi "5,19,19,19" -C
# nvidia-smi -L

# # nvidia-smi mig -dci && sudo nvidia-smi mig -dgi 1