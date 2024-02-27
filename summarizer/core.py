import requests
from bs4 import BeautifulSoup
from collections import Counter
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from nltk.tokenize import RegexpTokenizer
from nltk.cluster.util import cosine_distance
import numpy as np
import networkx as nx

nltk.download('punkt')
nltk.download('stopwords')


def fetch_webpage_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print("Error fetching webpage content:", e)
        return None


def preprocess_text(text):
    sentences = sent_tokenize(text)

    filtered_sentences = [sentence for sentence in sentences if
                          len(sentence) > 10 and any(c.isalnum() for c in sentence)]

    # Tokenize words and remove stopwords
    stop_words = set(stopwords.words("english"))
    preprocessed_words = []
    for sentence in filtered_sentences:
        words = word_tokenize(sentence.lower())
        words = [word for word in words if word not in stop_words]
        preprocessed_words.extend(words)

    return preprocessed_words


def sentence_similarity(sent1, sent2):
    vector1 = Counter(sent1)
    vector2 = Counter(sent2)
    intersection = set(vector1.keys()) & set(vector2.keys())
    numerator = sum([vector1[x] * vector2[x] for x in intersection])
    denominator = np.sqrt(sum([vector1[x] ** 2 for x in vector1])) * np.sqrt(sum([vector2[x] ** 2 for x in vector2]))
    if not denominator:
        return 0.0
    else:
        return float(numerator) / denominator


def build_similarity_matrix(sentences):
    similarity_matrix = np.zeros((len(sentences), len(sentences)))
    for i in range(len(sentences)):
        for j in range(len(sentences)):
            if i != j:
                similarity_matrix[i][j] = sentence_similarity(sentences[i], sentences[j])
    return similarity_matrix


def generate_summary(text, num_sentences=5):
    sentences = sent_tokenize(text)
    preprocessed_sentences = [preprocess_text(sentence) for sentence in sentences]
    similarity_matrix = build_similarity_matrix(preprocessed_sentences)
    nx_graph = nx.from_numpy_array(similarity_matrix)
    scores = nx.pagerank(nx_graph)
    ranked_sentences = sorted(((scores[i], sentence) for i, sentence in enumerate(sentences)), reverse=True)

    selected_sentences = []
    selected_sentences_text = set()

    for _, sentence in ranked_sentences:
        if len(selected_sentences) >= num_sentences:
            break
        if not any(sentence_similarity(sentence, selected_sent) > 0.8 for selected_sent in selected_sentences):
            selected_sentences.append(sentence)
            selected_sentences_text.add(sentence)

    return ' '.join(selected_sentences[:num_sentences])


def summarize_webpage(url, num_sentences=3):
    webpage_content = fetch_webpage_content(url)
    if webpage_content:
        soup = BeautifulSoup(webpage_content, 'html.parser')
        text = soup.get_text()
        summary = generate_summary(text, num_sentences)
        return summary
    else:
        return None


if __name__ == "__main__":
    url = "https://www.storylane.io/"
    summary = summarize_webpage(url)
    if summary:
        print("Summary:")
        print(summary)
    else:
        print("Failed to summarize the webpage.")
