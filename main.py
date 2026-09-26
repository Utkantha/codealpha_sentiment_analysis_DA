import pandas as pd
import os
from src.analyzer import TextAnalyzer
from src.visualizer import InsightsVisualizer

def load_data():
    amazon_df = pd.read_csv('data/sample_amazon_reviews.csv')
    social_df = pd.read_csv('data/sample_social_media.csv')
    news_df = pd.read_csv('data/sample_news.csv')
    
    return {
        'Amazon_Reviews': amazon_df,
        'Social_Media': social_df,
        'News_Articles': news_df
    }

def generate_insights_report(results_dict):
    report = ["# Sentiment Analysis Insights Report\n"]
    
    for source, df in results_dict.items():
        report.append(f"## Analysis for {source.replace('_', ' ')}")
        sentiment_counts = df['Sentiment'].value_counts().to_dict()
        report.append(f"- **Total Items:** {len(df)}")
        report.append(f"- **Sentiment Breakdown:** {sentiment_counts}")
        
        # Determine trend
        if sentiment_counts.get('Positive', 0) > sentiment_counts.get('Negative', 0):
            trend = "Generally Positive"
        elif sentiment_counts.get('Negative', 0) > sentiment_counts.get('Positive', 0):
            trend = "Generally Negative"
        else:
            trend = "Mixed / Neutral"
            
        report.append(f"- **Overall Trend:** {trend}\n")
        
    report.append("## Business Applications")
    report.append("- **Marketing:** Use the generally positive sentiment from Social Media to identify brand advocates and successful campaigns.")
    report.append("- **Product Development:** Address the negative Amazon reviews by analyzing the specific complaints (e.g., product durability issues).")
    report.append("- **Public Relations:** Monitor News sentiment to manage brand reputation and respond swiftly to emerging negative sentiment.")
    
    with open('output/insights_report.md', 'w', encoding='utf-8') as f:
        f.write('\n'.join(report))
        
    print("Insights report generated at output/insights_report.md")


def main():
    print("Initializing Analyzer (Downloading NLP resources if needed)...")
    analyzer = TextAnalyzer()
    visualizer = InsightsVisualizer(output_dir='output')
    
    datasets = load_data()
    analyzed_datasets = {}
    
    for source_name, df in datasets.items():
        print(f"Analyzing {source_name}...")
        analyzed_df = analyzer.analyze_dataframe(df)
        analyzed_datasets[source_name] = analyzed_df
        
        print(f"Generating visualizations for {source_name}...")
        visualizer.plot_sentiment_distribution(analyzed_df, source_name)
        visualizer.plot_emotion_frequencies(analyzed_df, source_name)
        
        # Save analyzed data
        analyzed_df.to_csv(f'output/analyzed_{source_name}.csv', index=False)
        
    print("Generating final insights report...")
    generate_insights_report(analyzed_datasets)
    print("Analysis complete! Check the 'output' folder for results, visualizations, and insights.")

if __name__ == "__main__":
    main()
