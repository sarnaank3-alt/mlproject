resource "aws_db_instance" "main" {
  identifier              = "entertainment-supplychain-db"
  engine                 = "postgres"
  engine_version         = "13.3"
  instance_class         = "db.t3.micro"
  allocated_storage       = 20
  storage_type           = "gp2"
  username               = var.db_username
  password               = var.db_password
  db_name                = var.db_name
  publicly_accessible     = false
  skip_final_snapshot    = true

  tags = {
    Name = "Entertainment Supply Chain RDS"
  }

  lifecycle {
    prevent_destroy = true
  }
}

resource "aws_db_subnet_group" "main" {
  name       = "entertainment-supplychain-db-subnet-group"
  subnet_ids = var.db_subnet_ids

  tags = {
    Name = "Entertainment Supply Chain DB Subnet Group"
  }
}

resource "aws_db_parameter_group" "main" {
  name   = "entertainment-supplychain-db-parameter-group"
  family = "postgres13"

  parameter {
    name  = "max_connections"
    value = "100"
  }

  tags = {
    Name = "Entertainment Supply Chain DB Parameter Group"
  }
}