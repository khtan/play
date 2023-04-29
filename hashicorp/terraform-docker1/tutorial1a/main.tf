terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0.1"
    }
  }
}

data "external" "os_type" {
   program = ["sh", "-c", "uname -s | jq -R '{ os: .}'"]
}

locals {
  os_type = data.external.os_type.result == "Linux" ? "linux" : "windows"
}

provider "docker" {
   host = local.os_type == "windows" ? "npipe:////.//pipe//docker_engine" : null
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

output "os_type" {
 value = local.os_type
}
