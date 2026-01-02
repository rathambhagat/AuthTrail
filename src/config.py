# Configuration File for AuthTrail - Discipline Edition

SCENARIOS = [
    # Scenario 0: Study Discipline
    {
        "command": "SOLVE_20_CALCULUS_PROBLEMS_CH3",
        "constraint": "Complete within 90 mins; NO solution manuals allowed.",
        "proof": "Written solutions photographed/uploaded clearly."
    },
    # Scenario 1: Focus Control
    {
        "command": "45_MINUTES_UNINTERRUPTED_STUDY",
        "constraint": "Zero phone usage or app switching.",
        "proof": "Timer completion and self-report confirmation."
    },
    # Scenario 2: Physical Discipline
    {
        "command": "30_PUSH_UPS_AND_30_SQUATS",
        "constraint": "One continuous session with correct form.",
        "proof": "Self-verification or short completion note."
    },
    # Scenario 3: Habit Building
    {
        "command": "WAKE_UP_BY_6_00_AM",
        "constraint": "Alarm must be silenced within 120 seconds.",
        "proof": "Timestamped confirmation entry."
    },
    # Scenario 4: Revision & Recall
    {
        "command": "REVISE_YESTERDAY_NOTES",
        "constraint": "25 minutes; No new material allowed.",
        "proof": "Key points written entirely from memory."
    }
]

# Allowed actions
VALID_ACTIONS = ["approve", "reject", "complete"]