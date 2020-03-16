#!/bin/bash

if ! [[ -f "/ssl/ca-cert" && -f "/ssl/ca-key" ]]; then
    echo "INFO - Creating a new certificate and private key"
    openssl req -new -newkey rsa:4096 -days 365 -x509 -subj "/CN=Cfei-Docker-CA" -keyout /ssl/ca-key -out /ssl/ca-cert -nodes
    echo "INFO - Certificate and private key created at /ssl"
else
    echo "INFO - Certificate and private key already exists. Using those"
fi

python3 /cert-server/main.py
