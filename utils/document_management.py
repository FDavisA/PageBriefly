from langchain.docstore.document import Document

def create_documents_from_texts(texts):
    return [Document(page_content=t) for t in texts]
