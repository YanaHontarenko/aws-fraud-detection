def create_variables(client):
    """
    https://docs.aws.amazon.com/frauddetector/latest/ug/create-a-variable.html
    """

    # Create variable email_address
    client.create_variable(
        name='email_address',
        variableType='EMAIL_ADDRESS',
        dataSource='EVENT',
        dataType='STRING',
        defaultValue='<unknown>'
    )

    # Create variable ip_address
    client.create_variable(
        name='ip_address',
        variableType='IP_ADDRESS',
        dataSource='EVENT',
        dataType='STRING',
        defaultValue='<unknown>'
    )


def create_entity_type(client):
    """
    https://docs.aws.amazon.com/frauddetector/latest/ug/create-an-entity-type.html
    """
    client.put_event_type(
        name='sample_registration',
        eventVariables=['ip_address', 'email_address'],
        labels=['legit', 'fraud'],
        entityTypes=['sample_customer'])


def create_label(client):
    """
    https://docs.aws.amazon.com/frauddetector/latest/ug/create-a-label.html
    """
    client.put_label(
        name='fraud',
        description='label for fraud events'
    )

    client.put_label(
        name='legit',
        description='label for legitimate events'
    )


def create_event_type(client):
    """
    https://docs.aws.amazon.com/frauddetector/latest/ug/create-event-type.html
    """
    client.put_event_type(
        name='sample_registration',
        eventVariables=['ip_address', 'email_address'],
        labels=['legit', 'fraud'],
        entityTypes=['sample_customer'])


def create_rules(client):
    """
    https://docs.aws.amazon.com/frauddetector/latest/ug/create-a-rule.html
    """
    client.create_rule(
        ruleId='high_fraud_risk',
        detectorId='sample_detector',
        expression='$sample_fraud_detection_model_insightscore > 900',
        language='DETECTORPL',
        outcomes=['verify_customer']
    )

    client.create_rule(
        ruleId='medium_fraud_risk',
        detectorId='sample_detector',
        expression='$sample_fraud_detection_model_insightscore <= 900 and $sample_fraud_detection_model_insightscore > 700',
        language='DETECTORPL',
        outcomes=['review']
    )

    client.create_rule(
        ruleId='low_fraud_risk',
        detectorId='sample_detector',
        expression='$sample_fraud_detection_model_insightscore <= 700',
        language='DETECTORPL',
        outcomes=['approve']
    )


def create_outcomes(client):
    """
    https://docs.aws.amazon.com/frauddetector/latest/ug/create-an-outcome.html
    """
    client.put_outcome(
        name='verify_customer',
        description='this outcome initiates a verification workflow'
    )

    client.put_outcome(
        name='review',
        description='this outcome sidelines event for review'
    )

    client.put_outcome(
        name='approve',
        description='this outcome approves the event'
    )


# TODO: Add more parameters and comments
