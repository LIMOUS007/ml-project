import pandas as pd 
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
df = pd.read_csv("data_log.csv")

df["is_correct"] = df["is_correct"].str.lower() == 'true'
plt.scatter(df["expected_time"], df["time_taken"], alpha=0.3)
plt.plot([0, max(df["expected_time"])],
         [0, max(df["expected_time"])], color="red")
plt.xlabel("Expected Time")
plt.ylabel("Actual Time")
plt.title("Expected vs Actual Time")
plt.show()
bins = pd.cut(df["p_correct"], bins=10)
grouped = df.groupby(bins)["is_correct"].mean()

grouped.plot(kind="bar")
plt.ylabel("Actual correctness")
plt.title("Calibration: p_correct vs actual")
plt.show()
for sid, g in df.groupby("session_id"):
    plt.plot(g["task_index"], g["difficulty_before"], alpha=0.5)

plt.xlabel("Task index")
plt.ylabel("Difficulty")
plt.title("Difficulty progression per session")
plt.show()
