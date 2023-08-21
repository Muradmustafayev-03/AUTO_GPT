from secret import *
import openai
import json


openai.api_key = OPENAI_KEY
openai.organization = ORGANIZATION


def gpt_response(user_prompt: str, system_prompt: str = None, temperature: float = 1.0):
    messages = []
    if system_prompt:
        messages.append({'role': 'system', 'content': system_prompt})
    messages.append({'role': 'user', 'content': user_prompt})
    res = openai.ChatCompletion.create(
        model='gpt-3.5-turbo-16k',
        messages=messages,
        temperature=temperature
    )
    return json.loads(str(res))['choices'][0]['message']['content']
