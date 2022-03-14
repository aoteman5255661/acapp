FROM python:alpine

WORKDIR /root
COPY . /root/acapp/.
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.ustc.edu.cn/g' /etc/apk/repositories


RUN apk update && apk upgrade

RUN apk add openrc --no-cache

RUN apk add wget gcc g++ make
RUN apk add supervisor
RUN apk add nginx
RUN nginx -t
RUN rc-update add nginx default
RUN rc-update add supervisord default
EXPOSE 80






CMD ["nginx", "-g", "daemon off;"]
