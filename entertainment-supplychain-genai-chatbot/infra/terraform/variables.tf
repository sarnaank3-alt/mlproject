variable "subnet_id" {
  description = "Subnet ID for EFS mount target"
  type        = string
}

variable "security_group_id" {
  description = "Security group ID for EFS mount target"
  type        = string
}

variable "db_username" {
  description = "Database username"
  type        = string
}

variable "db_password" {
  description = "Database password"
  type        = string
  sensitive   = true
}