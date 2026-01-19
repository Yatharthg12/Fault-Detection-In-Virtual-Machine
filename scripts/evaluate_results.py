import pandas as pd
from sklearn.metrics import precision_score, recall_score, f1_score

df = pd.read_csv("data/detection_results.csv")

y_true = df["failed"]
y_pred = df["detected_fault"]

print("Precision:", precision_score(y_true, y_pred))
print("Recall:", recall_score(y_true, y_pred))
print("F1 Score:", f1_score(y_true, y_pred))

# Evaluate EWMA baseline
print("\nEWMA BASELINE RESULTS")
print("Precision:", precision_score(df["failed"], df["ewma_fault"]))
print("Recall:", recall_score(df["failed"], df["ewma_fault"]))
print("F1 Score:", f1_score(df["failed"], df["ewma_fault"]))
