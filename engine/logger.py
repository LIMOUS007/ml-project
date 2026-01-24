import csv
import time 
from datetime import datetime
import os

def normalize(ans, answer_type):
    s = str(ans).strip().lower()
    if s == "":
        return None
    if answer_type == "boolean":
        mapping = {
            "true": "true", "t": "true", "1": "true",
            "false": "false", "f": "false", "0": "false"
        }
        return mapping.get(s, s)
    if answer_type == "yesno":
        mapping = {"yes": "yes", "y": "yes", "true": "yes", "t": "yes", "1": "yes",
            "no": "no", "n": "no", "false": "no", "f": "no", "0": "no"
        }
        return mapping.get(s, s)
    if answer_type == "integer":
        try:
            return str(int(s))
        except:
            return None
    return s
    

def log_attempt(user_id, session_id, task_index, task, user_answer, time_taken, difficulty_before, difficulty_after, delta, p_correct, expected_time):
    csv_file = os.path.join(os.getcwd(), "data_log.csv")
    fields = [
        "timestamp",
        "user_id",
        "session_id",
        "task_index",
        "skill",
        "task_id",
        "difficulty_before",
        "difficulty_after",
        "delta",
        "answer_type",
        "question",
        "answer",
        "user_answer",
        "is_correct",
        "time_taken",
        "p_correct",
        "expected_time"
    ]
    file_exists = os.path.isfile(csv_file)
    with open(csv_file,"a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        if not file_exists:
            writer.writeheader()
        norm_user = normalize(user_answer, task["answer_type"])
        norm_ans = normalize(task["answer"], task["answer_type"])
        writer.writerow({
            "timestamp": datetime.now().isoformat(),
            "user_id": user_id,
            "session_id": session_id,
            "task_index": task_index,
            "skill": task["skill"],
            "task_id": task["task_id"],
            "difficulty_before": difficulty_before,
            "difficulty_after": difficulty_after,
            "delta": delta,
            "answer_type": task["answer_type"],
            "question": task["question"],
            "answer": task["answer"],
            "user_answer": user_answer,
            "is_correct": int(norm_user is not None) and (norm_user == norm_ans),
            "time_taken": time_taken,
            "expected_time": expected_time,
            "p_correct": p_correct,
        })
