import os
from langchain.docstore.document import Document
from langchain.text_splitter import CharacterTextSplitter
from langchain_openai import OpenAI
from langchain.chains.summarize import load_summarize_chain
from langchain_community.document_loaders import UnstructuredURLLoader
import openai

urls = ["https://www.storylane.io/"]

loader = UnstructuredURLLoader(urls=urls)
data = loader.load()
# print(data)

text_splitter = CharacterTextSplitter(
    chunk_size=3000,
    chunk_overlap=200, 
    length_function=len, 
)
texts = text_splitter.split_text(data[0].page_content)

docs = [Document(page_content=t) for t in texts[:]]

# print(len(docs))

openai.api_key = os.getenv("OPENAI_API_KEY")
# print(openai.api_key)

llm = OpenAI(model_name="gpt-3.5-turbo-instruct", temperature=0, openai_api_key=openai.api_key)
map_reduce_chain = load_summarize_chain(llm, chain_type="map_reduce")

output = map_reduce_chain.invoke(docs)

print(output)
