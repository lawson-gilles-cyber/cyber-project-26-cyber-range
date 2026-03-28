# Cyber Range Simulation

from attack.attacker import launch_attack
from system.target_system import process_activity
from defense.ids import detect_intrusion
from defense.ips import prevent_attack
from defense.soc import analyze_security

print("=== Cyber Range Simulation ===\n")

# Step 1: Attack
activities = launch_attack()

# Step 2: System processes activity
logs = process_activity(activities)

# Step 3: IDS detects threats
alerts = detect_intrusion(logs)

# Step 4: IPS blocks threats
responses = prevent_attack(alerts)

# Step 5: SOC analyzes everything
analyze_security(logs, alerts, responses)
