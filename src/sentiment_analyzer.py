import pandas as pd
from textblob import TextBlob

def get_sentiment(polarity):
    if polarity > 0.2:
        return "Positive"
    elif polarity < -0.2:
        return "Negative"
    else:
        return "Neutral"

def analyze_reviews(file_path):
    df = pd.read_csv(file_path)
    df['Polarity'] = df['Review'].apply(lambda x: TextBlob(str(x)).sentiment.polarity)
    df['Sentiment'] = df['Polarity'].apply(get_sentiment)

    print("\nSentiment Summary:")
    print(df['Sentiment'].value_counts())
    
    # Save the result
    df.to_csv("reports/analyzed_reviews2.csv", index=False)
    return df

if __name__ == "__main__":
    analyze_reviews("data/reviews2.csv")

