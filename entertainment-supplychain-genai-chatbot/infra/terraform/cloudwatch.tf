resource "aws_cloudwatch_metric_alarm" "high_token_usage" {
  alarm_name          = "HighTokenUsage"
  comparison_operator = "GreaterThanThreshold"
  evaluation_periods  = "1"
  metric_name        = "TokenUsage"
  namespace          = "YourNamespace"
  period             = "60"
  statistic          = "Sum"
  threshold          = "1000"
  alarm_description  = "Alarm when token usage exceeds 1000 in a minute"
  actions_enabled    = true
  alarm_actions      = [aws_sns_topic.alerts.arn]
}

resource "aws_cloudwatch_metric_alarm" "tool_call_budget_exhaustion" {
  alarm_name          = "ToolCallBudgetExhaustion"
  comparison_operator = "GreaterThanThreshold"
  evaluation_periods  = "1"
  metric_name        = "ToolCallsCount"
  namespace          = "YourNamespace"
  period             = "60"
  statistic          = "Sum"
  threshold          = "25"
  alarm_description  = "Alarm when tool call budget is exhausted"
  actions_enabled    = true
  alarm_actions      = [aws_sns_topic.alerts.arn]
}

resource "aws_cloudwatch_metric_alarm" "rds_failover" {
  alarm_name          = "RDSFailover"
  comparison_operator = "GreaterThanThreshold"
  evaluation_periods  = "1"
  metric_name        = "DatabaseConnections"
  namespace          = "AWS/RDS"
  period             = "60"
  statistic          = "Average"
  threshold          = "0"
  alarm_description  = "Alarm when RDS database connections drop to 0"
  actions_enabled    = true
  alarm_actions      = [aws_sns_topic.alerts.arn]
}

resource "aws_cloudwatch_metric_alarm" "high_latency" {
  alarm_name          = "HighLatency"
  comparison_operator = "GreaterThanThreshold"
  evaluation_periods  = "1"
  metric_name        = "Latency"
  namespace          = "YourNamespace"
  period             = "60"
  statistic          = "Average"
  threshold          = "2000"
  alarm_description  = "Alarm when API latency exceeds 2000 ms"
  actions_enabled    = true
  alarm_actions      = [aws_sns_topic.alerts.arn]
}