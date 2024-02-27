from langchain_openai import OpenAI, ChatOpenAI
from langchain.chains.summarize import load_summarize_chain
from config import OPENAI_API_KEY

def get_llm(model_name, temperature=1):
    if model_name == "gpt-3.5-turbo-instruct":
        return OpenAI(model_name=model_name, temperature=temperature, openai_api_key=OPENAI_API_KEY)
    elif model_name == "gpt-4":
        return ChatOpenAI(model_name=model_name, temperature=temperature)
    else:
        raise ValueError(f"Unsupported model name: {model_name}")

def summarize_documents(docs, model_name="gpt-4", temperature=1, chain_type=None):
    llm = get_llm(model_name, temperature)
    if model_name == "gpt-3.5-turbo-instruct":
        summarize_chain = load_summarize_chain(llm, chain_type="map_reduce")
    else:
        summarize_chain = load_summarize_chain(llm)
    output = summarize_chain.invoke(docs)
    return output
