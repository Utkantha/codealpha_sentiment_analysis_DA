# Multi-Source Sentiment & Emotion Analysis

This project implements a complete sentiment analysis pipeline as requested:
1. **Classifies text** as positive, negative, or neutral using `vaderSentiment`.
2. **Detects specific emotions** (joy, anger, fear, etc.) using `NRCLex` (Lexicon-based NLP).
3. **Applies analysis** across diverse data sources: Amazon reviews, Social Media, and News.
4. **Understands public opinion and trends** by aggregating sentiments and emotions and generating visual charts.
5. **Informs business strategy** (Marketing, Product, PR) via an automatically generated insights report.

## Project Structure
- `data/`: Contains mock CSV data from Amazon, Social Media, and News.
- `src/analyzer.py`: Contains the `TextAnalyzer` class for sentiment and emotion extraction using NLP.
- `src/visualizer.py`: Contains the `InsightsVisualizer` class for plotting data using `seaborn` and `matplotlib`.
- `main.py`: The entry point that loads data, analyzes it, generates plots, and writes a report.
- `output/`: (Created upon running) Will contain graphs, processed CSVs, and the markdown insights report.

## Setup and Installation

1. Create a virtual environment (optional but recommended).
2. Install required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the main script:
   ```bash
   python main.py
   ```
*(Note: Running this for the first time will automatically download the necessary NLTK corpora.)*

## Results
Check the `output` directory after running for visual charts (PNG), processed data, and the `insights_report.md` for actionable business applications.
