terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0.1"
    }
  }
}

provider "docker" {
   host = "npipe:////.//pipe//docker_engine"
}

resource "docker_image" "nginx" {
  name = "nginx"
  keep_locally = false
}

resource "docker_container" "nginx" {
  image = "${docker_image.nginx.name}:latest"
  name  = "tutorial"
  ports {
    internal = 80
    external = 8000
  }
}