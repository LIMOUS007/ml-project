import math
def update_difficulty_ml(difficulty_before, correct, time_taken, expected_time, p_correct):
    expected_time = max(0.5, float(expected_time))
    time_taken = max(0.01, float(time_taken))
    log_taken = math.log1p(time_taken)
    log_expected = math.log1p(expected_time)
    time_ratio = log_taken / log_expected
    if correct:
        if time_ratio <= 0.85:
            delta = 3
        elif time_ratio <= 1.15:
            delta = 2
        else:
            delta = 1
    else:
        if time_ratio >= 1.3:
            delta = -2
        else:
            delta = -1
    if correct and p_correct < 0.4:
        delta += 1
    if (not correct) and p_correct > 0.7:
        delta -= 1
    difficulty_after = difficulty_before + delta
    difficulty_after = max(0, difficulty_after)
    return difficulty_after, delta