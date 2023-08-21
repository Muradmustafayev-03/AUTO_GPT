from openai_api import gpt_response
from system_prompts import *
import re


def is_task_complicated(user_prompt: str):
    return 'True' in gpt_response(user_prompt, IS_TASK_COMPLICATED)


def divide_into_subtasks(user_prompt: str):
    response = gpt_response(user_prompt, DIVIDE_INTO_SUBTASKS)
    pattern = r'(\d+)\.\s*([\s\S]+?)(?=\d+\.|$)'
    matches = re.finditer(pattern, response, re.DOTALL)
    return [match.group(2).strip() for match in matches]
