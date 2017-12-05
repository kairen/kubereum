# encode=utf-8
# Copyright 2017 Kyle Bai(kyle.b@inwinstack.com)
# All Rights Reserved

import os
import sys
import json
import requests

SA_PATH = '/var/run/secrets/kubernetes.io/serviceaccount'

class EthereumNode():
    """
    Get the ethereum nodes from Kubernetes.
    """
    def __init__(self):
        host = os.environ.get('KUBERNETES_PORT_443_TCP_ADDR', "192.160.0.1")
        port = os.environ.get('KUBERNETES_SERVICE_PORT_HTTPS', "443")
        namespace = os.environ.get('POD_NAMESPACE', "default")
        svc_name = os.environ.get('SERVICE_NAME')

        with open("{}/token".format(SA_PATH), 'r') as f:
            self.token = f.read()

        self.pod_name = os.environ.get('POD_NAME')
        self.url = "https://{}:{}/api/v1/namespaces/{}/endpoints/{}".format(
            host, port, namespace, svc_name,
        )

    def discover(self):
        try:
            headers = {"Authorization": "Bearer {}".format(self.token)}
            response = requests.get(self.url, headers=headers, verify=False)

            addrs = []
            nodes = {}
            for subnet in response.json()['subsets']:
                for addr in subnet['addresses']:
                    if addr['targetRef']['name'] != self.pod_name:
                        addrs.append(addr['ip'])
                    else:
                        nodes.update({"master": addr['ip']})
                nodes.update({"nodes": addrs})
            return nodes
        except Exception as e:
            print(e)

class EthereumPeer():
    """
    Add the ethereum nodes peer.
    """
    def __init__(self, nodes):
        self.nodes = nodes
        self.id = 1
        self.port = 8545

    def __payload(self, method, params):
        return json.dumps({
            "jsonrpc": "2.0",
            "method": method,
            "params": params,
            "id": self.id
        })

    def encodes(self):
        try:
            encodes = []
            headers = {'Content-Type': 'application/json'}
            payload = self.__payload("admin_nodeInfo", [])
            for host in self.nodes['nodes']:
                url = "http://{}:{}".format(host, self.port)
                response = requests.post(url, headers=headers, data=payload)
                encodes.append(response.json()['result']['enode'].replace('[::]', host))
            return encodes
        except Exception as e:
            print(e)

    def connectivity(self, encodes):
        try:
            headers = {'Content-Type': 'application/json'}
            url = "http://{}:{}".format(self.nodes['master'], self.port)
            for ec in encodes:
                payload = self.__payload("admin_addPeer", [ec])
                response = requests.post(url, headers=headers, data=payload)
                print(response.json())
        except Exception as e:
            print(e)


def main():
    node = EthereumNode()
    peer = EthereumPeer(node.discover())
    peer.connectivity(peer.encodes())


if __name__ == '__main__':
    main()
