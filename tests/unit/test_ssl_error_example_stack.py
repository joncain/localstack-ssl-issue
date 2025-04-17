import aws_cdk as core
import aws_cdk.assertions as assertions

from ssl_error_example.ssl_error_example_stack import SslErrorExampleStack

# example tests. To run these tests, uncomment this file along with the example
# resource in ssl_error_example/ssl_error_example_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = SslErrorExampleStack(app, "ssl-error-example")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
