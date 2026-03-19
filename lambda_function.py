import json
import boto3
import uuid

dynamodb = boto3.resource("dynamodb", region_name="eu-north-1")
table = dynamodb.Table("mesagesss")

def lambda_handler(event, context):

```
message = "No message"
if event.get("queryStringParameters"):
    message = event["queryStringParameters"].get("message", "No message")

table.put_item(
    Item={
        "id": str(uuid.uuid4()),
        "message": message
    }
)

return {
    "statusCode": 200,
    "body": json.dumps("Message saved successfully!")
}
```
