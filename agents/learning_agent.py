import json

def get_learning_path(role):
    with open("data/certifications.json", "r") as f:
        data = json.load(f)

    for item in data:
        if item["role"].lower() == role.lower():
            return {
                "certification": item["id"],
                "skills": item["skills"],
                "recommended_hours": item["recommended_hours"]
            }

    return None