from sentence_transformers import SentenceTransformer
import numpy as np

class EmbeddingUtils:
    def __init__(self, model_name='all-MiniLM-L6-v2'):
        self.model = SentenceTransformer(model_name)

    def generate_embeddings(self, documents):
        """
        Generate embeddings for a list of documents.

        :param documents: List of strings, where each string is a document.
        :return: Numpy array of embeddings.
        """
        embeddings = self.model.encode(documents, convert_to_numpy=True)
        return embeddings

    def normalize_embeddings(self, embeddings):
        """
        Normalize the embeddings to unit length.

        :param embeddings: Numpy array of embeddings.
        :return: Numpy array of normalized embeddings.
        """
        norms = np.linalg.norm(embeddings, axis=1, keepdims=True)
        normalized_embeddings = embeddings / norms
        return normalized_embeddings

    def compute_similarity(self, embedding1, embedding2):
        """
        Compute cosine similarity between two embeddings.

        :param embedding1: Numpy array of the first embedding.
        :param embedding2: Numpy array of the second embedding.
        :return: Cosine similarity score.
        """
        dot_product = np.dot(embedding1, embedding2)
        return dot_product[0]  # Return the scalar similarity score