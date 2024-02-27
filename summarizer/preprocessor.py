import re


def clean_text(text):
    # Implement cleaning operations, e.g., removing extra spaces, newlines
    text = re.sub(r'\s+', ' ', text)
    print(text)
    return text
