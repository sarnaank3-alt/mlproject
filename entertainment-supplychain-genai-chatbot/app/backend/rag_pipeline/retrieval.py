from typing import List, Dict
import boto3
from your_vector_store_module import VectorStore  # Replace with actual vector store module

class DocumentRetriever:
    def __init__(self, vector_store: VectorStore):
        self.vector_store = vector_store

    def retrieve_documents(self, query: str, top_k: int = 5) -> List[Dict]:
        """
        Retrieve the top K documents based on the query using the vector store.

        Args:
            query (str): The user query to retrieve relevant documents.
            top_k (int): The number of top documents to retrieve.

        Returns:
            List[Dict]: A list of dictionaries containing document metadata and content.
        """
        # Generate embeddings for the query
        query_embedding = self.vector_store.embed_query(query)
        
        # Retrieve top K documents from the vector store
        retrieved_docs = self.vector_store.query(query_embedding, top_k)
        
        return retrieved_docs

    def get_document_content(self, document_id: str) -> str:
        """
        Fetch the content of a document given its ID.

        Args:
            document_id (str): The ID of the document to fetch.

        Returns:
            str: The content of the document.
        """
        s3_client = boto3.client('s3')
        bucket_name = 'your-s3-bucket-name'  # Replace with your S3 bucket name
        s3_key = f'documents/{document_id}'  # Adjust the path as necessary

        response = s3_client.get_object(Bucket=bucket_name, Key=s3_key)
        document_content = response['Body'].read().decode('utf-8')

        return document_content
