provider "aws" {
  region = "us-west-2"
}

resource "aws_s3_bucket" "raw_files" {
  bucket = "entertainment-supplychain-raw-files"
  acl    = "private"
}

resource "aws_s3_bucket" "vector_store_dumps" {
  bucket = "entertainment-supplychain-vector-store-dumps"
  acl    = "private"
}

resource "aws_s3_bucket" "db_backups" {
  bucket = "entertainment-supplychain-db-backups"
  acl    = "private"
}

resource "aws_db_instance" "main" {
  identifier          = "entertainment-supplychain-db"
  engine              = "postgres"
  engine_version      = "13.3"
  instance_class      = "db.t3.micro"
  allocated_storage   = 20
  username            = var.db_username
  password            = var.db_password
  db_name             = "entertainment_db"
  skip_final_snapshot = true
}

resource "aws_ecs_cluster" "main" {
  name = "entertainment-supplychain-cluster"
}

resource "aws_efs_file_system" "shared_storage" {
  creation_token = "entertainment-supplychain-efs"
}

resource "aws_iam_role" "ecs_task_execution_role" {
  name = "ecsTaskExecutionRole"
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Action = "sts:AssumeRole"
      Principal = {
        Service = "ecs-tasks.amazonaws.com"
      }
      Effect = "Allow"
      Sid    = ""
    }]
  })
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