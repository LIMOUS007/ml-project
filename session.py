import time
import uuid
from engine.task_picker import pick_task
from engine.difficulty import update_difficulty
from engine.logger import log_attempt
def normalize(ans, answer_type):
    if answer_type == "boolean":
        return str(ans).strip().lower()
    elif answer_type == "yesno":
        mapping = {"yes": "yes", "y": "yes", "true": "yes",
               "no": "no", "n": "no", "false": "no"}
        return mapping.get(str(ans).lower(), str(ans).lower())
    else:  
        return str(ans).strip()

def run_session(user_id, rounds):
    session_id = str(uuid.uuid4())
    user_state = {
        "difficulty": 0
    }
    for task_index in range(1, rounds+1):
        difficulty_before = user_state["difficulty"]
        task = pick_task({"difficulty": difficulty_before})
        print("\n", task["question"])
        start = time.time()
        print("Answer type is", task["answer_type"])
        user_answer = input("Your answer: ").strip()
        end = time.time()
        time_taken = end - start
        correct = normalize(user_answer, task["answer_type"]) == normalize(task["answer"], task["answer_type"])
        difficulty_after = update_difficulty(difficulty_before, correct)
        user_state["difficulty"] = difficulty_after
        log_attempt(
            user_id=user_id,
            session_id = session_id,
            task_index = task_index,
            task=task,
            user_answer=user_answer,
            time_taken=time_taken,
            difficulty_before = difficulty_before,
            difficulty_after = difficulty_after
        )
        print("Correct:", correct)
        print("New difficulty:", user_state["difficulty"])
        
if __name__ == "__main__":
    run_session(user_id="test_user", rounds=10)
