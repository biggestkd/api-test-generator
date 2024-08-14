import sys
import os
import time
from datetime import datetime


# Add the package directory to the sys.path
sys.path.append(os.path.join(os.path.dirname(__file__), 'helpers'))

from helpers import generate_postman_collection
from helpers import record_parameters
from helpers import cleaner


if __name__ == "__main__":

    # Specify the model to use
    model_name = "llama3.1"

    # Get the current date and time as a string
    date_time_as_string = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print("Starting postman collection generation...")

    # Start the timer
    start_time = time.time()

    # Generate the postman collection
    system_prompt, user_prompt, response = generate_postman_collection.generate(date_time_as_string, model_name)

    # Stop the timer and calculate the execution time
    execution_time = time.time() - start_time

    print(f"Postman Collection Generation Execution time: {execution_time:.6f} seconds")

    # Clean the generated postman collection
    cleaned_json_output = cleaner.clean_postman_output(response)

    # Save the run information to a file
    record_parameters.save_as_file(date_time_as_string, execution_time, user_prompt, system_prompt, "llama3.1", response, cleaned_json_output)

    print("Finished")
