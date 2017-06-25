GETH_IMAGE = ethereum/client-go
DATA_DIR = genesis-data
NETWORK_ID = 15

.PHONY: all init run logs console clean rm

all: init

init:
	@echo "Init genesis block ..."
	mkdir -p $(DATA_DIR)
	cp genesis.json $(DATA_DIR)
	docker run \
	    -it --rm \
	    -v $(PWD)/$(DATA_DIR):/$(DATA_DIR) \
			--name geth-init \
			ethereum/client-go init \
			--datadir=/$(DATA_DIR) /$(DATA_DIR)/genesis.json

run_node:
	@echo "Run node ..."
	docker run \
	    -d \
	    -p 8545:8545 \
	    -p 30303:30303  \
	    -v $(PWD)/$(DATA_DIR):/$(DATA_DIR) \
	    --name geth-01 \
	    ethereum/client-go \
	    --datadir=/$(DATA_DIR) \
      --networkid=$(NETWORK_ID) \
	    --rpc \
			--rpcaddr=0.0.0.0 \
	    --rpcapi=admin,db,eth,debug,miner,net,shh,txpool,personal,web3 \
	    --rpccorsdomain=*

console:
	@echo "Login to console ..."
	docker exec -ti geth-01 geth attach ipc:/$(DATA_DIR)/geth.ipc

logs:
	@echo "Logging container ..."
	docker logs -f geth-01

clean:
	@echo "Clean all container ..."
	docker stop geth-01 && docker rm geth-01

rm:
	@echo "Remove genesis data ..."
	rm -rf $(DATA_DIR)
