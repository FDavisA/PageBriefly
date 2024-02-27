from summarizer.scraper import fetch_webpage_content, extract_text
from summarizer.preprocessor import clean_text
from summarizer.summarization import summarize_text


def main():
    url = "https://www.linkedin.com/in/davisaf/"
    html_content = fetch_webpage_content(url)
    text = extract_text(html_content)
    cleaned_text = clean_text(text)
    summary = summarize_text(cleaned_text)
    print(summary)


if __name__ == '__main__':
    main()
