# nginx_load_balancing


# reload
```
# it is good practice than restart
sudo nginx -s reload
```


## setup
```
 docker-compose down
 docker-compose up
 docker-compose up --build
 docker logs -f nginx_nginx_1

```


## Loadbalancer for both http and https
```
upstream backend  {
    ip_hash;
    server <server-1-ip>;
    server <server-2-ip>;
}

upstream backend_ssl {
    ip_hash;
    server <server-1-ip>:443;
    server <server-2-ip>:443;
}

server {
    location / {
        proxy_pass http://backend;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

}

server {
    listen 443 ssl;
    ssl_certificate /etc/nginx/ssl/mycert.crt;
    ssl_certificate_key /etc/nginx/ssl/mykey.key;
    location / {
        proxy_pass https://backend_ssl;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```



## worker_processes and worker_connections
```
worker_processes:
A worker process is a single-threaded process.
If Nginx is doing CPU-intensive work such as SSL or gzipping and you have 2 or more CPUs/cores, then you may set worker_processes to be equal to the number of CPUs or cores.

If you are serving a lot of static files and the total size of the files is bigger than the available memory, then you may increase worker_processes to fully utilize disk bandwidth.

Nginx worker process that handles the incoming request.
Set this to worker_process auto; to automatically adjust the number of Nginx worker processes based on available cores.
This can go beyond the available cores if you have IO access.


worker_connections:
The worker_connections and worker_processes from the main section allows you to calculate max clients you can handle:
max clients = worker_processes * worker_connections
max clients = 32 * 1024 = 32768

worker_connections is the number of simultaneous connections; so they are simply stating how to calculate, for example:
 1. you are only running 1 process with 512 connections, you will only be able to serve 512 clients.
 2. If 2 processes with 512 connections each, you will be able to handle 2x512=1024 clients.
The number of connections is limited by the maximum number of open files (RLIMIT_NOFILE) on your system

Each worker process can open by default 512 connections.
You can change this limit by worker_connections <no>.
You can set this to max limit ulimit -n.
hence,
max_clients = worker processes * worker connections

# https://www.javatpoint.com/nginx-introduction
[shoumitro@shoumitro-pc nginx_ex]$ ps -ef | grep nginx  
root        3035    3014  0 21:23 ?        00:00:00 nginx: master process nginx -g daemon off;
101         3103    3035  0 21:23 ?        00:00:00 nginx: worker process
101         3104    3035  0 21:23 ?        00:00:00 nginx: worker process
101         3105    3035  0 21:23 ?        00:00:00 nginx: worker process
101         3106    3035  0 21:23 ?        00:00:00 nginx: worker process
shoumit+    7825    7556  0 21:57 pts/5    00:00:00 grep --colour=auto nginx

```
![](https://github.com/shoumitro-cse/nginx_load_balancing/blob/main/images/nginx.png?raw=true)


##  nginx, use the following command
```
nginx -s stop  ==> fast shutdown
nginx -s quit  ==> graceful shutdown
nginx -s reload ==> changing configuration, starting new worker processes 
                    with a new configuration, graceful shutdown of old worker processes
nginx -s reopen ==> reopening log files
```