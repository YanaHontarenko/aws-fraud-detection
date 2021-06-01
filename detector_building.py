"""
https://docs.aws.amazon.com/frauddetector/latest/ug/building-a-model.html
"""


def create_detector(client, detector_id, event_type_name):
    client.put_detector(detectorId=detector_id,
                        eventTypeName=event_type_name)

    print("Detector is created")


def create_detector_version(client, detector_id, rules, model_id, model_type, model_version, rule_execution_mode):
    detection_rules = []
    for rule in rules:
        detection_rules.append({
            "detectorId": detector_id,
            "ruleId": rule['name'],
            "ruleVersion": "1"
        })

    client.create_detector_version(detectorId=detector_id,
                                   rules=detection_rules,
                                   modelVersions=[{
                                       'modelId': model_id,
                                       'modelType': model_type,
                                       'modelVersionNumber': model_version
                                   }],
                                   ruleExecutionMode=rule_execution_mode)

    print("Detector version is created!")


def check_detector(client, detector_id):
    response = client.describe_detector(detectorId=detector_id,
                                        nextToken='string',
                                        maxResults=1000)

    return response["detectorVersionSummaries"][0]["status"]


def deploy_detector(client, detector_id, detector_version):
    if check_detector(client, detector_id) == "DRAFT":
        client.update_detector_version_status(
            detectorId=detector_id,
            detectorVersionId=detector_version,
            status='ACTIVE'
        )
        print("Detector is activated!")
        return True
    else:
        print("Detector isn't created")
        return False

# TODO: Add more comments
