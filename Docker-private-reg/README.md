
# Docker Private Registry with Authentication Security
* Authentication create super secure username & password using htpasswd by following steps
* mkdir -p ~/registry/auth -- htpasswd will creates the passwd file in this directory
* Pull the registry image from docker hub and use entry point to create the credentials and save in ~/registry/auth/htpasswd file
* docker run --entrypoint htpasswd  registry:2 -Bbn user passwd >~/registry/auth/htpasswd
* Check the credentials cat ~/registry/auth/htpasswd
* Create the certificates using openssl 
openssl req \
-newkey rsa:4096 -nodes -sha256 -keyout ~/registry/certs/domain.key \
-x509 -days 365 -out ~/registry/certs/domain.crt
* Now run container in background and mount these volumes to containers and also these files make sure container restart on when when docker daemon starts up
docker run -d -p 443:443 --restart=always --name registry \
-v ~/registry/certs/:/certs \
-v ~/registry/auth/:/auth \
-e REGISTRY_HTTP_ADDR=0.0.0.0:443 \
-e REGISTRY_HTTP_TLS_CERTIFICATE=/certs/domain.crt \
-e REGISTRY_HTTP_TLS_KEY=/certs/domain.key \
-e REGISTRY_AUTH=htpasswd \
-e "REGISTRY_AUTH_HTPASSWD_REALM=Registry Realm" \
-e REGISTRY_AUTH_HTPASSWD_PATH=/auth/htpasswd \
 registry:2
* On the client side copy the .crt certificate to the /etc/docker/certs.d/hostnme:port
* If incase our certificate not works perfectly then create the daemon.json in /etc/docker and add 
{
"insecure-registries": ["host-name:443"]
}
* Check the docker login from client docker login url:port 




