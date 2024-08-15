import requests
import load_file

url = "http://localhost:11434/api/chat"


def generate(user_prompt, system_prompt, model_name):

    data = {
        "model": model_name,
        "messages": [
            {"role": "system_prompt", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        "stream": False,
    }

    headers = {
        "Content-Type": "application/json"
    }

    response_from_model = requests.post(url, headers=headers, json=data)
    # print(response_from_model.json())
    return response_from_model.json()["message"]["content"]

