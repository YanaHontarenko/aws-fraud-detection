"""
https://docs.aws.amazon.com/frauddetector/latest/ug/building-a-model.html
"""


def create_model(client):
    client.create_model(
        modelId='sample_fraud_detection_model',
        eventTypeName='sample_registration',
        modelType='ONLINE_FRAUD_INSIGHTS')


def train_model(client, s3_file_location, role):
    client.create_model_version(
        modelId='sample_fraud_detection_model',
        modelType='ONLINE_FRAUD_INSIGHTS',
        trainingDataSource='EXTERNAL_EVENTS',
        trainingDataSchema={
            'modelVariables': ['ip_address', 'email_address'],
            'labelSchema': {
                'labelMapper': {
                    'FRAUD': ['fraud'],
                    'LEGIT': ['legit']
                }
            }
        },
        externalEventsDetail={
            'dataLocation': s3_file_location,
            'dataAccessRoleArn': role
        }
    )


def check_model(client):
    response = client.describe_model_versions(
        modelId='sample_fraud_detection_model',
        modelVersionNumber='1.0',
        modelType='ONLINE_FRAUD_INSIGHTS',
        nextToken='string',
        maxResults=1
    )

    return response["modelVersionDetails"][0]["status"]


def deploy_model(client):
    if check_model(client) == "TRAINING_COMPLETE":
        client.update_model_version_status(
            modelId='sample_fraud_detection_model',
            modelType='ONLINE_FRAUD_INSIGHTS',
            modelVersionNumber='1.00',
            status='ACTIVE'
        )
    else:
        return "Training isn't complete"

# TODO: Add more parameters and comments
