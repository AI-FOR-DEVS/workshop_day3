from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import InMemoryVectorStore

loader = PyPDFLoader("report.pdf")
docs = loader.load()

splitter = RecursiveCharacterTextSplitter(chunk_size=5000, chunk_overlap=1000)

splits = splitter.split_documents(docs)

embeddings = OpenAIEmbeddings()
in_memory_vector_store = InMemoryVectorStore.from_documents(splits, embeddings)


def get_results(query): 
    results = in_memory_vector_store.similarity_search(query, k=2)

    return results

if __name__ == "__main__":
    query = "Who is the architect of the Umwelthaus?"
    print(get_results(query))