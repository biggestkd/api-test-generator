import load_file
from helpers import send_prompt
from helpers import save_to_file


def generate(date_and_time, model_name):

    # Load the generic user prompt from a file
    generic_prompt = load_file.load_file("/Users/kevindowdy/Library/CloudStorage/OneDrive-EY/Desktop/Software Applications/auto-test-generation-script/data/input/postman-collection-generation-prompt.txt")

    # Load the OpenAPI documentation from a file
    documentation = load_file.load_file("/Users/kevindowdy/Library/CloudStorage/OneDrive-EY/Desktop/Software Applications/auto-test-generation-script/data/input/open-api-documenation.yml")

    # Replace the placeholder in the user prompt with the OpenAPI documentation
    user_prompt = generic_prompt.replace("******document******", documentation)

    # Load the system prompt from a file
    system_prompt = load_file.load_file("/Users/kevindowdy/Library/CloudStorage/OneDrive-EY/Desktop/Software Applications/auto-test-generation-script/data/input/reasoning_system_prompt_draft.txt")

    # Send the user prompt and system prompt to the LLM system
    response = send_prompt.generate(user_prompt, system_prompt, model_name)

    return system_prompt, user_prompt, response