from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

training_text = [
    "excellent support thank you",
    "problem solved quickly",
    "very happy with service",
    "bad support",
    "issue not solved",
    "very disappointed",
    "okay service",
    "average response"
]

labels = [
    "Positive",
    "Positive",
    "Positive",
    "Negative",
    "Negative",
    "Negative",
    "Neutral",
    "Neutral"
]

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(training_text)

model = MultinomialNB()
model.fit(X, labels)

def predict_sentiment(text):
    text_vector = vectorizer.transform([text])
    prediction = model.predict(text_vector)
    return prediction[0]