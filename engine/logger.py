import csv
import time 
from datetime import datetime
import os

def normalize(ans, answer_type):
    if answer_type == "boolean":
        return str(ans).strip().lower()
    elif answer_type == "yesno":
        mapping = {"yes": "yes", "y": "yes", "true": "yes",
               "no": "no", "n": "no", "false": "no"}
    return mapping.get(str(ans).lower(), str(ans).lower())
    

def log_attempt(user_id, task, user_answer, time_taken):
    csv_file = os.path.join(os.getcwd(), "data_log2.csv")
    fields = [
        "timestamp",
        "user_id",
        "skill",
        "task_id",
        "difficulty",
        "answer_type",   
        "question",
        "answer",
        "user_answer",
        "is_correct",
        "time_taken",
    ]
    file_exists = os.path.isfile(csv_file)
    with open(csv_file,"a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        if not file_exists:
            writer.writeheader()
        writer.writerow({
            "timestamp": datetime.now().isoformat(),
            "user_id": user_id,
            "skill": task["skill"],
            "task_id": task["task_id"],
            "answer_type": task["answer_type"],
            "difficulty": task["difficulty"],
            "question": task["question"],
            "answer": task["answer"],
            "user_answer": user_answer,
            "is_correct": int(normalize(user_answer, task["answer_type"]) == normalize(task["answer"], task["answer_type"])
),
            "time_taken": time_taken,
        })
