terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0.2"
    }
  }
}

variable "container_name" {
   description = "Name of Nginx container"
   type = string
   default = "ExampleNginxContainer"
}

provider "docker" {}

resource "docker_image" "nginx" {
  name         = "nginx:latest"
  keep_locally = false
}

resource "docker_container" "nginx" {
  image = docker_image.nginx.image_id
  name  = var.container_name
  ports {
    internal = 80
    external = 8080
  }
}

output "container_id" {
       description = "ID of nginx container"
       value = docker_container.nginx.id
}
output "image_id" {
       description = "ID of nginx image"
       value = docker_image.nginx.id
}
