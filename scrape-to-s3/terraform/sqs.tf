resource "aws_sqs_queue" "main" {
  name                      = "paylesshealth-main"
  delay_seconds             = 0
  max_message_size          = 2048
  message_retention_seconds = 86400
  receive_wait_time_seconds = 1
  redrive_policy = jsonencode({
    deadLetterTargetArn = aws_sqs_queue.dead.arn
    maxReceiveCount     = 4
  })
}

resource "aws_sqs_queue" "dead" {
  name                      = "paylesshealth-dead"
  delay_seconds             = 90
  max_message_size          = 2048
  message_retention_seconds = 345600
  receive_wait_time_seconds = 10
}
