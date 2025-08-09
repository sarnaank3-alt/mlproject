def lambda_handler(event, context):
    import json
    import boto3
    from utils.embedding import generate_embeddings

    s3_client = boto3.client('s3')
    vector_store_client = boto3.client('your_vector_store_service')  # Replace with actual vector store service client

    bucket_name = event['bucket']
    document_key = event['key']

    try:
        # Retrieve the document from S3
        response = s3_client.get_object(Bucket=bucket_name, Key=document_key)
        document_content = response['Body'].read().decode('utf-8')

        # Generate embeddings for the document
        embeddings = generate_embeddings(document_content)

        # Index the document and its embeddings into the vector store
        vector_store_client.index_document(
            document_id=document_key,
            content=document_content,
            embeddings=embeddings
        )

        return {
            'statusCode': 200,
            'body': json.dumps('Document ingested and indexed successfully.')
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error ingesting document: {str(e)}')
        }