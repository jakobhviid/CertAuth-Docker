FROM ubuntu:18.04

RUN apt update && \
    apt install -y openssl python3 python3-pip && \
    openssl rand -out /root/.rnd -hex 256 && \
    mkdir /ssl

# Copy necessary scripts
COPY scripts /tmp/
RUN chmod +x /tmp/*.sh && \
    mv /tmp/* /usr/bin && \
    rm -rf /tmp/*

COPY cert-api/* /cert-server/

# configuring required packages and directories for server
RUN pip3 install flask Werkzeug && \
    mkdir /certificates_uploads && mkdir /signed_certificates

WORKDIR /ssl

VOLUME [ "/ssl" ]

CMD [ "docker-entrypoint.sh" ]