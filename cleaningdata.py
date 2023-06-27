import re
import string
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import pandas as pd
nltk.download('punkt')

#Load your data into a pandas DataFrame:
#data = pd.read_csv("C:\Users\fujitsu\Documents\STMIK Jayakarta\sem 3\bigdata\tugasopenapi\rawdata.csv")  
data = pd.read_csv('rawdata.csv')

# Download the necessary resources for tokenization
#nltk.download('punkt')
    
#Remove any special characters, URLs, or non-alphanumeric characters using regular 
def remove_special_characters(text):
    pattern = r'[^a-zA-Z0-9\s]'
    text = re.sub(pattern, '', text)
    return text

def remove_urls(text):
    pattern = r'http\S+|www\S+'
    text = re.sub(pattern, '', text)
    return text

#Convert the text to lowercase
def convert_to_lowercase(text):
    text = text.lower()
    return text

#Tokenize the text into individual words:
def tokenize_text(text):
    tokens = word_tokenize(text)
    return tokens

#Remove stop words (commonly occurring words that do not carry much information) using NLTK
nltk.download('stopwords')

def remove_stopwords(tokens):
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [token for token in tokens if token not in stop_words]
    return filtered_tokens

#Perform stemming or lemmatization to reduce words to their base or root form:
nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer

def lemmatize_tokens(tokens):
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens]
    return lemmatized_tokens

from nltk.stem import PorterStemmer

def stem_tokens(tokens):
    stemmer = PorterStemmer()
    stemmed_tokens = [stemmer.stem(token) for token in tokens]
    return stemmed_tokens

#Rejoin the cleaned tokens into a single text string:

def rejoin_tokens(tokens):
    text = ' '.join(tokens)
    return text

#Create a function to apply the text cleaning steps to a specific column in the DataFrame:
def clean_text(text):
    if isinstance(text, float):
        return str(text)
    text = remove_special_characters(text)
    text = remove_urls(text)
    text = convert_to_lowercase(text)
    tokens = tokenize_text(text)
    tokens = remove_stopwords(tokens)
    tokens = lemmatize_tokens(tokens)
    cleaned_text = rejoin_tokens(tokens)
    return cleaned_text



#Apply the cleaning function to the desired column in the DataFrame using the apply
data['tokens'] = data['text'].apply(clean_text)

#data['text'].fillna('', inplace=True)
#data['Word Count'] = data['text'].apply(lambda x: len(str(x).split()))
del data['text']

# Membuat DataFrame baru untuk menampung hasil
new_df = pd.DataFrame(columns=['Word'])

# Menambahkan baris baru sesuai jumlah kata pada kalimat baris sebelumnya
for index, row in data.iterrows():
    sentence = row['tokens']
    words = sentence.split()
    for word in words:
        new_df = new_df.append({'Word': word}, ignore_index=True)
        new_df['Word'].fillna('', inplace=True)

#export to csv
new_df.to_csv(r'clean.csv', index=False)