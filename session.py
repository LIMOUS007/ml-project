import time
from engine.task_picker import pick_task
from engine.difficulty import update_difficulty
from engine.logger import log_attempt
def normalize(ans, answer_type):
    if answer_type in ("boolean", "yesno"):
        return str(ans).strip().lower()
    return str(ans).strip()

def run_session(user_id, rounds=20):
    user_state = {
        "difficulty": 0
    }
    for _ in range(rounds):
        task = pick_task(user_state)
        print("\n", task["question"])
        start = time.time()
        print("Answer type is", task["answer_type"])
        user_answer = input("Your answer: ").strip()
        end = time.time()
        time_taken = end - start
        correct = normalize(user_answer, task["answer_type"]) == normalize(task["answer"], task["answer_type"])
        user_state["difficulty"] = update_difficulty(
            user_state["difficulty"],
            correct
        )
        log_attempt(
            user_id=user_id,
            task=task,
            user_answer=user_answer,
            time_taken=time_taken
        )
        print("Correct:", correct)
        print("New difficulty:", user_state["difficulty"])
        
if __name__ == "__main__":
    run_session(user_id="test_user", rounds=20)
