resource "aws_efs_file_system" "chatbot_efs" {
  creation_token = "chatbot-efs-${var.environment}"
  performance_mode = "generalPurpose"
  tags = {
    Name = "Chatbot EFS"
    Environment = var.environment
  }
}

resource "aws_efs_mount_target" "chatbot_mount_target" {
  file_system_id = aws_efs_file_system.chatbot_efs.id
  subnet_id      = var.subnet_id
  security_groups = [var.security_group_id]
}

output "efs_id" {
  value = aws_efs_file_system.chatbot_efs.id
}

output "efs_dns_name" {
  value = aws_efs_file_system.chatbot_efs.dns_name
}