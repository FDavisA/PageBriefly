from langchain_openai import ChatOpenAI
from langchain.chains.summarize import load_summarize_chain
import openai
from config import OPENAI_API_KEY

def summarize_documents(docs, model_name="gpt-4", temperature=1):
    openai.api_key = OPENAI_API_KEY
    llm = ChatOpenAI(model_name=model_name, temperature=temperature)
    summarize_chain = load_summarize_chain(llm)
    output = summarize_chain.invoke(docs)
    return output
