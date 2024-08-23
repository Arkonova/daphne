
import re

def clean_text(text):
    text = text.strip()
    text = re.sub(r'\s+', ' ', text)
    return text.lower()

def normalize_text_column(dataset, column_name):
    return dataset.map(lambda x: {column_name: clean_text(x[column_name])})
