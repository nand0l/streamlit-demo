import streamlit as st
import boto3
from datetime import datetime

# Display a title on the app
st.title('DynamoDB Table Creation')

# Importing the SDK (assumed to be boto3 in a standard environment)
ddb_req = boto3

# Button to start table creation process
if st.button('Create DynamoDB Table'):

    start_time = datetime.now()
    st.write(f"{start_time} Starting to create table")

    # Get the service resource.
    dynamodb = ddb_req.resource('dynamodb')

    # Create the DynamoDB table.
    try:
        table = dynamodb.create_table(
            TableName='users',
            KeySchema=[
                {
                    'AttributeName': 'username',
                    'KeyType': 'HASH'
                },
                {
                    'AttributeName': 'last_name',
                    'KeyType': 'RANGE'
                }
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'username',
                    'AttributeType': 'S'
                },
                {
                    'AttributeName': 'last_name',
                    'AttributeType': 'S'
                },
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 1,
                'WriteCapacityUnits': 1
            }
        )
        st.success("Table creation initiated")

        # Wait until the table exists.
        table.meta.client.get_waiter('table_exists').wait(TableName='users')

        end_time = datetime.now()
        elapsed_time = end_time - start_time
        st.write(f"{end_time} Table created with: {table.item_count} Items.")
        st.write(f"Elapsed time for table creation: {elapsed_time}")
    except Exception as e:
        st.error(f"Failed to create table: {str(e)}")
