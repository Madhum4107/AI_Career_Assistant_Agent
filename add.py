import re

def process_resume(text):
    words = len(text.split())
    return {
        "word_count": words,
        "score": max(1, words // 6)
    }

def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-z\s]", "", text)
    return text

def extract_words(text):
    return text.split()