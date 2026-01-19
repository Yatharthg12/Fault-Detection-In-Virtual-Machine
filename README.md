# Fault Detection Analysis on Google Borg Traces

This project presents a statistical fault detection and analysis framework applied to the **Google Borg Cluster Traces**, a large-scale real-world dataset representing resource usage and events in Google’s production data centers.  
The goal is to explore how lightweight, interpretable statistical methods perform for early fault detection in cloud environments, with a focus on **CPU and memory anomalies**, **lead-time behavior**, and **method comparison**.

---

## Project Overview

Cloud data centers generate massive telemetry streams, making early fault detection both critical and challenging. Instead of using black-box machine learning models, this project focuses on:

- **Explainable statistical fault detection**
- **Low-overhead, real-time friendly techniques**
- **Comparative evaluation of multiple detection strategies**
- **Research-grade visualizations and metrics**

The system processes raw Borg traces, applies fault detection logic, evaluates detection quality, and produces publication-ready visual results.

---

## Fault Detection Methods Implemented

### 1. Z-Score Based Detection
- Sliding window per machine
- Flags anomalies when CPU or memory deviates beyond a fixed standard deviation threshold
- Simple, fast, and interpretable
- Serves as the primary baseline

### 2. EWMA (Exponentially Weighted Moving Average)
- Smooths CPU usage over time
- Detects sudden deviations from expected trends
- Acts as a secondary baseline for comparison

### 3. Adaptive Z-Score (Controlled Improvement)
- Uses rolling mean and rolling standard deviation
- Threshold adapts dynamically to workload variability
- Improves recall under non-stationary behavior
- Explicitly presented as a **controlled improvement**, not a production-ready solution

---

## Evaluation Metrics

The project evaluates detection performance using:

- **Precision**
- **Recall**
- **F1-score**
- **Fault count comparison across methods**
- **Lead-time statistics** (average, min, max time between detection and failure)

Example observed results:

- Z-Score:
  - Precision ≈ 0.25
  - Recall ≈ 0.00014
- EWMA:
  - Precision ≈ 0.066
  - Recall ≈ 0.00035

These results highlight the classic trade-off between false positives and early detection in large-scale systems.

---

##  Visualizations

The project generates a single consolidated visualization window containing:

- CPU usage with fault markers
- Memory usage with fault markers
- Method-wise fault detection counts
- Lead-time statistics or textual summaries (when distributions are sparse)

All plots are designed to be **publication-friendly**, cleanly labeled, and suitable for inclusion in academic papers or technical reports.

---

## Dataset

**Google Borg Cluster Traces**

- Source: Google Cluster Data (Borg Traces)
- Publicly available research dataset
- Captures task events, machine resource usage, and failures at scale

📎 Dataset reference:  
https://github.com/google/cluster-data

> Note: This project uses a cleaned and sampled subset of the original traces for computational feasibility.

---

## How the System Works (High Level)

1. Raw Borg trace CSV is cleaned and normalized
2. Fault detection logic is applied per machine
3. Detection results are stored as annotated CSV files
4. Evaluation scripts compute performance metrics
5. Visualization script generates combined analytical plots

Each step is modular and reproducible.

---

## Research Scope & Limitations

### What This Project Does Well
- Demonstrates explainable fault detection at scale
- Uses real-world cloud telemetry data
- Provides comparative, metric-based evaluation
- Produces research-quality visual outputs

### What This Project Does NOT Do
- Does not claim production deployment readiness
- Does not use supervised or deep learning models
- Does not model causal failure propagation
- Does not optimize thresholds automatically per workload

These limitations are intentional to preserve interpretability and academic clarity.

---

## Possible Extensions

If extended further, this project could include:

- Per-metric adaptive thresholds (CPU vs memory)
- Machine-specific baseline learning
- Change-point detection methods
- Survival analysis for failure prediction
- Graph-based dependency modeling
- Comparison with lightweight ML baselines

---

## Requirements

Core dependencies used in this project:

- Python 3.10+
- pandas
- numpy
- matplotlib
- scikit-learn

(Exact versions can be checked in requirements.txt)

---

## Usage

This project is intended for:
- Academic research
- Cloud systems coursework
- Fault detection experimentation
- Reproducible systems analysis

If you use this work in academic writing, please cite the Google Borg dataset appropriately.

---

## Authors

Yatharth Garg & Yogesh Mehta
