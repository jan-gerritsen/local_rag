# https://medium.com/@rubentak/talk-to-your-files-in-a-local-rag-application-using-mistral-7b-langchain-and-chroma-db-no-2b4ba77358e0
# Import libraries
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.llms import Ollama
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain_community.embeddings import OllamaEmbeddings
from langchain.prompts import PromptTemplate
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders import DirectoryLoader
from langchain.chains import RetrievalQA
import logging

from rag_server import retrieve_and_respond

# Ollama embeddings
embeddings_open = OllamaEmbeddings(model="Llama2")

llm_open = Ollama(model='Llama2',
                    callback_manager = CallbackManager([StreamingStdOutCallbackHandler()]))


def load_documents_into_chroma():
    loader = DirectoryLoader('./../../data/')

    doc = loader.load()
    logging.debug(f'Number of documents loaded: {len(doc)}')

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    texts = text_splitter.split_documents(doc)

    # persist documents in Chroma for future RAG use
    persist_directory = 'alice_chroma'
    vectordb = Chroma.from_documents(documents=texts,
                                 embedding=embeddings_open,
                                 persist_directory=persist_directory)
    vectordb.persist()


if __name__ == "__main__":
    load_documents_into_chroma()
    # test if it worked
    the_answer = retrieve_and_respond('Is the queen a nice person?')
    print(the_answer)
