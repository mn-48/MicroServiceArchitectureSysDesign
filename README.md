# MicroServiceArchitectureSysDesign

![MicroServiceArchitecture.jpg](/doc/images/MicroServiceArchitecture.jpg)

# ------------------------ admin project --------------------------------------

### 1. Build Image named `admin`

`docker build -t admin .`

### 2. Run Container named `admin-container` using `admin` image

`docker run -p 8000:8000 --name admin-container admin`

_run detuched Mode Terminal_
`docker run -d -p 8000:8000 --name admin-container admin`

### 3. If get error to run container --> Stop Running Container whose name `admin-container`

`docker stop admin-container`

### 4. Remove `admin-container` and and Run new container named `admin-container` as same as before

`docker run --rm -d -p 8000:8000 --name admin-container admin`

### [Note:] Get Updated code effect -->

> (1) bulid image

> (2) first stop container

> (3) remove container

> (4) run container


#### Install MySQL Srver
```
sudo apt-get update
sudo apt-get install mysql-server

mysql --version

```


```
sudo mysql -u root -p

show databases;

use mysql

update user set plugin='mysql_native_password' where user='root'; 

flush privileges;

exit

```


```
mysql -u root -p
create database demo;
show databases;

```




