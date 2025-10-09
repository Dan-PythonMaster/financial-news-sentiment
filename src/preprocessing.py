import re
from nltk.corpus import stopwords
import nltk

# Download stopwords if not already done
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

def clean_text(text):
    # Lowercase
    text = text.lower()
    
    # Remove URLs
    text = re.sub(r'https?:\/\/\S+', '', text)
    
    # Remove punctuation
    text = re.sub(r'[^a-z0-9\s]', ' ', text)
    
    # Remove extra spaces
    text = re.sub(r'\s+', ' ', text).strip()
    
    # Remove stop words
    text = ' '.join(word for word in text.split() if word not in stop_words)
    
    return text
