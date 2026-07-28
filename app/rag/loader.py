from pathlib import Path

from langchain_community.document_loaders import (
    UnstructuredWordDocumentLoader,
    PyPDFLoader,
)


def load_documents(data_folder="data"):

    documents = []

    data_path = Path(data_folder)

    # Load Word documents
    for file in data_path.glob("*.docx"):

        print(f"Loading {file.name}")

        loader = UnstructuredWordDocumentLoader(str(file))

        documents.extend(loader.load())

    # Load PDF files
    for file in data_path.glob("*.pdf"):

        print(f"Loading {file.name}")

        loader = PyPDFLoader(str(file))

        documents.extend(loader.load())

    return documents