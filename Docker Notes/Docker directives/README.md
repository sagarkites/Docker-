# Dockerfile directives
* **FROM**       Base image
* MAINTAINER Mail of owner
* RUN        Commands to be executed as a part of building image as Layers
* USER       Create Image as non-privileged user & all RUN layer above user or else you will get privileges issues
* ADD        Addes the files to the Images
* COPY       Copies the files to the Image
* WORKDIR    Change directory
* ENV        Creates environment variables
* CMD        Executes the when container build does not creates the Layers & can be overridden with docker exce
* ENTRYPOINT Default Application cannot be overridden docker exec
* EXPOSE     Ports should be gets out of the container

