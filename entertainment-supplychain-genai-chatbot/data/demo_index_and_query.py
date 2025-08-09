import os
import json
import boto3
from vectorstore.driver import VectorStore

# Initialize AWS clients
s3_client = boto3.client('s3')
vector_store = VectorStore()

# Constants
S3_BUCKET_NAME = 'your-s3-bucket-name'
S3_SAMPLE_DOCS_PREFIX = 'sample_docs/'
VECTOR_STORE_INDEX_NAME = 'your-vector-store-index'

def index_documents():
    # List sample documents in S3
    response = s3_client.list_objects_v2(Bucket=S3_BUCKET_NAME, Prefix=S3_SAMPLE_DOCS_PREFIX)
    documents = response.get('Contents', [])

    for doc in documents:
        doc_key = doc['Key']
        if doc_key.endswith('.txt'):
            # Download document
            s3_client.download_file(S3_BUCKET_NAME, doc_key, doc_key.split('/')[-1])
            with open(doc_key.split('/')[-1], 'r') as file:
                content = file.read()
                # Index document in vector store
                vector_store.index_document(VECTOR_STORE_INDEX_NAME, doc_key, content)

            # Clean up local file
            os.remove(doc_key.split('/')[-1])

def query_vector_store(query):
    results = vector_store.query(VECTOR_STORE_INDEX_NAME, query)
    return results

if __name__ == "__main__":
    index_documents()
    query = input("Enter your query: ")
    results = query_vector_store(query)
    print(json.dumps(results, indent=2))