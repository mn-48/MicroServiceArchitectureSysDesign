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
