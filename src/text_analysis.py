from textblob import TextBlob

def analyze_text(text):
    polarity = TextBlob(text).sentiment.polarity
    confidence = round((polarity + 1) * 5, 1)
    clarity = min(len(text.split()) / 15, 10)
    return confidence, clarity
