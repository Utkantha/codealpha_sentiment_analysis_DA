# Sentiment & Emotion Detector 🚀

Welcome to the Sentiment and Emotion Detector! This Python-based pipeline analyzes text datasets to understand underlying human emotions and general sentiment (positive/negative/neutral). 

## What This Project Does
This script processes text from various mock sources like E-commerce platforms, Social Networks, and News Outlets. 
- **Sentiment Scoring:** Uses `vaderSentiment` to rank text polarity.
- **Emotion Tagging:** Uses a custom keyword lexicon to find deep emotions (like anger, fear, joy).
- **Data Visualization:** Automatically generates bar charts and distribution graphs using `matplotlib` and `seaborn`.
- **Business Intelligence:** Outputs an automated Markdown report (`insights_report.md`) containing actionable business recommendations based on the datasets.

## How to Run It
1. Make sure you have installed the required libraries from `requirements.txt` (`pip install -r requirements.txt`).
2. Execute the pipeline by running: `python main.py`.

## Outputs
Once the script finishes running, check the newly generated `analysis_results` folder. It will contain all your processed `.csv` data tagged with sentiments, visual `.png` graphs, and your final business insights report!
