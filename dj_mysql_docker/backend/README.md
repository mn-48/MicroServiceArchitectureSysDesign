# Run 
```
docker-compose up --build

# for detuch mode

docker-compose up -d --build 

# Migrate database:

docker-compose exec web python manage.py makemigrations


docker-compose exec web python manage.py migrate


docker-compose exec web python manage.py createsuperuser


sudo chmod -R 755 .mysql_data

```


## Putting It All Together
```
# Stop all running containers
docker stop $(docker ps -q)

# Remove all containers
docker rm $(docker ps -a -q)

# Remove all images
docker rmi $(docker images -q)

# Remove all volumes
docker volume rm $(docker volume ls -q)

# Remove all networks
docker network rm $(docker network ls -q)

```




```
docker-compose exec web python manage.py createsuperuser
```

# Access Container Shell
```
docker exec -it  backend_web_1 /bin/bash
```