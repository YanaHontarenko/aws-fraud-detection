"""
https://docs.aws.amazon.com/frauddetector/latest/ug/building-a-model.html
"""


def create_model(client, model_id, event_type_name, model_type):
    client.create_model(modelId=model_id,
                        eventTypeName=event_type_name,
                        modelType=model_type)

    print("Model is created!")


def train_model(client, s3_file_location, role, model_id, model_type, variables, mapper):
    var_names = [variable["name"] for variable in variables]

    client.create_model_version(modelId=model_id,
                                modelType=model_type,
                                trainingDataSource='EXTERNAL_EVENTS',
                                trainingDataSchema={
                                    'modelVariables': var_names,
                                    'labelSchema': {
                                        'labelMapper': mapper
                                    }
                                },
                                externalEventsDetail={
                                    'dataLocation': s3_file_location,
                                    'dataAccessRoleArn': role
                                })

    print("Model training is started..")


def check_model(client, model_id, model_version, model_type):
    response = client.describe_model_versions(modelId=model_id,
                                              modelVersionNumber=model_version,
                                              modelType=model_type,
                                              nextToken='string',
                                              maxResults=1)

    return response["modelVersionDetails"][0]["status"]


def deploy_model(client, model_id, model_type, model_version):
    if check_model(client, model_id, model_type, model_version) == "TRAINING_COMPLETE":
        client.update_model_version_status(
            modelId=model_id,
            modelType=model_type,
            modelVersionNumber=model_version,
            status='ACTIVE'
        )
        print("Model deploying is started..")
    else:
        print("Training isn't completed")

# TODO: Add more comments
