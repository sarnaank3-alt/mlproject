provider "aws" {
  region = "us-west-2"
}

resource "aws_s3_bucket" "raw_files" {
  bucket = "entertainment-supplychain-raw-files"
}

resource "aws_s3_bucket" "vector_store_dumps" {
  bucket = "entertainment-supplychain-vector-store-dumps"
}

resource "aws_s3_bucket" "db_backups" {
  bucket = "entertainment-supplychain-db-backups"
}

resource "aws_ecs_cluster" "main" {
  name = "entertainment-supplychain-cluster"
}

resource "aws_efs_file_system" "shared_storage" {
  creation_token = "entertainment-supplychain-efs"
}

resource "aws_cloudwatch_log_group" "ecs_logs" {
  name = "/ecs/entertainment-supplychain"
}

resource "aws_cloudwatch_metric_alarm" "high_cpu" {
  alarm_name          = "HighCPUUtilization"
  comparison_operator = "GreaterThanThreshold"
  evaluation_periods  = "1"
  metric_name         = "CPUUtilization"
  namespace           = "AWS/ECS"
  period              = "60"
  statistic           = "Average"
  threshold           = "80"
  alarm_description   = "This alarm triggers when CPU utilization exceeds 80%"
  dimensions = {
    ClusterName = aws_ecs_cluster.main.name
    ServiceName = "your_service_name"
  }
}