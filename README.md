
# 2020_group_06_s4210875_s4199456_s4208110

## Monitoring Spark

### Dependencies

* [Python 3.7](https://www.python.org/downloads/release/python-370/)
* [Docker](https://www.docker.com/)
* [Pyspark 2.4.5](https://spark.apache.org/docs/latest/)
* [Pika](https://github.com/pika/pika)
* [RabbitMQ 3.8.3-rc.1](https://github.com/rabbitmq/rabbitmq-server/releases/tag/v3.8.3-rc.1)

### Run the program

* To run `docker-compose up`

* To run in detached mode `docker-compose up -d`

* To see the logs of a specific, container, first find the container name by running `docker ps -a`, then run `docker container logs <container_name>`

* To see the network details in which all the containers of this project are running, first find the network name from `docker network ls`, then run `docker network inspect <network_name>`

* To clean up `docker-compose down -v --rmi all --remove-orphans`

* We can run separate container by `docker-compose up <container_name>` where `container_name` is one of the service names from the `docker-compose.yml`

* While the containers are running, we can monitor the queue on the dashboard http://localhost:15672/ with [Username/Password] as `[guest/guest]`
