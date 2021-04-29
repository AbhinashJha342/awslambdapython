import json
import boto3
from dicttoxml import dicttoxml
#from json2xml import json2xml
#from json2xml.utils import readfromurl, readfromstring, readfromjson

s3 = boto3.client('s3')


def printMessage(event, context):
	print(event['header']['echoToken'])
	print(":::::::keys are::::::",event.keys())
	xml = dicttoxml(event, custom_root='test', attr_type=False)
	#print(json2xml.Json2xml(event).to_xml())
	response = {
        "statusCode": 200
    }

	return response