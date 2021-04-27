import json
import boto3
import logging
import os
import time
import uuid
import requests



def create(event, context):
    print("value: ")
    # create a response
    response = {
        "statusCode": 200,
        #"body": json.dumps(item)
    }

    return response