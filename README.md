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

Expected Error:

```
snowflake.connector.vendored.urllib3.exceptions.MaxRetryError: HTTPSConnectionPool(host='sfc-prod3-ds1-20-customer-stage.s3.us-west-2.amazonaws.com', port=443): Max retries exceeded with url: /cdic0000-s/results/01bbc5fb-0305-0388-003d-0e0713080e16_0/main/data_0_0_5_1?x-amz-server-side-encryption-customer-algorithm=AES256&response-content-encoding=gzip&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20250418T145144Z&X-Amz-SignedHeaders=host&X-Amz-Expires=21599&X-Amz-Credential=AKIA5YS3OHMWJ7DHC2VK%2F20250418%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Signature=de47daaeaf8258a5b313a98e3283dd07041dda6ab63bfb9cc168e252e18158e0 (Caused by SSLError(CertificateError("hostname 'sfc-prod3-ds1-20-customer-stage.s3.us-west-2.amazonaws.com' doesn't match either of 'localhost.localstack.cloud', '*.amplifyapp.localhost.localstack.cloud', '*.cloudfront.localhost.localstack.cloud', '*.dkr.ecr.eu-central-1.localhost.localstack.cloud', '*.dkr.ecr.eu-west-1.localhost.localstack.cloud', '*.dkr.ecr.us-east-1.localhost.localstack.cloud', '*.dkr.ecr.us-east-2.localhost.localstack.cloud', '*.dkr.ecr.us-west-1.localhost.localstack.cloud', '*.dkr.ecr.us-west-2.localhost.localstack.cloud', '*.elb.localhost.localstack.cloud', '*.eu-central-1.opensearch.localhost.localstack.cloud', '*.eu-west-1.opensearch.localhost.localstack.cloud', '*.execute-api.localhost.localstack.cloud', '*.lambda-url.eu-central-1.localhost.localstack.cloud', '*.lambda-url.eu-west-1.localhost.localstack.cloud', '*.lambda-url.us-east-1.localhost.localstack.cloud', '*.lambda-url.us-east-2.localhost.localstack.cloud', '*.lambda-url.us-west-1.localhost.localstack.cloud', '*.lambda-url.us-west-2.localhost.localstack.cloud', '*.localhost.localstack.cloud', '*.opensearch.localhost.localstack.cloud', '*.s3-website.localhost.localstack.cloud', '*.s3.localhost.localstack.cloud', '*.scm.localhost.localstack.cloud', '*.snowflake.localhost.localstack.cloud', '*.us-east-1.opensearch.localhost.localstack.cloud', '*.us-east-2.opensearch.localhost.localstack.cloud', '*.us-west-1.opensearch.localhost.localstack.cloud', '*.us-west-2.opensearch.localhost.localstack.cloud', 'sqs.eu-central-1.localhost.localstack.cloud', 'sqs.eu-west-1.localhost.localstack.cloud', 'sqs.us-east-1.localhost.localstack.cloud', 'sqs.us-east-2.localhost.localstack.cloud', 'sqs.us-west-1.localhost.localstack.cloud', 'sqs.us-west-2.localhost.localstack.cloud'")))
```
