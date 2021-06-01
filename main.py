# TODO: Add data

from create_components import *
from model_building import *
from detector_building import *
from dotenv import load_dotenv

import boto3
import os

load_dotenv()

if __name__ == "__main__":

    variables = [
        {
            "name": "email_address",
            "type": "EMAIL_ADDRESS",
            "source": "EVENT",
            "data_type": "STRING",
            "default": "<unknown>"
        },
        {
            "name": "ip_address",
            "type": "IP_ADDRESS",
            "source": "EVENT",
            "data_type": "STRING",
            "default": "<unknown>"
        },
    ]
    entity_type_name = "sample_customer"
    entity_type_description = "sample customer entity type"
    labels = [
        {
            "name": "fraud",
            "description":"label for fraud events"
        },
        {
            "name": "legit",
            "description": "label for legitimate events"
        }
    ]
    event_type_name = "sample_registration"
    mapper = {
        'FRAUD': ['fraud'],
        'LEGIT': ['legit']
    }
    outcomes = [
        {
            "name": "verify_customer",
            "description": "this outcome initiates a verification workflow"
        },
        {
            "name": "review",
            "description": "this outcome sidelines event for review"
        },
        {
            "name": "approve",
            "description": "this outcome approves the event"
        }
    ]
    rules = [
        {
            "name": "high_fraud_risk",
            "expression": "$sample_fraud_detection_model_insightscore > 900",
            "outcome": outcomes[0]["name"]
        },
        {
            "name": "medium_fraud_risk",
            "expression": "$sample_fraud_detection_model_insightscore <= 900 and $sample_fraud_detection_model_insightscore > 700",
            "outcome": outcomes[1]["name"]
        },
        {
            "name": "low_fraud_risk",
            "expression": "$sample_fraud_detection_model_insightscore <= 700",
            "outcome": outcomes[2]["name"]
        }
    ]
    aws_access_key_id = os.environ.get("AWS_ACCESS_KEY_ID")
    aws_secret_access_key = os.environ.get("AWS_SECRET_ACCESS_KEY")
    region_name = os.environ.get("REGION_NAME")
    model_id = os.environ.get("MODEL_ID")
    model_type = os.environ.get("MODEL_TYPE")
    model_version = os.environ.get("MODEL_VERSION")
    detector_id = os.environ.get("DETECTOR_ID")
    detector_version = os.environ.get("DETECTOR_VERSION")
    rule_execution_mode = os.environ.get("RULE_EXECUTION_MODE")
    s3_input = os.environ.get("S3_INPUT")
    s3_output = os.environ.get("S3_output")
    role_arn = os.environ.get("ROLE_ARN")

    client = boto3.client("frauddetector",
                          aws_access_key_id=aws_access_key_id,
                          aws_secret_access_key=aws_secret_access_key,
                          region_name=region_name)

    create_variables(client, variables)
    create_entity_type(client, entity_type_name, entity_type_description)
    create_label(client, labels)
    create_event_type(client, event_type_name, variables, labels, entity_type_name)
    create_model(client, model_id, event_type_name, model_type)
    train_model(client, s3_input, role_arn, model_id, model_type, variables, mapper)
    deploy_model(client, model_id, model_type, model_version)
    create_detector(client, detector_id, event_type_name)
    create_outcomes(client, outcomes)
    create_rules(client, rules, detector_id)
    create_detector_version(client, detector_id, rules, model_id, model_type, model_version, rule_execution_mode)
    deploy_detector(client, detector_id, detector_version)
