# Using Docker

This version of docker is customized for the enviorment that we are using.
We have a folder called workspace to map the data into.

```shell
docker build -t <image_name> .
```

Build within the folder where the dockerfile is contained.

```shell
docker run -v /host/directory:/workspace/ --rm -it --cap-add=SYS_PTRACE --security-opt seccomp=unconfined <image_name>
```

Where host directory is the mtypes folder, mapped to here. The options also allow for gdb to run.

To delete all instances and restart:
```shell
docker rm $(docker ps -a -q)
docker rmi $(docker images -q) 
```  