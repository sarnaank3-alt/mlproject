resource "aws_ecs_cluster" "chatbot_cluster" {
  name = "entertainment-supplychain-cluster"
}

resource "aws_ecs_task_definition" "chatbot_task" {
  family                   = "chatbot-task"
  network_mode             = "awsvpc"
  requires_compatibilities  = ["FARGATE"]
  cpu                      = "256"
  memory                   = "512"

  container_definitions = jsonencode([
    {
      name      = "chatbot-backend"
      image     = "<your_backend_image_uri>"
      essential = true
      portMappings = [
        {
          containerPort = 8000
          hostPort      = 8000
          protocol      = "tcp"
        }
      ]
      environment = [
        {
          name  = "DATABASE_URL"
          value = "<your_database_url>"
        },
        {
          name  = "VECTOR_STORE_URL"
          value = "<your_vector_store_url>"
        }
      ]
    },
    {
      name      = "chatbot-streamlit"
      image     = "<your_streamlit_image_uri>"
      essential = true
      portMappings = [
        {
          containerPort = 8501
          hostPort      = 8501
          protocol      = "tcp"
        }
      ]
    }
  ])
}

resource "aws_ecs_service" "chatbot_service" {
  name            = "chatbot-service"
  cluster         = aws_ecs_cluster.chatbot_cluster.id
  task_definition = aws_ecs_task_definition.chatbot_task.arn
  desired_count   = 1
  launch_type     = "FARGATE"

  network_configuration {
    subnets          = ["<your_subnet_id>"]
    security_groups  = ["<your_security_group_id>"]
    assign_public_ip = true
  }
}