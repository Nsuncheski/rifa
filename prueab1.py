import logging
from boto3.dynamodb.conditions import Key, Attr


logger = logging.getLogger()


class TablaDynamo:
    """Encapsulates an Amazon DynamoDB table of movie data."""
    def __init__(self, ddb):
        """
        :param ddb: A Boto3 DynamoDB resource.
        """
        self.ddb = ddb
        self.table = None
        self.rifa_amount = None
        self.table_name = None

    def create_table(self, table_name, partition_key, rifa_amount:int=100):
        """
        Creates an Amazon DynamoDB table that can be used to store movie data.
        The table uses the release year of the movie as the partition key and the
        title as the sort key.

        :param table_name: The name of the table to create.
        :return: The newly created table.
        """
        try:
            self.rifa_amount = rifa_amount
            self.table_name = table_name
            self.table = self.ddb.create_table(
                TableName=table_name,
                KeySchema=[
                    {'AttributeName': partition_key, 'KeyType': 'HASH'} # Partition key
                ],
                AttributeDefinitions=[
                    {'AttributeName': partition_key, 'AttributeType': 'N'},
                ],
                ProvisionedThroughput={'ReadCapacityUnits': 10, 'WriteCapacityUnits': 10})
            self.table.wait_until_exists()
            for i in range(rifa_amount):
                self.insert_rifa(rifa=i, nombre=' ', celular=0, email=' ', vendida=False)
        except ClientError as err:
            logger.error(
                "Couldn't create table %s. Here's why: %s: %s", table_name,
                err.response['Error']['Code'], err.response['Error']['Message'])
            raise
        else:
            return self.table, self.rifa_amount, self.table_name

    def insert_rifa(self, rifa:int, nombre:str='', celular:int=0, email:str='', vendida:bool=False):
        """
        Inserts a new movie into the table.

        :param year: The release year of the movie.
        :param title: The title of the movie.
        :param info: Additional information about the movie, stored as a dictionary.
        :return: The response from the DynamoDB put_item operation.
        """
        item = {
            'rifa': rifa,
            'nombre': nombre,
            'celular': celular,
            'email': email,
            'vendida': vendida
        }
        try:
            response = self.table.put_item(Item=item)
        except ClientError as err:
            logger.error("No se pudo insertar los datos")


    def buy_rifa(self, table_name, event_dict):
        table = self.ddb.Table(table_name)
        for rifa in event_dict['rifas']:
            table.update_item(
                TableName=table_name,
                Key={'rifa': rifa},
                UpdateExpression='SET celular = :cel, nombre = :nombre, vendida = :ven, email = :ema',
                ExpressionAttributeValues={
                    ':cel':event_dict['cel'],
                    ':nombre':event_dict['name'],
                    ':ven':event_dict['vendida'],
                    ':ema':event_dict['email']
                }
            )   
            
    def show_table(self, table_name):
        lista_datos = []
        tabla= self.ddb.Table(table_name)
        for i in range(100):
            response = tabla.query(
            KeyConditionExpression=Key('rifa').eq(i)
            )
            lista_datos.append(response['Items'])
        return lista_datos

class ClientError(Exception):
    pass

