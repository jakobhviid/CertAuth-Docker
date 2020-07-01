# About
A certificate authorith for the CFEI Kafka / Zookeeper stack. Please note this is only a proof of concept. It is not ready for production as it is extremly insecure. It signs everything it is given with question.
It provides a http rest endpoint for signing certificates.

TODO: Rewrite it in dotnet + security
TODO: Put https in front 

# Volumes
`/ssl/`: This is a very important volume to store, as this is where the private key and public certificate is stored, so if this container ever gets removed completly from the system all clients will have to get a new certificate in order to work.