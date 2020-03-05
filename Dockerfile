FROM ubuntu:18.04

RUN apt update && \
    apt install -y openssl python3 python3-pip && \
    openssl rand -out /root/.rnd -hex 256 && \
    mkdir /ssl && \
    openssl req -new -newkey rsa:4096 -days 365 -x509 -subj "/CN=CFEI-DOCKER-CA" -keyout /ssl/ca-key -out /ssl/ca-cert -nodes

# TODO - remove this, this is just for testing purposes
RUN apt install -y --no-install-recommends openjdk-11-jre-headless

# Copy necessary scripts
COPY scripts /tmp/
RUN chmod +x /tmp/*.sh && \
    mv /tmp/* /usr/bin && \
    rm -rf /tmp/*

COPY cert-api/* /cert-server/

# configuring required packages and directories for server
RUN pip3 install flask Werkzeug && \
    mkdir /ssl/certificates_uploads && mkdir /ssl/signed_certificates

WORKDIR /ssl

# TODO: figure out volumes, perhaps the certificate key and certification itself ?

CMD [ "docker-entrypoint.sh" ]