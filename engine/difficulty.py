def update_difficulty(current, is_correct):
    if is_correct:
        return min(current + 2, 100)
    else:
        return max(current - 1, 0)
