# Volumes
`/ssl/`: This is a very important volume to store, as this is where the private key and public certificate is stored, so if this container ever gets removed completly from the system all clients will have to get a new certificate in order to work.