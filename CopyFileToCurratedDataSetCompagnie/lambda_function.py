"""
Decription :

This Lambda function performs the following actions:
    * If the file is valid, meaning that it is in CSV format, non-empty, and has a line separator 
    of (";" or "\t") the file is transferred to the S3 bucket after converting it to UTF-8
    "xxx-datalake-9443-0190-4016-curated" with the following folder 
    structure: "eu-totalenergies-datalake-9443-0190-4016-curated/application/YYYY/MM/DD/file.csv"
      
    * Otherwise, the file is transferred to the "xxx-datalake-9443-0190-4016-error" 
    bucket with the following folder structure: 
      


Date V1 : 23/03/2023
Date V2 : 24/03/2023
"""
import datetime

#import time
import codecs
#import botocore
import boto3



today = datetime.date.today()

def lambda_handler(event, context):
    """
    AWS Lambda function handler.

    :param event: A dictionary containing event data.
    :type event: dict
    :param context: An object containing information about the current execution context.
    :return: A dictionary containing the Lambda function's response.
    """

    print(event)
    print("Hello World")
    
