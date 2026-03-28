def detect_intrusion(logs):

    alerts = []

    for log in logs:
        if "FAILED LOGIN" in log:
            alerts.append("Brute force detected")

        if "confidential" in log:
            alerts.append("Sensitive data access")

    return alerts
