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
