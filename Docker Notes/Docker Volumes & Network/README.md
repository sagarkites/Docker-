# Documentation of Docker Volumes and Network in Centos
* Create Volume Locally - **docker volume create --name name_of_volume**
* List Volumes - **docker volume ls** 
* Location of Volume - **/var/lib/docker/volumes/specfiedhexadir/_data**
* Attach local volume to the Conatiner - **docker run -it --name name -v localdir:/conatinerdir image**
* Create network - **docker network create --driver bridge some_name**
* Gateway & subnet - **docker network create --driver bridge --subnet=ip/cidr --gateway=ip some_name**
* Gateway & subnet with iplimits - **docker network create --driver bridge --subnet=ip/cidr --gateway=ip --ip-range=ip some_name**
* Attach custom network to the container - **docker run -it --name name --net docker_network image**
