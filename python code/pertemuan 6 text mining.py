    # import libraries
import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# download nltk corpus (first time only
import nltk
nltk.download( 'all')

# Load the amazon review dataset
df = pd.read_csv('https://raw.githubusercontent.com/pycaret/pycaret/master/datasets/amazon.csv')

def preprocess_text(text):
  #Tokenize the text
  token = word_tokenize(text.lower())

  #Remove stop word
  filtered_tokens = [token for token in token if token not in stopword.words('english')]

  #Lemmatize the tokens
  lemmatizer = WordNetLemmatizer()
  lemmatized_tokens = [lemmatizer.lemmatize(token) for token in filtered_token]

  #join the token back into a string
  processed_text = ' '.join(lemmatized_tokens)
  return processed_text

analyzer = SentimentIntensityAnalyzer()

#Create get_sentiment function
def get_sentiment(text):
    scores = analyzer.polarity_scores(text)
    sentiment = 1 if scores['pos'] > 0 else 0
    return sentiment

#Apply get_sentiment function
df['sentiment'] = df['reviewText'].apply(get_sentiment)
from sklearn.metrics import confusion_matrix
print(confusion_matrix(df['Positive'], df['sentiment']))
  
from sklearn.metrics import classification_report
print(classification_report(df['Positive'], df['sentiment']))