import boto3

client = boto3.client('dynamodb', endpoint_url='http://localhost:8000')
response = client.describe_table(
    TableName='NOMBRE_DE_TU_TABLA'
)
arn = response['Table']['TableArn']


import os
import subprocess
def deploy_serverless():
    # Navigate to the directory that contains the Serverless YAML file
    os.chdir('/path/to/serverless/yaml')
    # Deploy the Serverless stack
    subprocess.call(['serverless', 'deploy'])
# ****************YAML SERVERLESS FRAMEWORK PARA CREAR PERMISOS SOBRE LAS TABLAS DDB QUE SE CREAN*************
# service: my-fastapi-app
# plugins:
#   - serverless-python-requirements
# provider:
#   name: aws
#   runtime: python3.8
# functions:
#   fastapi:
#     handler: main.handler
#     events:
#       - http:
#           path: /
#           method: any
#     environment:
#       DYNAMODB_TABLE_1: ${self:service}-table-1
#       DYNAMODB_TABLE_2: ${self:service}-table-2
#       # ... Agrega aquí todas las variables de entorno que necesites
# resources:
#   Resources:
#     Table1:
#       Type: AWS::DynamoDB::Table
#       Properties:
#         TableName: ${self:service}-table-1
#         AttributeDefinitions:
#           - AttributeName: id
#             AttributeType: S
#         KeySchema:
#           - AttributeName: id
#             KeyType: HASH
#         BillingMode: PAY_PER_REQUEST
#     Table2:
#       Type: AWS::DynamoDB::Table
#       Properties:
#         TableName: ${self:service}-table-2
#         AttributeDefinitions:
#           - AttributeName: id
#             AttributeType: S
#         KeySchema:
#           - AttributeName: id
#             KeyType: HASH
#         BillingMode: PAY_PER_REQUEST
#     # Agrega permisos para la función de Lambda
#     LambdaExecutionRole:
#       Type: AWS::IAM::Role
#       Properties:
#         RoleName: ${self:service}-lambda-role
#         AssumeRolePolicyDocument:
#           Version: "2012-10-17"
#           Statement:
#             - Effect: Allow
#               Principal:
#                 Service:
#                   - lambda.amazonaws.com
#               Action:
#                 - sts:AssumeRole
#         Policies:
#           - PolicyName: ${self:service}-dynamodb-access
#             PolicyDocument:
#               Version: "2012-10-17"
#               Statement:
#                 - Effect: Allow
#                   Action:
#                     - dynamodb:GetItem
#                     - dynamodb:PutItem
#                     - dynamodb:UpdateItem
#                     - dynamodb:DeleteItem
#                     - dynamodb:Scan
#                     - dynamodb:Query
#                   Resource:
#                     - !Sub "arn:aws:dynamodb:${self:provider.region}:*:table/${self:service}-table-1"
#                     - !Sub "arn:aws:dynamodb:${self:provider.region}:*:table/${self:service}-table-2"