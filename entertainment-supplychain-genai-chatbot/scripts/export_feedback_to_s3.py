import boto3
import json
import os
from botocore.exceptions import ClientError

def export_feedback_to_s3(feedback_data, bucket_name, feedback_file_name):
    """
    Exports user feedback data to an S3 bucket.

    Parameters:
    feedback_data (dict): The feedback data to export.
    bucket_name (str): The name of the S3 bucket.
    feedback_file_name (str): The name of the file to save the feedback as in S3.
    """
    s3_client = boto3.client('s3')

    try:
        # Convert feedback data to JSON
        feedback_json = json.dumps(feedback_data)

        # Upload the feedback data to S3
        s3_client.put_object(
            Bucket=bucket_name,
            Key=feedback_file_name,
            Body=feedback_json,
            ContentType='application/json'
        )
        print(f"Feedback exported successfully to s3://{bucket_name}/{feedback_file_name}")

    except ClientError as e:
        print(f"Failed to export feedback to S3: {e}")

if __name__ == "__main__":
    # Example usage
    feedback = {
        "user_id": "12345",
        "session_id": "abcde",
        "feedback": "This response was helpful.",
        "rating": 5
    }
    bucket = os.getenv('FEEDBACK_BUCKET')
    file_name = "user_feedback.json"
    
    export_feedback_to_s3(feedback, bucket, file_name)