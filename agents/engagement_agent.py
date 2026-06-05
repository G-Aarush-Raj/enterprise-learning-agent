import json

def get_study_recommendation(employee_id):

    with open("data/workload.json", "r") as f:
        data = json.load(f)

    for employee in data:

        if employee["employee_id"] == employee_id:

            if employee["meeting_hours"] > 20:
                recommendation = (
                    f"Schedule study sessions during "
                    f"{employee['preferred_slot']} focus hours."
                )
            else:
                recommendation = (
                    f"Use 1-2 hour study blocks in the "
                    f"{employee['preferred_slot']}."
                )

            return recommendation

    return "No workload data found."