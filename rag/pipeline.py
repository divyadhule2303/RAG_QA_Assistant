from .loader import load_pdfs
from .chunker import chunk_text
from .embedder import create_vectorizer
from .vectorstore import VectorStore
from .retriever import dynamic_retrieve
from .qa import generate_answer
from django.conf import settings
import os


class RAGPipeline:

    def __init__(self):
        self.vectorizer = create_vectorizer()
        self.store = VectorStore(self.vectorizer)

    def build_index(self):

        documents, doc_names = load_pdfs(settings.MEDIA_ROOT)

        all_chunks = []
        all_sources = []

        for doc, name in zip(documents, doc_names):
            chunks = chunk_text(doc)
            all_chunks.extend(chunks)
            all_sources.extend([name] * len(chunks))

        self.store.build(all_chunks, all_sources)

    def query(self, question):

        similarities = self.store.search(question)
        indices = dynamic_retrieve(similarities)

        return generate_answer(
            indices,
            self.store.chunks,
            self.store.chunk_sources
        )
