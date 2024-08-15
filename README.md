# api-test-generator

# Pre-requisites
- Python 3.6 or higher
- [postman cli or newman](https://learning.postman.com/docs/postman-cli/postman-cli-installation/)
- [Ollama (llama3.1 model installed)](https://ollama.com/download)

# Run steps
1. Clone the repository
2. Install the pre-requisites
3. Replace the Open API specification in the input directory `data/input/open-api-documenation.yml`
4. Run the following command to generate the test cases and output the path to the postman collection.
   If there are any errors re-run the command and usually it will work.
    ```bash
    python3 main.py
    ```
5. Run the following command to run the postman collection
    ```bash
    newman run /path/to/postman_collection.json
    # or
    postman run /path/to/postman_collection.json
    ```


