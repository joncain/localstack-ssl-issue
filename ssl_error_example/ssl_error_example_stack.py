from aws_cdk import (
    Duration,
    Stack,
    aws_lambda as lambda_,
)
from constructs import Construct

class SslErrorExampleStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create a Lambda function to process uploaded files
        lambda_fn = lambda_.DockerImageFunction(
            self,
            "TestLambda",
            function_name="TestLambda",
            code=lambda_.DockerImageCode.from_image_asset(
                directory=".",
                file="lambdas/test/Dockerfile"
            ),
            timeout=Duration.seconds(300),
            memory_size=1024,
            architecture=lambda_.Architecture.ARM_64,
        )
