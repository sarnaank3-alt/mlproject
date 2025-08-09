resource "aws_lambda_function" "ingest_doc" {
  function_name = "ingest_doc_function"
  handler       = "handler.lambda_handler"
  runtime       = "python3.8"
  role          = aws_iam_role.lambda_exec_ingest.arn
  timeout       = 30

  source_code_hash = filebase64sha256("path/to/your/zip/package.zip")

  environment = {
    VECTOR_STORE_ENDPOINT = aws_vectorstore.endpoint
    S3_BUCKET            = aws_s3_bucket.raw_files.bucket
  }

  depends_on = [aws_iam_role_policy_attachment.lambda_policy_ingest]
}

resource "aws_iam_role" "lambda_exec_ingest" {
  name = "lambda_exec_role_ingest"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Principal = {
          Service = "lambda.amazonaws.com"
        }
        Effect = "Allow"
        Sid    = ""
      },
    ]
  })
}

resource "aws_iam_role_policy_attachment" "lambda_policy_ingest" {
  policy_arn = aws_iam_policy.lambda_policy_ingest.arn
  role       = aws_iam_role.lambda_exec_ingest.name
}

resource "aws_iam_policy" "lambda_policy_ingest" {
  name        = "lambda_policy_ingest"
  description = "IAM policy for Lambda function to access S3 and Vector Store"

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Action = [
          "s3:GetObject",
          "s3:PutObject",
          "s3:ListBucket"
        ]
        Resource = [
          aws_s3_bucket.raw_files.arn,
          "${aws_s3_bucket.raw_files.arn}/*"
        ]
      },
      {
        Effect = "Allow"
        Action = "execute-api:Invoke"
        Resource = aws_vectorstore.api_gateway.arn
      }
    ]
  })
}