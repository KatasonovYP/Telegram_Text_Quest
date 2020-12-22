import boto3



dynamodb = boto3.resource('dynamodb')



def add_user(data, act):
    table = dynamodb.Table('users')
    from_event = data['message']['from']
    user_info = {
        'user_id': str(from_event['id']),
        'first_name': from_event['first_name'],
        'event': act
    }
    if 'last_name' in from_event:
        user_info['last_name'] = from_event['last_name']
    if 'username' in from_event:
        user_info['username'] = from_event['username']
        
    table.put_item(
        Item=user_info
    )



def get_act(data):
    table = dynamodb.Table('users')
    from_event = data['message']['from']
    response = table.get_item(
        Key = {
            'user_id': str(from_event['id']),
            'first_name': from_event['first_name']
        }
    )
    item = response['Item']['event']
    return item



def create_table():
    table = dynamodb.create_table(
        TableName='users',
        KeySchema=[
            {
                'AttributeName': 'user_id',
                'KeyType': 'HASH'
            },
            {
                'AttributeName': 'first_name',
                'KeyType': 'RANGE'
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'user_id',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'first_name',
                'AttributeType': 'S'
            },
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
    )
    
    # Wait until the table exists.
    table.meta.client.get_waiter('table_exists').wait(TableName='users')
    
    # Print out some data about the table.
    print(table.item_count)

    