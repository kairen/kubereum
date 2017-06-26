FROM httpd:2-alpine
MAINTAINER Kyle Bai <kyle.b@inwinstack.com>

RUN apk add --no-cache git g++ make bash python curl wget nodejs nodejs-npm && \
  git clone https://github.com/ethereum/browser-solidity /solidity && \
  cd /solidity && \
  npm install && \
  npm run prepublish && \
  npm cache clear && \
  mv ./* /usr/local/apache2/htdocs/ && \
  cd .. && rm -rf browser-solidity/ && \
  apk del --no-cache git g++ make python curl wget nodejs nodejs-npm && \
  rm -f /var/cache/apk/*

EXPOSE 80/tcp
