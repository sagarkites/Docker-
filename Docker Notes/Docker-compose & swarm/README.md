# Documentation of Docker-compose & Docker-swarm
* Deploy composefile - **docker-compose up**
* Deploy in backgeound - **docker-compose up -d**
* Check the response - **docker-compose ps**
* Start,stop,restart,abort - **docker-compose start, stop, restart, down**
* Instialization of swarm - **docker swarm init --advertise-addr swarm manager private IP**
* Copy & paste the generated Token in Woker Nodes
* Deploy all worker Nodes from Manager - **docker service create --name image**
* Check Response of Nodes - **docker node ls**
* Make worker Node as Manager && Manager as worker - **docker node promote node id or name && docker node demote node id or name**
* Remove Node && Swarm permenently - **docker rm -rf node id or name && docker swarm leave**
* Deploy Stack - **docker stack deploy --compose-file docker-compose.yml nameofstack**
* Ckeck Response - **docker stack ls**

