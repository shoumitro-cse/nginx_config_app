FROM python:3.9 as base

FROM base as builder

ENV LANG en_GB.UTF-8 \
    LANGUAGE en_GB.UTF-8 \
    PYTHONUNBUFFERED=True \
    PYTHONIOENCODING=UTF-8

RUN apt-get update \
    && apt-get install --no-install-recommends --no-install-suggests -y \
    build-essential  \
    patch \
    git \
    wget \
    libssl-dev \
    libjwt-dev \
    libjansson-dev \
    libpcre3-dev \
    zlib1g-dev \
    && wget https://nginx.org/download/nginx-1.18.0.tar.gz \
    && tar -zxvf nginx-1.18.0.tar.gz \
    && git clone https://github.com/TeslaGov/ngx-http-auth-jwt-module \
    && cd nginx-1.18.0  \
    && ./configure --add-module=../ngx-http-auth-jwt-module \
    --with-http_ssl_module \
    --with-http_v2_module \
    --with-ld-opt="-L/usr/local/opt/openssl/lib" \
    --with-cc-opt="-I/usr/local/opt/openssl/include" \
    && make


FROM base

COPY --from=builder /nginx-1.18.0/objs/nginx /usr/sbin/nginx
COPY --from=builder /nginx-1.18.0/conf /usr/local/nginx/conf

ENV LANG en_GB.UTF-8 \
    LANGUAGE en_GB.UTF-8 \
    PYTHONUNBUFFERED=True \
    PYTHONIOENCODING=UTF-8

RUN apt-get update && \
    apt-get install --no-install-recommends --no-install-suggests -y \
    libssl-dev \
    libjwt-dev \
    libjansson-dev \
    libpcre3-dev \
    zlib1g-dev
