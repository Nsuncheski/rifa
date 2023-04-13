from prueab1 import TablaDynamo
import boto3
from boto3.dynamodb.conditions import Key, Attr

ddb = boto3.resource('dynamodb', endpoint_url='http://localhost:8000')

table = TablaDynamo(ddb)
# Crea tabla con rifa, donde el primer argumento es el nombre de la tabla,
# segundo la 'partition key' 
# la columna por la cual se va a ordenar la rifa
table.create_table('rifa', 'rifa')


# *************CODIGO PARA AWS*******************
# import boto3
# from boto3.dynamodb.conditions import Key, Attr
# from prueab1 import TablaDynamo
# def lambda_handler(event, context):
#     ddb = boto3.resource('dynamodb')
#     table = TablaDynamo(ddb)
#     # Crea tabla con rifa, donde el primer argumento es el nombre de la tabla,
#     # segundo la 'partition key' 
#     # la columna por la cual se va a ordenar la rifa
#     table.create_table('rifa3', 'rifa', 'nombre')