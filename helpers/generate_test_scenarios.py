import load_file
from helpers import send_prompt
from helpers import save_to_file


def generate(datetime):
    prompt = load_file.load_file("/Users/kevindowdy/Library/CloudStorage/OneDrive-EY/Desktop/Software Applications/auto-test-generation-script/data/input/test-case-scenario-generation-prompt.txt")
    documentation = load_file.load_file("/Users/kevindowdy/Library/CloudStorage/OneDrive-EY/Desktop/Software Applications/auto-test-generation-script/data/input/open-api-documenation.yml")
    decorated_prompt = prompt.replace("******document******", documentation)
    # print(decorated_prompt)
    response = send_prompt.generate(decorated_prompt)
    save_to_file.save_to_file(datetime, "/Users/kevindowdy/Library/CloudStorage/OneDrive-EY/Desktop/Software Applications/auto-test-generation-script/data/output/" + str(datetime) + "/test_scenarios", response)




