def prevent_attack(alerts):

    responses = []

    for alert in alerts:
        if "Brute force" in alert:
            responses.append("Blocked IP")

        if "Sensitive" in alert:
            responses.append("Restricted access")

    return responses
