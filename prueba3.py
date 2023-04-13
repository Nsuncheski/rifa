import boto3

ddb = boto3.resource('dynamodb', endpoint_url='http://localhost:8000')

table = ddb.Table('peliculas')

print(table.creation_date_time)