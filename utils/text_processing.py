from langchain.text_splitter import CharacterTextSplitter

def split_text_into_chunks(text, chunk_size=3000, chunk_overlap=200):
    text_splitter = CharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        length_function=len,
    )
    texts = text_splitter.split_text(text)
    return texts
from langchain.text_splitter import CharacterTextSplitter

def split_text_into_chunks(text, chunk_size=3000, chunk_overlap=200):
    text_splitter = CharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        length_function=len,
    )
    texts = text_splitter.split_text(text)
    return texts
