[![Build Status](https://travis-ci.org/kairen/kubereum.svg?branch=master)](https://travis-ci.org/kairen/kubereum)
# Kubernetes + Ethereum = Kubereum
This repos is containerize the Ethereum example. The goal is quickly setup a private Ethereum blockchain using Docker and Kubernetes.

Support Feature:
* Private network chain.
* Miner monitoring.
* Blockchain stats dashboard.
* Solidity browser service.

Example in my Lab:
[![asciicast](https://asciinema.org/a/lRWNbs4bQmmS6ijQcyjdLqvsS.png)](https://asciinema.org/a/lRWNbs4bQmmS6ijQcyjdLqvsS?speed=2)

### Image build status

| Solidity | Ethnetintel | Ethstats | Auto peer |
|----------|-------------|----------|-----------|
|[![Docker Build Statu](https://img.shields.io/docker/build/kairen/solidity.svg)](https://hub.docker.com/r/kairen/solidity/)|[![Docker Build Statu](https://img.shields.io/docker/build/kairen/ethnetintel.svg)](https://hub.docker.com/r/kairen/ethnetintel/)|[![Docker Build Statu](https://img.shields.io/docker/build/kairen/ethstats.svg)](https://hub.docker.com/r/kairen/ethstats/)|[![Docker Build Statu](https://img.shields.io/docker/build/kairen/auto-peer.svg)](https://hub.docker.com/r/kairen/auto-peer/)|

### Requirements
* Docker engine.
* Kubernetes cluster.

## Usage
To run the Ethereum private chain cluster(without the Ethereum network status):
```sh
$ kubectl apply \
-f geth-config.yml \
-f geth-svc.yml \
-f geth-ds.yml
```

Check the pods:
```sh
$  kubectl get po,svc -o wide
NAME            READY     STATUS    RESTARTS   AGE       IP            NODE
po/geth-289mg   2/2       Running   0          10m       10.244.52.3   node4
po/geth-fqszz   2/2       Running   0          10m       10.244.96.2   node1
po/geth-hxlf2   2/2       Running   0          10m       10.244.85.4   node3
po/geth-vjtpf   2/2       Running   0          10m       10.244.98.3   node2

NAME             CLUSTER-IP        EXTERNAL-IP   PORT(S)    AGE       SELECTOR
svc/geth         192.168.170.219   <none>        8545/TCP   4h        app=geth
```

Attach the Ethereum IPC file(Install geth from [Building-Ethereum](https://github.com/ethereum/go-ethereum/wiki/Building-Ethereum)):
```sh
$ cd /var/geth && ls
geth  geth.ipc  keystore

$ geth attach ipc:geth.ipc
Welcome to the Geth JavaScript console!

instance: Geth/v1.6.7-unstable/linux-amd64/go1.7.3
coinbase: 0x2f99300b9fb9da018e7004e448f0a16730dbe6a4
at block: 0 (Thu, 01 Jan 1970 00:00:00 UTC)
 datadir: /var/geth
 modules: admin:1.0 debug:1.0 eth:1.0 miner:1.0 net:1.0 personal:1.0 rpc:1.0 txpool:1.0 web3:1.0

> net.peerCount
3
```
