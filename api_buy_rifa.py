from prueab1 import TablaDynamo
import boto3
from boto3.dynamodb.conditions import Key, Attr

ddb = boto3.resource('dynamodb', endpoint_url='http://localhost:8000')

table = TablaDynamo(ddb)
event_dict = {'name':'nahuel', 'cel':3546, 'vendida':True,
              'email':'naubera@gmail.com', 'rifas':[5,10,55,22,14]}
table.buy_rifa('rifa', event_dict)


# import boto3
# from boto3.dynamodb.conditions import Key, Attr
# ddb = boto3.resource('dynamodb')
# def lambda_handler(event, context):
#     event_dict = event['event_dict']
#     table = ddb.Table('nombre_de_la_tabla_dynamodb')
#     table.buy_rifa('rifa', event_dict)