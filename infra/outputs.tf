output "bucket_staging" {
  value = aws_s3_bucket.staging_data.bucket
}

output "ip_dev" {
  value = aws_instance.dev.public_ip
}

output "endpoint_prod" {
  value = aws_db_instance.prod.endpoint
}
