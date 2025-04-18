FROM public.ecr.aws/lambda/python:3.11

ARG PATH_TO_LAMBDA_CODE=lambdas/test

# Copy the lambda code into the container
COPY ${PATH_TO_LAMBDA_CODE}/main.py ${LAMBDA_TASK_ROOT}
COPY ${PATH_TO_LAMBDA_CODE}/requirements.txt ${LAMBDA_TASK_ROOT}

# Install dependencies
RUN pip install -r ${LAMBDA_TASK_ROOT}/requirements.txt

# Set the CMD to your handler start function
CMD [ "main.handler" ]
