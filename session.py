import time
import uuid
from engine.task_picker import pick_task
from engine.difficulty import update_difficulty_ml
from engine.logger import log_attempt
from engine.session_summary import log_session_summary
from engine.ml_models import load_models, predict 
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

def run_session(user_id, duration_seconds):
    session_id = str(uuid.uuid4())
    correct_model, time_model, feature_cols = load_models()
    user_state = {
        "difficulty": 0
    }
    session_start = time.time()
    task_index = 0
    total_correct = 0
    while True:
        now = time.time()
        if now - session_start >= duration_seconds:
            break
        difficulty_before = user_state["difficulty"]
        task = pick_task({"difficulty": difficulty_before})
        task_subfamily = task["task_id"].split("-")[1]
        p_correct, expected_time = predict(
            correct_model, time_model, feature_cols,
            difficulty_before = difficulty_before,
            skill = task["skill"],
            task_subfamily= task_subfamily,
            answer_type = task["answer_type"]
        )
        print(f"ML p_correct={p_correct:.3f} | expected_time={expected_time:.2f}s")
        print("\n", task["question"])
        start = time.time()
        print("Answer type is", task["answer_type"])
        user_answer = input("Your answer: ").strip()
        if user_answer.strip() == "":
            user_answer = "__EMPTY__"
        end = time.time()
        time_taken = end - start
        norm_user = normalize(user_answer, task["answer_type"])
        norm_ans = normalize(task["answer"], task["answer_type"])
        correct = (norm_user is not None) and (norm_user == norm_ans)
        if correct:
            total_correct += 1
        difficulty_after, delta = update_difficulty_ml(
            difficulty_before=difficulty_before,
            correct=correct,
            time_taken=time_taken,
            expected_time=expected_time,
            p_correct=p_correct
        )
        user_state["difficulty"] = difficulty_after
        log_attempt(
            user_id=user_id,
            session_id = session_id,
            task_index = task_index,
            task=task,
            user_answer=user_answer,
            time_taken=time_taken,
            difficulty_before = difficulty_before,
            difficulty_after = difficulty_after,
            delta = delta,
            p_correct = p_correct,
            expected_time = expected_time
        )
        task_index += 1
        print("Correct:", correct)
        print("New difficulty:", user_state["difficulty"])
        print("Delta: ", delta)
    log_session_summary(
            user_id = user_id,
            session_id = session_id,
            total_attempts = task_index,
            total_correct = total_correct,
            start_time_iso = time.strftime("%Y-%m-%dT%H:%M:%S", time.localtime(session_start)),
            end_time_iso = time.strftime("%Y-%m-%dT%H:%M:%S", time.localtime(time.time()))
        )
        
if __name__ == "__main__":
    run_session(user_id="LIMOUS", duration_seconds = 300)
