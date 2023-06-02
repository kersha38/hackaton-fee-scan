import os

import boto3
from classes.rates_dynamo import *


def init_dynamo_session(name_table):
    session = boto3.session.Session(
        aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'],
        aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY'],
        aws_session_token=os.environ['AWS_SESSION_TOKEN'],
        region_name=os.environ['REGION'])
    dynamodb = session.resource('dynamodb')
    return dynamodb.Table(name_table)


def put_item(item, table_session):
    table_session.put_item(Item=item)


def create_rates_item(fee_list_scan: List[FeeByPaymentMethod]):
    fee_list_dynamo = []
    for fee_cell in fee_list_scan:
        fee_dynamo = RatesDynamo("20000000100592357000", fee_cell)
        dict_item = vars(fee_dynamo)
        fee_list_dynamo.append(dict_item)

    return fee_list_dynamo
