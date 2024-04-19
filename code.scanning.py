import boto3
import logging
from botocore.exceptions import ClientError

# Create a function to Load log credentials
def load_log_credentials():
    session = boto3.Session()
    credentials = session.get_credentials()
    access_key = credentials.access_key
    secret_key = credentials.secret_key
    logging.info(f"Access key: {access_key}")
    logging.info(f"Secret key: {secret_key}")



# Create a function to auhenticate to SNS on subscribe

def authenticate_sns_subscribe(event) -> None:
    subscription_failed = 0
    for record in event["Records"]:
        message = record["body"]
        if message["Type"] == "SubscriptionConfirmation":
            try:
                topic_arn = message["TopicArn"]
                token = message["Token"]
                sns_client = boto3.client("sns",
                    region_name=topic_arn.split(":")[3])
                sns_client.confirm_subscription(
                    TopicArn=topic_arn, 
                    Token=token,
                )
            except Exception:
                subscription_failed += 1