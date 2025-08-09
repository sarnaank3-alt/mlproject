output "s3_bucket_name" {
  value = aws_s3_bucket.raw_files.bucket
}

output "rds_endpoint" {
  value = aws_db_instance.main.endpoint
}

output "ecs_cluster_name" {
  value = aws_ecs_cluster.main.name
}

output "lambda_function_name" {
  value = aws_lambda_function.ingest_doc.function_name
}