import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

class InsightsVisualizer:
    def __init__(self, output_dir='analysis_results'):
        self.output_dir = output_dir
        import os
        os.makedirs(self.output_dir, exist_ok=True)
        
    def plot_sentiment_distribution(self, df, source_name):
        plt.figure(figsize=(8, 5))
        sns.countplot(data=df, x='Sentiment', palette='viridis', order=['Positive', 'Neutral', 'Negative'])
        plt.title(f'Sentiment Distribution - {source_name}')
        plt.xlabel('Sentiment')
        plt.ylabel('Count')
        plt.savefig(f'{self.output_dir}/{source_name}_sentiment.png')
        plt.close()
        
    def plot_emotion_frequencies(self, df, source_name):
        # Aggregate all emotions
        emotion_counts = {}
        for emotions in df['Emotions']:
            for emotion, count in emotions.items():
                if emotion not in ['positive', 'negative']: # Filter out general sentiments
                    emotion_counts[emotion] = emotion_counts.get(emotion, 0) + count
                    
        if not emotion_counts:
            return
            
        emotions_df = pd.DataFrame(list(emotion_counts.items()), columns=['Emotion', 'Count'])
        emotions_df = emotions_df.sort_values(by='Count', ascending=False)
        
        plt.figure(figsize=(10, 6))
        sns.barplot(data=emotions_df, x='Count', y='Emotion', palette='magma')
        plt.title(f'Emotion Frequencies - {source_name}')
        plt.xlabel('Frequency')
        plt.ylabel('Emotion')
        plt.savefig(f'{self.output_dir}/{source_name}_emotions.png')
        plt.close()
