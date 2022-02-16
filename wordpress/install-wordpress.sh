#!/bin/bash

docker network create -d bridge wp

docker run -d -p 3306:3306 --name db -e MYSQL_DATABASE=wpdb \
     -e MYSQL_USER=whale -e MYSQL_PASSWORD=examplepass -e MYSQL_RANDOM_ROOT_PASSWORD=1 \
     --network=wp --restart=always mysql:5.7 

docker run -d -p 8080:80 --name wordpress -e WORDPRESS_DB_HOST=db:3306 \
    -e WORDPRESS_DB_USER=whale -e WORDPRESS_DB_PASSWORD=examplepass \
    -e WORDPRESS_DB_NAME=wpdb --network=wp --restart=always wordpress:php7.4