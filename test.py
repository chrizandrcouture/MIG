import pdb
import requests
import aiohttp
import asyncio
import json


async def llm_test():
    data = {
        "model": "mistralai/Mixtral-8x7B-Instruct-v0.1",
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


outputs = asyncio.run(llm_test())
breakpoint()
