import boto3

# Conecta a DynamoDB Local
ddb = boto3.resource('dynamodb', endpoint_url='http://localhost:8000')

# Crea la tabla
table2 = ddb.create_table(
    TableName='TablaRifas',
    KeySchema=[
        {
            'AttributeName': 'rifa',
            'KeyType': 'HASH'  # Clave de partición
        },
        {
            'AttributeName': 'nombre',
            'KeyType': 'RANGE'  # Clave de partición
        }  
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'rifa',
            'AttributeType': 'N'
        },
        {
            'AttributeName': 'nombre',
            'AttributeType': 'S'
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)

# Espera a que la tabla se cree
table2.meta.client.get_waiter('table_exists').wait(TableName='TablaRifas')

print("La tabla se ha creado correctamente.")
