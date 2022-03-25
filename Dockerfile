FROM alpine:latest

RUN add-apt-repository ppa:openjdk-r/ppa && \
    apt-get update && \
    apt-get install -y openjdk-7-jdk && \
    apt-get install -y ant && \
    apt-get clean;

RUN apk add --no-cache bash libxml2-utils