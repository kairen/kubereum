#!/bin/bash
#
# Docker container boot entrypoint script.
#

set -ex

export CLUSTER_NUM="1"
export NAME_PREFIX=${NAME_PREFIX:-"ethereum"}
export WS_SERVER=${WS_SERVER:-"http://localhost:3000"}
export WS_SECRET=${WS_SECRET:-"admin"}
export RPC_HOST=${RPC_HOST:-"localhost"}
export RPC_PORT=${RPC_PORT:-"8545"}

echo "Number of clusters : ${CLUSTER_NUM}"
echo "Name prefix : ${NAME_PREFIX}"
echo "Dashboard web socket server : ${WS_SERVER}"
echo "Dashboard web socket secret : ${WS_SECRET}"
echo "RPC server host : ${RPC_HOST}"
echo "RPC server port : ${RPC_PORT}"

cd /ethnetintel
bash netstatconf.sh ${CLUSTER_NUM} \
                    ${NAME_PREFIX} \
                    ${WS_SERVER} \
                    ${WS_SECRET} \
                    ${RPC_HOST} \
                    ${RPC_PORT} > app.json

# Starting netstats server process
/usr/local/bin/pm2 start ./app.json
tail -f $HOME/.pm2/logs/${NAME_PREFIX}-out-0.log
