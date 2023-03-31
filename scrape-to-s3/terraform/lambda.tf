#data "archive_file" "this" {
#  type        = "zip"
#  source_file = "../lambda.py"
#  output_path = "${path.module}/scraper.zip"
#}
#
#resource "aws_s3_object" "this" {
#  bucket = aws_s3_bucket.this.id
#  key    = "scraper.zip"
#  source = data.archive_file.this.output_path
#  etag   = filemd5(data.archive_file.this.output_path)
#}

resource "aws_lambda_function" "scraper" {
  function_name = "scraper"
  package_type  = "Image"
  image_uri     = "566613373177.dkr.ecr.us-east-2.amazonaws.com/scraper:latest"
  role          = aws_iam_role.this.arn
  timeout       = 15
  memory_size   = 128
}

resource "aws_cloudwatch_log_group" "this" {
  name = "/aws/lambda/${aws_lambda_function.scraper.function_name}"

  retention_in_days = 1
}

resource "aws_lambda_event_source_mapping" "sqs" {
  event_source_arn                   = aws_sqs_queue.main.arn
  function_name                      = aws_lambda_function.scraper.function_name
  batch_size                         = 1
  maximum_batching_window_in_seconds = 0
}