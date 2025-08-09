variable "aws_region" {
  description = "The AWS region where resources will be created."
  type        = string
  default     = "us-east-1"
}

variable "s3_bucket_name" {
  description = "The name of the S3 bucket for storing raw files and backups."
  type        = string
}

variable "rds_instance_type" {
  description = "The instance type for the RDS database."
  type        = string
  default     = "db.t3.micro"
}

variable "db_username" {
  description = "The username for the RDS database."
  type        = string
}

variable "db_password" {
  description = "The password for the RDS database."
  type        = string
  sensitive   = true
}

variable "ecs_cluster_name" {
  description = "The name of the ECS cluster."
  type        = string
}

variable "ecs_service_name" {
  description = "The name of the ECS service."
  type        = string
}

variable "lambda_function_name" {
  description = "The name of the Lambda function for document ingestion."
  type        = string
}

variable "vector_store_type" {
  description = "The type of vector store to use (e.g., 'faiss', 'weaviate')."
  type        = string
  default     = "faiss"
}

variable "max_tool_calls_per_session" {
  description = "The maximum number of tool calls allowed per user session."
  type        = number
  default     = 25
}

variable "token_tracking_enabled" {
  description = "Enable or disable token tracking."
  type        = bool
  default     = true
}