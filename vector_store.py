from langchain.text_splitter import RecursiveCharacterTextSplitter                              #split long doc into chunks
from langchain.embeddings import HuggingFaceEmbeddings                                          #embedding model(text --> dense vector)
from langchain_community.vectorstores import Chroma                                             #local vector database to store and retrieve text chunks
from langchain.schema import Document                                                           #data structure used by langchaim to represent doc

def create_retriever(text, persist_directory="db"):                                             #chroma will save its data in "db"
    documents = [Document(page_content=text)]
    
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)           #splits text into chunks max=500 
    splits = text_splitter.split_documents(documents)

    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")      # used for creating dense vector 
    vectordb = Chroma.from_documents(
        documents=splits,
        embedding=embeddings,
        persist_directory=persist_directory
    )
    return vectordb.as_retriever(search_kwargs={"k": 3})                                           




####all-MiniLM-L6-v2##########################
# 6 layers
# output=384 dimensional dense vector
##### Use cases###############################
# - Semantic search
# - FAQ matching
# - Clustering similar sentences
# - Text classification
# - Retrieval-augmented generation (RAG)
###############################################