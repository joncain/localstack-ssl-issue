
1. Activate virtualenv
    ```bash
    $ source .venv/bin/activate
    ```

2. Once the virtualenv is activated, you can install the required dependencies.

    ```bash
    $ pip install -r requirements.txt
    ```

3. Bootstrap CDK

    ```bash
    $ cdklocal --profile localstack bootstrap
    ```

4. Deploy to localstack

    ```bash
    cdklocal --profile localstack deploy --require-approval never
    ```

5. Invoke Lambda and inspect the logs