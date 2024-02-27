from config import URLS, MODEL_NAME, TEMPERATURE, CHUNK_SIZE, CHUNK_OVERLAP
from utils.data_loader import load_data_from_urls
from utils.text_processing import split_text_into_chunks
from utils.document_management import create_documents_from_texts
from utils.summarization import summarize_documents

def main():
    data = load_data_from_urls(URLS)
    texts = split_text_into_chunks(data[0].page_content, CHUNK_SIZE, CHUNK_OVERLAP)
    docs = create_documents_from_texts(texts)
    output = summarize_documents(docs, MODEL_NAME, TEMPERATURE)
    print(output["output_text"])

if __name__ == "__main__":
    main()
