import re
import string

def clean_text(text):
    text = text.lower()
    text = re.sub(r'https?:\/\/\S+', '', text)  # remove URLs
    text = re.sub(r'[^a-z0-9\s]', ' ', text)   # remove punctuation
    text = re.sub(r'\s+', ' ', text).strip()   # remove extra spaces
    return text
