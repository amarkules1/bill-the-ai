import boto3


def verify_email_identity():
    ses_client = boto3.client("ses", region_name="us-east-2")
    response = ses_client.verify_email_identity(
        EmailAddress="amarlar2354@gmail.com"
    )
    print(response)
