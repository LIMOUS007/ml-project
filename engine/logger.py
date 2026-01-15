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
    else:  
        return str(ans).strip()
    

def log_attempt(user_id, session_id, task_index, task, user_answer, time_taken, difficulty_before, difficulty_after):
    csv_file = os.path.join(os.getcwd(), "data_log1.csv")
    fields = [
        "timestamp",
        "user_id",
        "session_id",
        "task_index",
        "skill",
        "task_id",
        "difficulty_before",
        "difficulty_after",
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
            "session_id": session_id,
            "task_index": task_index,
            "skill": task["skill"],
            "task_id": task["task_id"],
            "difficulty_before": difficulty_before,
            "difficulty_after": difficulty_after,
            "answer_type": task["answer_type"],
            "question": task["question"],
            "answer": task["answer"],
            "user_answer": user_answer,
            "is_correct": int(normalize(user_answer, task["answer_type"]) == normalize(task["answer"], task["answer_type"])),
            "time_taken": time_taken,
        })
