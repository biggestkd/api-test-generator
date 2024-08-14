# api-test-generator

# Pre-requisites
- Python 3.6 or higher
- postman cli or newman
- Ollama (llama3.1 model installed)

# Run steps
1. Clone the repository
2. Install the pre-requisites
3. Run the following command to generate the test cases
    ```bash
    python3 main.py
    ```
4. Run the following command to run the postman collection
    ```bash
    newman run /path/to/postman_collection.json
    # or
    postman run /path/to/postman_collection.json
    ```


