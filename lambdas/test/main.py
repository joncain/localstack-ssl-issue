import logging
import json
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa

import snowflake.snowpark as snowpark
import boto3


# Set up logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

secrets = boto3.client('secretsmanager')


def handler(event, context):
    try:
        logger.info(f"Received event")

        # # Execute a SELECT that returns a significant amount of data. In my case it appears Snowflake was returning ~2.5MB of data.
        sql = """
        SELECT
            * 
        FROM
            foo
        """

        # Enter your Snowflake information here
        config = {
            "account": "",
            "user": "",
            "password": "",
            "role": "",
            "warehouse": "",
            "database": "",
            "schema": ""
        }

        # I use a private key to authenticate to Snowflake. You probably don't need this.
        # resp = secrets.get_secret_value(SecretId="")
        # secret = json.loads(resp['SecretString'])
        # config.update({
        #     "account": secret['account'],
        #     "user": secret['username'],
        #     "private_key": load_private_key(secret['private_key']),
        #     "role": secret['role'],
        #     "warehouse": "",
        #     "database": "",
        #     "schema": ""
        # })

        session = snowpark.Session.builder.configs(config).create()
        df = session.sql(sql).to_pandas()
        logger.info(f"DataFrame: {df}")

    except Exception as e:
        logger.error(f"Error processing event: {str(e)}")
        raise e 


def load_private_key(private_key: bytes | str) -> rsa.RSAPrivateKey:
    """Load a private key from PEM format.

    Args:
        private_key: The private key in PEM format, either as bytes or string

    Returns:
        RSAPrivateKey: The loaded private key object
    """
    if isinstance(private_key, str):
        private_key = private_key.encode('utf-8')

    return serialization.load_pem_private_key(
        private_key,
        password=None,
    )
