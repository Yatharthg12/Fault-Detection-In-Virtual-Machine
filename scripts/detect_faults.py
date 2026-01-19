import pandas as pd
import numpy as np

WINDOW = 6
THRESHOLD = 2.0

df = pd.read_csv("data/clean_borg_traces.csv")

df["detected_fault"] = 0

for mid, group in df.groupby("machine_id"):
    cpu = group["cpu_usage"].values
    mem = group["memory_usage"].values
    idx = group.index

    for i in range(WINDOW, len(group)):
        cpu_w = cpu[i-WINDOW:i]
        mem_w = mem[i-WINDOW:i]

        if np.std(cpu_w) > 0:
            z_cpu = (cpu[i] - cpu_w.mean()) / cpu_w.std()
        else:
            z_cpu = 0

        if np.std(mem_w) > 0:
            z_mem = (mem[i] - mem_w.mean()) / mem_w.std()
        else:
            z_mem = 0

        if abs(z_cpu) > THRESHOLD or abs(z_mem) > THRESHOLD:
            df.loc[idx[i], "detected_fault"] = 1

df.to_csv("data/detection_results.csv", index=False)
print("Detection completed.")

#Adding EWMA baseline for comparison
ALPHA = 0.3
EWMA_THRESHOLD = 0.15

df["ewma_cpu"] = 0.0
df["ewma_fault"] = 0

for mid, group in df.groupby("machine_id"):
    cpu = group["cpu_usage"].values
    idx = group.index

    ewma = cpu[0]

    for i in range(1, len(cpu)):
        ewma = ALPHA * cpu[i] + (1 - ALPHA) * ewma
        df.loc[idx[i], "ewma_cpu"] = ewma

        if abs(cpu[i] - ewma) > EWMA_THRESHOLD:
            df.loc[idx[i], "ewma_fault"] = 1

df.to_csv("data/detection_results.csv", index=False)
print("EWMA baseline added.")

# Adaptive Z-Score Fault Detection
window = 50        # adaptivity window
k = 2.5            # sensitivity threshold

rolling_mean = df["cpu_usage"].rolling(window=window).mean()
rolling_std = df["cpu_usage"].rolling(window=window).std()

adaptive_z = (df["cpu_usage"] - rolling_mean) / rolling_std

df["adaptive_fault"] = (adaptive_z.abs() > k).astype(int)
df.to_csv("data/detection_results.csv", index=False)
print("Adaptive Z-score added.")
