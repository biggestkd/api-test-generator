import sys
import os
import time
from datetime import datetime


# Add the package directory to the sys.path
sys.path.append(os.path.join(os.path.dirname(__file__), 'helpers'))

from helpers import generate_test_scenarios
from helpers import generate_postman_collection


if __name__ == "__main__":

    date_time_as_string = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Generate test scenarios
    # print("Starting test scenario generation...")
    #
    # start_time = time.time()
    #
    # generate_test_scenarios.generate(date_time_as_string)
    #
    # execution_time = time.time() - start_time
    #
    # print(f"Test Scenario Generation Execution time: {execution_time:.6f} seconds")

    # Generate postman collection
    print("Starting postman collection generation...")

    start_time = time.time()

    generate_postman_collection.generate(date_time_as_string)

    execution_time = time.time() - start_time

    print(f"Postman Collection Generation Execution time: {execution_time:.6f} seconds")

    print("Finished")
