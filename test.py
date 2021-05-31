"""
https://docs.aws.amazon.com/frauddetector/latest/ug/getting-fraud-predictions.html
"""

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

    return response['modelScores'][0]["scores"], response['ruleResults'][0]


def test_on_batch(client):
    """TODO: Implement testing on batch"""

# TODO: Add more parameters and comments