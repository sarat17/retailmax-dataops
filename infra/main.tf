# ============================================================
#  RetailMax DataOps - Infraestructura
# ============================================================
terraform {
  required_version = ">= 1.6"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = var.region
  default_tags {
    tags = {
      Proyecto   = "retailmax-dataops"
      Gestionado = "terraform"
    }
  }
}

# ---------- 1. Bucket S3 para datos de staging (QA) ----------
resource "aws_s3_bucket" "staging_data" {
  bucket = "retailmax-staging-data"
  tags   = { Entorno = "qa" }
}

resource "aws_s3_bucket_versioning" "staging_data" {
  bucket = aws_s3_bucket.staging_data.id
  versioning_configuration {
    status = "Enabled"
  }
}

resource "aws_s3_bucket_server_side_encryption_configuration" "staging_data" {
  bucket = aws_s3_bucket.staging_data.id
  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "AES256"
    }
  }
}

resource "aws_s3_bucket_public_access_block" "staging_data" {
  bucket                  = aws_s3_bucket.staging_data.id
  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}

# ---------- 2. Instancia EC2 para DEV ----------
data "aws_ami" "ubuntu" {
  most_recent = true
  owners      = ["099720109477"]
  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd/ubuntu-jammy-22.04-amd64-server-*"]
  }
}

resource "aws_instance" "dev" {
  ami                  = data.aws_ami.ubuntu.id
  instance_type        = var.tipo_instancia_dev
  iam_instance_profile = aws_iam_instance_profile.dev.name
  user_data            = <<-EOF
    #!/bin/bash
    apt-get update -y
    apt-get install -y docker.io git
  EOF
  tags = {
    Name    = "retailmax-dev"
    Entorno = "dev"
  }
}

# ---------- 3. Base de datos RDS para PROD ----------
resource "aws_db_instance" "prod" {
  identifier                  = "retailmax-prod-db"
  engine                      = "postgres"
  engine_version              = "16"
  instance_class              = "db.m6g.large"
  allocated_storage           = 100
  db_name                     = "retailmax"
  username                    = "retailmax_admin"
  manage_master_user_password = true
  multi_az                    = true
  storage_encrypted           = true
  backup_retention_period     = 14
  deletion_protection         = true
  publicly_accessible         = false
  skip_final_snapshot         = false
  final_snapshot_identifier   = "retailmax-prod-final"
  tags                        = { Entorno = "prod" }
}

# ---------- 4. Rol IAM con permisos restringidos ----------
resource "aws_iam_role" "dev_lectura" {
  name = "retailmax-dev-solo-lectura"
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect    = "Allow"
      Principal = { Service = "ec2.amazonaws.com" }
      Action    = "sts:AssumeRole"
    }]
  })
}

resource "aws_iam_policy" "leer_staging" {
  name = "retailmax-leer-staging"
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect = "Allow"
      Action = ["s3:GetObject", "s3:ListBucket"]
      Resource = [
        aws_s3_bucket.staging_data.arn,
        "${aws_s3_bucket.staging_data.arn}/*"
      ]
    }]
  })
}

resource "aws_iam_role_policy_attachment" "dev_lectura" {
  role       = aws_iam_role.dev_lectura.name
  policy_arn = aws_iam_policy.leer_staging.arn
}

resource "aws_iam_instance_profile" "dev" {
  name = "retailmax-dev-profile"
  role = aws_iam_role.dev_lectura.name
}


resource "aws_s3_bucket" "datos_chile" {
  bucket = "retailmax-datos-chile"
  tags   = { Entorno = "qa", Pais = "CL" }
}