resource "aws_s3_bucket" "this" {
  bucket = "paylesshealth-lambda"
}

resource "aws_s3_bucket_acl" "this" {
  bucket = aws_s3_bucket.this.id
  acl    = "private"
}

