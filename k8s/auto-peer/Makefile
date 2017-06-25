IMAGE = kairen/auto-peer

.PHONY: all init push

all: init push

init:
	@echo "Build image ..."
	docker build -t $(IMAGE) .

push:
	@echo "Push image ..."
	docker push $(IMAGE)
