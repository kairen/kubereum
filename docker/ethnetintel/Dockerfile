FROM node:6-alpine
MAINTAINER Kyle Bai <kyle.b@inwinstack.com>

RUN apk add --no-cache git g++ make bash && \
  git clone https://github.com/cubedro/eth-net-intelligence-api /ethnetintel && \
  cd /ethnetintel && \
  npm install && \
  npm install -g pm2 && \
  npm cache clear && \
  apk del --no-cache git make g++  && \
  rm -f /var/cache/apk/* && \
  npm cache clear

COPY scripts/netstatconf.sh /ethnetintel
COPY scripts/entrypoint.sh /usr/local/bin/

WORKDIR /ethnetintel
EXPOSE 3000 3001

ENTRYPOINT ["entrypoint.sh"]
