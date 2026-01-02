# Base Image
FROM ubuntu

RUN apt update && apt install -y curl
RUN curl -sL https://deb.nodesource.com/setup_22.x -o /tmp/nodesource_setup.sh
RUN bash /tmp/nodesource_setup.sh
RUN apt install -y nodejs

# Copying the source code to docker image
COPY server.js /home/app/server.js
COPY package-lock.json /home/app/package-lock.json
COPY package.json /home/app/package.json
WORKDIR /home/app/
RUN npm install