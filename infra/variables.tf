variable "region" {
  description = "Región de AWS"
  type        = string
  default     = "us-east-1"
}

variable "tipo_instancia_dev" {
  description = "Tamaño de la máquina de DEV"
  type        = string
  default     = "t3.medium"
}
