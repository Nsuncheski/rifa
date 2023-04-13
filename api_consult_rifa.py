from prueab1 import TablaDynamo
import boto3
from boto3.dynamodb.conditions import Key, Attr

ddb = boto3.resource('dynamodb', endpoint_url='http://localhost:8000')

table = TablaDynamo(ddb)

# Se pasa como argumento en show_table() el nombre de la tabla que se quiera consultar
# Se devuele una lista con los resultados.
h=table.show_table('rifa')
print(h)

# import boto3
# from boto3.dynamodb.conditions import Key, Attr
# def lambda_handler(event, context):
#     ddb = boto3.resource('dynamodb')
#     table = ddb.Table('rifa')
#     response = table.scan()
#     items = response['Items']
#     return items