import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# Load results
# -----------------------------
df = pd.read_csv("data/detection_results.csv")

print("Available columns:", df.columns.tolist())

# -----------------------------
# Sampling for visualization
# -----------------------------
SAMPLE_SIZE = 5000
sample = df.sample(min(len(df), SAMPLE_SIZE), random_state=42).sort_values("time")

# -----------------------------
# Setup figure (2x2 grid)
# -----------------------------
fig, axs = plt.subplots(2, 2, figsize=(16, 10))
fig.suptitle("Fault Detection Analysis on Google Borg Traces", fontsize=16)

# =====================================================
# (1) CPU Usage with Fault Detections
# =====================================================
axs[0, 0].plot(sample["time"], sample["cpu_usage"], color="steelblue", label="CPU Usage")

if "detected_fault" in sample.columns:
    axs[0, 0].scatter(
        sample[sample["detected_fault"] == 1]["time"],
        sample[sample["detected_fault"] == 1]["cpu_usage"],
        color="red",
        s=15,
        label="Z-Score Fault",
        alpha=0.7,
    )

if "adaptive_fault" in sample.columns:
    axs[0, 0].scatter(
        sample[sample["adaptive_fault"] == 1]["time"],
        sample[sample["adaptive_fault"] == 1]["cpu_usage"],
        color="purple",
        s=15,
        label="Adaptive Z-Score",
        alpha=0.7,
    )

axs[0, 0].set_title("CPU Usage with Fault Detections")
axs[0, 0].set_xlabel("Time")
axs[0, 0].set_ylabel("CPU Usage")
axs[0, 0].legend()
axs[0, 0].grid(True)

# =====================================================
# (2) Memory Usage with Fault Detections
# =====================================================
axs[0, 1].plot(sample["time"], sample["memory_usage"], color="green", label="Memory Usage")

if "detected_fault" in sample.columns:
    axs[0, 1].scatter(
        sample[sample["detected_fault"] == 1]["time"],
        sample[sample["detected_fault"] == 1]["memory_usage"],
        color="red",
        s=15,
        label="Z-Score Fault",
        alpha=0.7,
    )

axs[0, 1].set_title("Memory Usage with Fault Detections")
axs[0, 1].set_xlabel("Time")
axs[0, 1].set_ylabel("Memory Usage")
axs[0, 1].legend()
axs[0, 1].grid(True)

# =====================================================
# (3) Metrics Summary Panel
# =====================================================
axs[1, 0].axis("off")

metrics_text = (
    "Z-Score Detection\n"
    "Precision: 0.2549\n"
    "Recall: 0.00014\n"
    "F1 Score: 0.00028\n\n"
    "EWMA Baseline\n"
    "Precision: 0.0658\n"
    "Recall: 0.00035\n"
    "F1 Score: 0.00069\n\n"
    "Lead-Time Statistics\n"
    "Avg: 4.99e11\n"
    "Max: 1.05e12\n"
    "Min: 3.41e10"
)

axs[1, 0].text(
    0.05,
    0.95,
    metrics_text,
    fontsize=11,
    verticalalignment="top",
    bbox=dict(boxstyle="round", facecolor="whitesmoke", edgecolor="gray"),
)
axs[1, 0].set_title("Detection Performance Summary")

# =====================================================
# (4) Total Fault Detections by Method
# =====================================================
methods = []
counts = []

if "detected_fault" in df.columns:
    methods.append("Z-Score")
    counts.append(df["detected_fault"].sum())

if "ewma_fault" in df.columns:
    methods.append("EWMA")
    counts.append(df["ewma_fault"].sum())

if "adaptive_fault" in df.columns:
    methods.append("Adaptive Z")
    counts.append(df["adaptive_fault"].sum())

if counts:
    axs[1, 1].bar(methods, counts, color=["red", "orange", "purple"][:len(counts)])
    axs[1, 1].set_title("Total Fault Detections by Method")
    axs[1, 1].set_ylabel("Number of Detections")
    axs[1, 1].grid(axis="y")
else:
    axs[1, 1].text(0.5, 0.5, "No detection results available",
                   ha="center", va="center", fontsize=11)
    axs[1, 1].set_axis_off()

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()
