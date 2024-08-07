import load_file
from helpers import send_prompt
from helpers import save_to_file


def generate(datetime):
    prompt = load_file.load_file("/Users/kevindowdy/Library/CloudStorage/OneDrive-EY/Desktop/Software Applications/auto-test-generation-script/data/input/postman-collection-generation-prompt.txt")
    documentation = load_file.load_file("/Users/kevindowdy/Library/CloudStorage/OneDrive-EY/Desktop/Software Applications/auto-test-generation-script/data/input/open-api-documenation.yml")
    # test_scenarios = load_file.load_file("/Users/kevindowdy/Library/CloudStorage/OneDrive-EY/Desktop/Software Applications/auto-test-generation-script/data/output/" + str(datetime) + "/test_scenarios")
    # decorated_prompt = prompt.replace("******test scenarios******", test_scenarios)
    decorated_prompt = prompt.replace("******document******", documentation)
    # print(decorated_prompt)
    response = send_prompt.llama3(decorated_prompt)
    save_to_file.save_to_file(datetime, "/Users/kevindowdy/Library/CloudStorage/OneDrive-EY/Desktop/Software Applications/auto-test-generation-script/data/output/" + str(datetime) + "/postman_collection", response)