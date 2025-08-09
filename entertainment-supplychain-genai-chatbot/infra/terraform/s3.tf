resource "aws_s3_bucket" "raw_files" {
  bucket = "entertainment-supplychain-raw-files"
  acl    = "private"
}

resource "aws_s3_bucket" "vector_store_dumps" {
  bucket = "entertainment-supplychain-vector-store-dumps"
  acl    = "private"
}

resource "aws_s3_bucket" "backup_db_snapshots" {
  bucket = "entertainment-supplychain-backup-db-snapshots"
  acl    = "private"
}