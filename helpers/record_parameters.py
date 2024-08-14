import datetime

from helpers import save_to_file


def save_as_file(date_and_time, execution_time, user_prompt, system_prompt, model_name, response, json_output):
    # Save the user prompt to a file
    save_to_file.save_to_file(date_and_time, "/Users/kevindowdy/Library/CloudStorage/OneDrive-EY/Desktop/Software Applications/auto-test-generation-script/data/output/" + str(date_and_time) + "/user_prompt", user_prompt)

    # Save the system prompt to a file
    save_to_file.save_to_file(date_and_time, "/Users/kevindowdy/Library/CloudStorage/OneDrive-EY/Desktop/Software Applications/auto-test-generation-script/data/output/" + str(date_and_time) + "/system_prompt", system_prompt)

    # Save the response to a file
    save_to_file.save_to_file(date_and_time, "/Users/kevindowdy/Library/CloudStorage/OneDrive-EY/Desktop/Software Applications/auto-test-generation-script/data/output/" + str(date_and_time) + "/postman_collection", response)

    # Save the performance metrics to a file
    metrics = "Model Name: " + model_name + "\nExecution time: " + str(execution_time) + " seconds"
    save_to_file.save_to_file(date_and_time, "/Users/kevindowdy/Library/CloudStorage/OneDrive-EY/Desktop/Software Applications/auto-test-generation-script/data/output/" + str(date_and_time) + "/metrics", metrics)

    # Save the cleaned json to a file
    save_to_file.save_to_file(date_and_time, "/Users/kevindowdy/Library/CloudStorage/OneDrive-EY/Desktop/Software Applications/auto-test-generation-script/data/output/" + str(date_and_time) + "/json_output", json_output)
