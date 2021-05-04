import json

def create(event, context):
    print("value: ")
    # create a response
    response = {
        "statusCode": 200,
        #"body": json.dumps(item)
    }

    return response