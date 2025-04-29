FROM python:3.10-slim

# 安装编译器、基本依赖
RUN apt-get update && apt-get install -y \
    gcc \
    make \
    wget \
    nginx \
    && rm -rf /var/lib/apt/lists/*

# 手动安装 OpenSSL 1.0.1
WORKDIR /tmp
RUN wget http://www.openssl.org/source/openssl-1.0.1c.tar.gz && \
    tar -zxvf openssl-1.0.1c.tar.gz && \
    cd openssl-1.0.1c && \
    rm -rf /usr/bin/pod2man && \
    ./config && \
    make && make install

# 把老openssl加到PATH
ENV PATH="/usr/local/ssl/bin:$PATH"
ENV LD_LIBRARY_PATH="/usr/local/ssl/lib"

# 验证一下版本
RUN openssl version  # 应该显示 OpenSSL 1.0.1

# 安装 Python 依赖
COPY requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt

# 设置工作目录
WORKDIR /app

# 复制应用代码
COPY app.py secret.py /app/

# 自签名证书（如果没有）
RUN mkdir -p /etc/ssl/private /etc/ssl/certs && \
    openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
    -subj "/C=US/ST=CTF/L=CTF/O=CTF/OU=CTF/CN=localhost" \
    -keyout /etc/ssl/private/server.key \
    -out /etc/ssl/certs/server.crt

# 复制nginx配置
COPY nginx.conf /etc/nginx/nginx.conf

# 删除默认站点配置
RUN rm -f /etc/nginx/sites-enabled/default

# 开放443端口
EXPOSE 443

# 启动脚本
CMD python app.py & nginx -g "daemon off;"

