from sklearn.metrics.pairwise import cosine_similarity

class VectorStore:

    def __init__(self, vectorizer):
        self.vectorizer = vectorizer
        self.matrix = None
        self.chunks = []
        self.chunk_sources = []

    def build(self, chunks, sources):
        self.chunks = chunks
        self.chunk_sources = sources
        self.matrix = self.vectorizer.fit_transform(chunks)

    def search(self, query):
        query_vec = self.vectorizer.transform([query])
        similarities = cosine_similarity(query_vec, self.matrix)[0]
        return similarities
