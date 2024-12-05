.PHONY: run-bash run-python run-go build

run-bash:
	docker-compose run --rm -e DAY=$(DAY) bash

run-python:
	docker-compose run --rm -e DAY=$(DAY) python

run-go:
	docker-compose run --rm -e DAY=$(DAY) go

build:
	docker-compose up --build

default: run-bash