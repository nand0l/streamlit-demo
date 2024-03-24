import boto3

# Get the service resource.
dynamodb = boto3.resource('dynamodb')

# Connect to the table 'users'
table = dynamodb.Table('users')

# Perform a put_item operation and request the total consumed capacity
response = table.put_item(
    Item={
        'username': 'janedoe',
        'first_name': 'Jane',
        'last_name': 'Doe',
        'age': 26,
        'account_type': 'standard_user',
    },
    ReturnConsumedCapacity='TOTAL'
)

# Print out the response to see the consumed capacity
print(response)

# If you specifically want to print the consumed capacity part
if 'ConsumedCapacity' in response:
    print("Consumed capacity:", response['ConsumedCapacity'])
else:
    print("No consumed capacity information returned.")
