def create_variables(client, variables):
    """
    https://docs.aws.amazon.com/frauddetector/latest/ug/create-a-variable.html
    """

    for variable in variables:
        client.create_variable(name=variable["name"],
                               variableType=variable["type"],
                               dataSource=variable["source"],
                               dataType=variable["data_type"],
                               defaultValue=variable["default"])

    print("Variables are created!")


def create_entity_type(client, entity_type_name, entity_type_description):
    """
    https://docs.aws.amazon.com/frauddetector/latest/ug/create-an-entity-type.html
    """
    client.put_entity_type(name=entity_type_name,
                           description=entity_type_description)

    print("Entity type is created!")


def create_label(client, labels):
    """
    https://docs.aws.amazon.com/frauddetector/latest/ug/create-a-label.html
    """

    for label in labels:
        client.put_label(name=label["name"],
                         description=label["description"])

    print("Labels are created!")


def create_event_type(client, event_type_name, variables, labels, entity_type_name):
    """
    https://docs.aws.amazon.com/frauddetector/latest/ug/create-event-type.html
    """
    var_names = [variable["name"] for variable in variables]
    label_names = [label["name"] for label in labels]

    client.put_event_type(name=event_type_name,
                          eventVariables=var_names,
                          labels=label_names,
                          entityTypes=[entity_type_name])

    print("Event type is created!")


def create_rules(client, rules, detector_id):
    """
    https://docs.aws.amazon.com/frauddetector/latest/ug/create-a-rule.html
    """

    for rule in rules:
        client.create_rule(ruleId=rule["rule_id"],
                           detectorId=detector_id,
                           expression=rule["expression"],
                           language='DETECTORPL',
                           outcomes=[rule["outcome"]])

    print("Rules are created")


def create_outcomes(client, outcomes):
    """
    https://docs.aws.amazon.com/frauddetector/latest/ug/create-an-outcome.html
    """

    for outcome in outcomes:
        client.put_outcome(name=outcome["name"],
                           description=outcome["description"])

    print("Outcomes are created!")


# TODO: Add comments
