#!/bin/bash
#
# Docker container boot entrypoint script.
#

set -ex

export WS_SECRET=${WS_SECRET}

if [ -z ${WS_SECRET} ]; then
  echo "Pls, provide a web socket secret key"
  exit 1
fi

echo "Dashboard web socket secret : ${WS_SECRET}"

# Starting netstats server process
cd /ethstats
npm start
