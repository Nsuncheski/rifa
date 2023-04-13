import boto3


dynamodb = boto3.resource('dynamodb', endpoint_url='http://localhost:8000')

# Selecciona la tabla
table = dynamodb.Table('TablaRifas')

# Inserta valores en la columna 'rifa'
with table.batch_writer() as batch:
    for i in range(100):
        batch.put_item(Item={
            'rifa': str(i)
        })

print('Los valores se han insertado correctamente.')