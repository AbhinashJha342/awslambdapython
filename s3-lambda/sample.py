import boto3
import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom
import io
import boto3
import logging as logger
import json as JSON

s3 = boto3.resource('s3')
bucket = s3.Bucket('s3-encora-task1')
bucket_name = "s3-encora-task1"


def printMessage(event, context):
    print(event)
    root = ET.Element("Reservation")
    m1 = ET.Element("header")
    root.append(m1)
    b1 = ET.SubElement(m1, "echoToken")
    b1.text = event['header']['echoToken']
    b2 = ET.SubElement(m1, "timestamp")
    b2.text = event['header']['timestamp']
    m2 = ET.Element("body")
    m3 = ET.Element("hotel")
    root.append(m2)
    m2.append(m3)
    c1 = ET.SubElement(m3, "uuid")
    c1.text = event['reservation']['hotel']['uuid']
    c2 = ET.SubElement(m3, "code")
    c2.text = event['reservation']['hotel']['code']
    c3 = ET.SubElement(m3, "offset")
    c3.text = event['reservation']['hotel']['offset']
    d1 = ET.SubElement(m2, "reservationId")
    d1.text = str(event['reservation']['reservationId'])
    m4 = ET.Element("reservations")
    childOrg = event['reservation']['confirmationNumbers'][0]['source']
    childConfNum = event['reservation']['confirmationNumbers'][0]['confirmationNumber']
    # missedNode
    missedNode1 = ET.Element("reservation")
    missedNode1.set('source', childOrg)
    m4.append(missedNode1)
    # ends here
    m2.append(m4)
    m5 = ET.Element("info")
    m5.set('confirmationNumber', childConfNum)
    m4.append(m5)
    childnodename = event['reservation']['confirmationNumbers'][0]['guest']
    e1 = ET.SubElement(m5, "firstName")
    e1.text = childnodename.split()[0]
    e2 = ET.SubElement(m5, "firstName")
    e2.text = childnodename.split()[1]
    # m6
    m6 = ET.Element("reservation")
    parentorg = event['reservation']['confirmationNumbers'][1]['source']
    parentconfnum = event['reservation']['confirmationNumbers'][1]['confirmationNumber']
    m6.set('source', parentorg)
    m4.append(m6)
    m7 = ET.Element("info")
    m7.set('confirmationNumber', parentconfnum)
    m6.append(m7)
    childNodeName = event['reservation']['confirmationNumbers'][1]['guest']
    e3 = ET.SubElement(m7, "firstName")
    e3.text = childNodeName.split()[0]
    e4 = ET.SubElement(m7, "firstName")
    e4.text = childNodeName.split()[1]
    # last section
    m8 = ET.Element("lastUpdateTimestamp")
    m8.text = event['reservation']['lastUpdateTimestamp']
    m2.append(m8)
    m9 = ET.Element("lastUpdateOperatorId")
    m9.text = event['reservation']['lastUpdateOperatorId']
    m2.append(m9)
    xmlstr = minidom.parseString(ET.tostring(root)).toprettyxml(indent="   ")
    # print(xmlstr)
    string_out = io.StringIO()
    string_out.write(xmlstr)
    # print(string_out.getvalue())
    s3.Object('s3-encora-task1', 'output.xml').put(Body=string_out.getvalue())
    # URL s3Url = s3Client.getUrl('s3-encora-task1', 'output.xml');
    # logger.info("S3 url is " + s3.getUrl('s3-encora-task1', 'output.xml'));
    location = boto3.client('s3').get_bucket_location(Bucket=bucket_name)['LocationConstraint']
    url = "https://s3-%s.amazonaws.com/%s/%s" % (location, bucket_name, 'output.xml')
    print(url)
    response = {
        "statusCode": 200
    }

    return response
