# Communication between two Containers
* Create Newtwork - **docker network create --driver overlay name**
* Image - **docker pull mysql:latest**
* Run Backround - **docker run -d --name mysql-server --network bridge n/w -e MYSQL_ROOT_PASSWORD=pass image**
* Enter Container - **docker run -it --rm --network brideg n/w mysql sh -c 'exec mysql -h"hostname" -P"3306" -uroot -p"pass"'**
* Directory - **mkdir build && cd build**
* Build Image - **docker build -t name .**
* Run image background - **docker run -it --rm --network my-network image**
