import requests
import load_file

url = "http://localhost:11434/api/chat"


def llama3(prompt):

    # system_prompt = load_file.load_file("/Users/kevindowdy/Library/CloudStorage/OneDrive-EY/Desktop/Software Applications/auto-test-generation-script/data/input/system-prompt.txt")
    system_prompt = load_file.load_file("/Users/kevindowdy/Library/CloudStorage/OneDrive-EY/Desktop/Software Applications/auto-test-generation-script/data/input/reasoning_system_prompt_draft.txt")

    data = {
        # "model": "codellama:7b",
        "model": "llama3.1",
        # "model": "llama2:7b",
        "messages": [
            {"role": "system_prompt", "content": system_prompt},
            {"role": "user", "content": prompt}
        ],
        "stream": False,
    }

    headers = {
        "Content-Type": "application/json"
    }

    response_from_model = requests.post(url, headers=headers, json=data)
    print(response_from_model.json())
    return response_from_model.json()["message"]["content"]

