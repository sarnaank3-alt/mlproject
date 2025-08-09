import pytest
import boto3
from botocore.exceptions import ClientError
from app.backend.main import app  # Assuming the main app is imported from this path

@pytest.fixture
def s3_client():
    return boto3.client('s3')

@pytest.fixture
def setup_s3_bucket(s3_client):
    bucket_name = 'test-s3-fallback-bucket'
    s3_client.create_bucket(Bucket=bucket_name)
    yield bucket_name
    s3_client.delete_bucket(Bucket=bucket_name)

def test_s3_fallback_on_rds_failure(setup_s3_bucket):
    bucket_name = setup_s3_bucket
    test_document = 'test_document.txt'
    test_content = 'This is a test document for S3 fallback.'
    
    # Upload a test document to S3
    s3_client = boto3.client('s3')
    s3_client.put_object(Bucket=bucket_name, Key=test_document, Body=test_content)

    # Simulate RDS failure (this would be done by mocking the RDS calls in the app)
    # Here we assume the app has a method to check RDS availability
    app.rds_available = False  # Mocking RDS as unavailable

    # Call the function that should trigger S3 fallback
    response = app.handle_user_query("What is in the test document?")

    # Check if the response is from S3
    assert response['source'] == f's3://{bucket_name}/{test_document}'
    assert response['content'] == test_content

    # Reset RDS availability for further tests
    app.rds_available = True  # Mocking RDS as available again