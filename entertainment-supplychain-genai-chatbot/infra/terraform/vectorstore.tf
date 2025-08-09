resource "aws_appsync_graphql_api" "vector_store_api" {
  name          = "VectorStoreAPI"
  authentication_type = "API_KEY"
}

resource "aws_appsync_datasource" "vector_store" {
  api_id = aws_appsync_graphql_api.vector_store_api.id
  name   = "VectorStore"
  type   = "AMAZON_DYNAMODB"
  
  dynamodb_config {
    table_name = aws_dynamodb_table.vector_store_table.name
    region     = var.region
  }
}

resource "aws_dynamodb_table" "vector_store_table" {
  name         = "VectorStore"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "id"

  attribute {
    name = "id"
    type = "S"
  }

  attribute {
    name = "embedding"
    type = "S"
  }
}

resource "aws_appsync_resolver" "query_vector" {
  api_id = aws_appsync_graphql_api.vector_store_api.id
  type   = "Query"
  field  = "getVector"

  data_source = aws_appsync_datasource.vector_store.name

  request_template = <<EOF
{
  "version": "2017-02-28",
  "operation": "GetItem",
  "key": {
    "id": $util.dynamodb.toDynamoDBJson($ctx.args.id)
  }
}
EOF

  response_template = <<EOF
$util.toJson($ctx.result)
EOF
}