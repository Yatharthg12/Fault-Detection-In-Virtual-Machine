import pandas as pd

df = pd.read_csv("data/detection_results.csv")

lead_times = []

for mid, group in df.groupby("machine_id"):
    failures = group[group["failed"] == 1]

    for _, fail_row in failures.iterrows():
        fail_time = fail_row["time"]

        detected = group[
            (group["detected_fault"] == 1) &
            (group["time"] < fail_time)
        ]

        if not detected.empty:
            first_detect_time = detected.iloc[-1]["time"]
            lead_time = fail_time - first_detect_time
            lead_times.append(lead_time)

if lead_times:
    print("Average Lead Time:", sum(lead_times) / len(lead_times))
    print("Max Lead Time:", max(lead_times))
    print("Min Lead Time:", min(lead_times))
else:
    print("No early detections found.")

