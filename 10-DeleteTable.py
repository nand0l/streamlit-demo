import streamlit as st
import boto3
from datetime import datetime

# Display a title on the app
st.title('DynamoDB Table Deletion')

# Code to be displayed
code_to_display = """
import boto3
from datetime import datetime

print("Starting to delete the table")
# Get the service client.
client = boto3.client('dynamodb')

# Delete the table
client.delete_table(TableName='users')

print(str(datetime.now()) + " Deleting table")
# Wait for the table to be deleted
waiter = client.get_waiter('table_not_exists')
waiter.wait(TableName='users')

# Print Message when Job is done.
print(str(datetime.now()) + " table deleted")
"""

# Button to start table deletion process and display code
if st.button('Delete DynamoDB Table and Show Code'):

    start_time = datetime.now()
    st.write(f"{start_time} Starting to delete the table")
    st.code(code_to_display, language='python')
    # Actual code to delete the DynamoDB table
    try:
        client = boto3.client('dynamodb')
        client.delete_table(TableName='users')
        st.write(f"{datetime.now()} Deleting table")

        # Wait for the table to be deleted
        waiter = client.get_waiter('table_not_exists')
        waiter.wait(TableName='users')

        end_time = datetime.now()
        st.success(f"{end_time} Table deleted.")

        # Display the code after the button is clicked
        st.code(code_to_display, language='python')
    except Exception as e:
        st.error(f"Failed to delete table: {str(e)}")
