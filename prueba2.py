from prueab1 import TablaDynamo
import boto3
from boto3.dynamodb.conditions import Key, Attr

ddb = boto3.resource('dynamodb', endpoint_url='http://localhost:8000')

table = TablaDynamo(ddb)
table.create_table('rifa3', 'rifa', 'nombre')
table.show_table()
# consultar tabla
tabla= ddb.Table('rifa1')
response = tabla.query(
    KeyConditionExpression=Key('rifa').eq(55)
)
items = response['Items']
print(items)
# consultar todos los datos del 0 al 100
lista1 = []
for i in range(100):
    response = tabla.query(
    KeyConditionExpression=Key('rifa').eq(i)
    )
    lista1.append(response['Items'])
print(lista1)

# agregar rifas nuevas