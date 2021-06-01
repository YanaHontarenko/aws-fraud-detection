"""
https://docs.aws.amazon.com/frauddetector/latest/ug/getting-fraud-predictions.html
"""
from dotenv import load_dotenv

import boto3
import os

load_dotenv()


def test_on_sample(client):
    response = client.get_event_prediction(
        detectorId='sample_detector',
        eventId='802454d3-f7d8-482d-97e8-c4b6db9a0428',
        eventTypeName='sample_registration',
        eventTimestamp='2020-07-13T23:18:21Z',
        entities=[{'entityType': 'sample_customer', 'entityId': '12345'}],
        eventVariables={
            'email_address': 'johndoe@exampledomain.com',
            'ip_address': '1.2.3.4'
        }
    )

    return response['modelScores'][0]["scores"]["sample_fraud_detection_model_insightscore"], \
           response['ruleResults'][0]["ruleId"], \
           response['ruleResults'][0]["outcomes"]


def test_on_batch(client):
    """TODO: Implement testing on batch"""

# TODO: Add more comments


if __name__ == "__main__":
    aws_access_key_id = os.environ.get("AWS_ACCESS_KEY_ID")
    aws_secret_access_key = os.environ.get("AWS_SECRET_ACCESS_KEY")
    region_name = os.environ.get("REGION_NAME")

    client = boto3.client("frauddetector",
                          aws_access_key_id=aws_access_key_id,
                          aws_secret_access_key=aws_secret_access_key,
                          region_name=region_name)
    score, rule, outcomes = test_on_sample(client)
    print(f"Score: {score}")
    print(f"Rule: {rule}")
    print(f"Score: {outcomes[0]}")
