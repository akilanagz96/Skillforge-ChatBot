from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.retrieval import create_retrieval_chain

from rag.llm import get_llm
from rag.prompt import prompt
from rag.retriever import get_retriever


def get_rag_chain():

    llm = get_llm()

    retriever = get_retriever()

    document_chain = create_stuff_documents_chain(
        llm,
        prompt
    )

    retrieval_chain = create_retrieval_chain(
        retriever,
        document_chain
    )

    return retrieval_chain