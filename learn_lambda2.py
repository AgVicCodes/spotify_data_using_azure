def learn_lambda(event, context):

    first_name = event['first_name']
    last_name = event['last_name']

    return greeting(first_name, last_name)

# Seperaring main logic from lambda handler
def greeting(first_name, last_name):
    message = "Hello {} {}!".format(first_name, last_name)
    return message

import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def learn_lambda(event, context):
    result = None
    action = event['action']
    if action == 'increment':
        result = event['number']
        logger.info(f'Calculated result of {result}')
    else:
        logger.error(f"{action} is not a valid action.")

    response = {'result': result}
    return response

import boto3
import botocore

def learn_lambda(event, context):
    return {
        'boto3 version': boto3.__version__,
        'botocore version': botocore.__version__
    }