from config import URLS, MODEL_NAME, TEMPERATURE, CHUNK_SIZE, CHUNK_OVERLAP, RECIPIENT_EMAIL, SENDER_EMAIL, SENDER_PASSWORD
from utils.data_loader import load_data_from_urls
from utils.text_processing import split_text_into_chunks
from utils.document_management import create_documents_from_texts
from utils.summarization import summarize_documents
from utils.email_sender import send_email
from utils.email_content import generate_html_email_body

def main():
    data = load_data_from_urls(URLS)
    texts = split_text_into_chunks(data[0].page_content, CHUNK_SIZE, CHUNK_OVERLAP)
    docs = create_documents_from_texts(texts)
    output = summarize_documents(docs, MODEL_NAME, TEMPERATURE)
    
    email_body = generate_html_email_body(URLS[0], output["output_text"])
    dynamic_subject = f"{URLS[0]} Briefly"
    send_email(dynamic_subject, email_body, RECIPIENT_EMAIL, SENDER_EMAIL, SENDER_PASSWORD)

if __name__ == "__main__":
    main()
