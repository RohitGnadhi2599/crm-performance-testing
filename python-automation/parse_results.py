import pandas as pd

df = pd.read_csv("results/login_results.csv")

print("==== LOGIN API PERFORMANCE ====")
print("Avg Response Time:", df["elapsed"].mean())
print("Max Response Time:", df["elapsed"].max())
print("Throughput:", df["Bytes"].sum() / df["elapsed"].sum())
print("Error Rate:", (df["success"] == False).mean() * 100, "%")
