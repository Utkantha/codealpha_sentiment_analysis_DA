import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

class TextAnalyzer:
    def __init__(self):
        self.vader_analyzer = SentimentIntensityAnalyzer()
        
        # A basic emotion lexicon for demonstration
        self.emotion_lexicon = {
            'happy': 'joy', 'amazing': 'joy', 'love': 'joy', 'best': 'joy', 'excited': 'joy', 'great': 'joy',
            'terrible': 'anger', 'hate': 'anger', 'waste': 'anger', 'disappointed': 'anger', 'angry': 'anger',
            'broke': 'sadness', 'sad': 'sadness', 'homeless': 'sadness',
            'anxious': 'fear', 'fear': 'fear', 'scared': 'fear', 'devastating': 'fear',
            'protests': 'anger', 'diseases': 'fear', 'crisis': 'fear'
        }
        
    def get_sentiment(self, text):
        """Classifies text as positive, negative, or neutral using VADER."""
        scores = self.vader_analyzer.polarity_scores(text)
        compound = scores['compound']
        
        if compound >= 0.05:
            return 'Positive'
        elif compound <= -0.05:
            return 'Negative'
        else:
            return 'Neutral'
            
    def get_emotions(self, text):
        """Detects specific emotions using a custom lexicon."""
        words = text.lower().split()
        emotions = {}
        for word in words:
            # Strip basic punctuation
            clean_word = ''.join(e for e in word if e.isalnum())
            if clean_word in self.emotion_lexicon:
                emotion = self.emotion_lexicon[clean_word]
                emotions[emotion] = emotions.get(emotion, 0) + 1
        return emotions

    def analyze_dataframe(self, df, text_column='text'):
        """Applies sentiment and emotion analysis to a DataFrame."""
        df['Sentiment'] = df[text_column].apply(self.get_sentiment)
        df['Emotions'] = df[text_column].apply(self.get_emotions)
        return df
