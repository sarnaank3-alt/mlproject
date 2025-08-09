variable "environment" {
  description = "Deployment environment (e.g. dev, prod)"
  type        = string
  default     = "dev"
}

variable "db_name" {
  description = "Database name"
  type        = string
  default     = "entertainment_db"
}

variable "db_subnet_ids" {
  description = "List of subnet IDs for RDS"
  type        = list(string)
  default     = []
}

variable "region" {
  description = "AWS region"
  type        = string
  default     = "us-west-2"
}