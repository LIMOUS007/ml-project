import pickle
import pandas as pd
import numpy as np
def load_models():
    with open("correct_model.pkl", "rb") as f:
        correct_model = pickle.load(f)
    with open("time_model.pkl", "rb") as f:
        time_model = pickle.load(f)
    with open("feature_cols.pkl", "rb") as f:
        feature_cols = pickle.load(f)
    return correct_model, time_model, feature_cols

def build_feature_row(difficulty_before, skill, task_subfamily, answer_type, feature_cols):
    row = {
        "difficulty_before": difficulty_before,
        f"skill_{skill}" : 1,
        f"answer_type_{answer_type}" : 1,
        f"task_subfamily_{task_subfamily}" : 1
    }
    x = pd.DataFrame([row])
    for col in feature_cols:
        if col not in x.columns:
            x[col] = 0
    x = x[feature_cols]
    return x

def predict(correct_model, time_model, feature_cols, difficulty_before, skill, task_subfamily, answer_type):
    x = build_feature_row(difficulty_before, skill, task_subfamily, answer_type, feature_cols)
    p_correct = correct_model.predict_proba(x)[0, 1]
    expected_time = float(np.expm1(time_model.predict(x)[0]))
    return p_correct, expected_time