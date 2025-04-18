1. Activate virtualenv
    ```bash
    $ source .venv/bin/activate
    ```

1. Once the virtualenv is activated, you can install the required dependencies.

    ```bash
    $ pip install -r requirements.txt
    ```
1. Modify the lambdas/test/main.py file to include your test query and connection info

1. Bootstrap CDK

    ```bash
    $ cdklocal --profile localstack bootstrap
    ```

1. Deploy to localstack

    ```bash
    cdklocal --profile localstack deploy --require-approval never
    ```

1. Invoke Lambda (region is us-west-1) and inspect the logs
