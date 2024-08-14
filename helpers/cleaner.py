import json
import re

from helpers import load_file


def clean_postman_output(response):

    # Clean the file
    json_match = re.search(r'\{.*\}', response, re.DOTALL)

    # Check if the JSON was found
    if json_match:
        json_string = json_match.group(0)
        try:
            # Try to load the JSON string to ensure it's valid
            json.loads(json_string)
            return json_string
        except json.JSONDecodeError as e:
            print("Error decoding JSON:", e)
            return None
    else:
        print("No JSON found in the text.")
        return None
