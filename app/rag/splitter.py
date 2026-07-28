from pathlib import Path

from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter



COURSE_DISPLAY_NAMES = {
    "11_Data_Analytics": "Data Analytics Professional Program",
    "12_Data_Science": "Data Science Professional Program",
    "13_AI_ML": "AI & Machine Learning Professional Program",
    "14_GenAI": "Generative AI Professional Program",
    "15_Python": "Python Programming Professional Program",
    "16_SQL": "SQL Professional Program",
    "17_PowerBI": "Power BI Professional Program",
    "18_Excel": "Excel for Business Professional Program",
    "19_cloud": "Cloud Computing Professional Program",
    "20_UI_UX": "UI/UX Design Professional Program",
    "21_Digital_marketing": "Digital Marketing Professional Program",
    "22_cybersecurity": "Cybersecurity Professional Program",
}


def get_document_name(source: str) -> str:
    return Path(source).stem


def get_document_metadata(source: str):
    name = get_document_name(source)

    if name in COURSE_DISPLAY_NAMES:
        return {
            "document_type": "course",
            "course_name": COURSE_DISPLAY_NAMES[name],
        }

    return {
        "document_type": "document",
        "course_name": None,
    }


def split_documents(documents):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=150,
    )

    chunks = splitter.split_documents(documents)

    enriched_chunks = []

    for chunk in chunks:

        source = chunk.metadata.get("source", "Unknown")

        document_info = get_document_metadata(source)

        metadata = {
            **chunk.metadata,
            **document_info,
        }

        title = (
            document_info["course_name"]
            if document_info["document_type"] == "course"
            else get_document_name(source)
        )

        enriched_content = f"""
        Document: {title}

        {chunk.page_content}
        """.strip()

        enriched_chunk = Document(
            page_content=enriched_content,
            metadata=metadata,
        )

        enriched_chunks.append(enriched_chunk)

    return enriched_chunks