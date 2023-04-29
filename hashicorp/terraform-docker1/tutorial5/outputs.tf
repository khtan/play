output "container_id" {
       description = "ID of nginx container"
       value = docker_container.nginx.id
}
output "image_id" {
       description = "ID of nginx image"
       value = docker_image.nginx.id
}
