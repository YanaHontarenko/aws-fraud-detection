"""
https://docs.aws.amazon.com/frauddetector/latest/ug/building-a-model.html
"""

from model_building import check_model


def create_detector(client):
    client.put_detector(
        detectorId='sample_detector',
        eventTypeName='sample_registration'
    )


def create_detector_version(client):
    client.create_detector_version(
        detectorId='sample_detector',
        rules=[{
            'detectorId': 'sample_detector',
            'ruleId': 'high_fraud_risk',
            'ruleVersion': '1'
        },
        {
            'detectorId': 'sample_detector',
            'ruleId': 'medium_fraud_risk',
            'ruleVersion': '1'
        },
        {
            'detectorId': 'sample_detector',
            'ruleId': 'low_fraud_risk',
            'ruleVersion': '1'
        }],
        modelVersions=[{
            'modelId': 'sample_fraud_detection_model',
            'modelType': 'ONLINE_FRAUD_INSIGHTS',
            'modelVersionNumber': '1.00'
        }],
        ruleExecutionMode='FIRST_MATCHED'
    )


def check_detector(client):
    response = client.describe_detector(
        detectorId='sample_detector',
        nextToken='string',
        maxResults=1000
    )

    return response["detectorVersionSummaries"][0]["status"]


def deploy_detector(client):
    if check_detector(client) == "DRAFT":
        client.update_detector_version_status(
            detectorId='sample_detector',
            detectorVersionId='1',
            status='ACTIVE'
        )
    else:
        return "Activating isn't complete"

# TODO: Add more parameters and comments
