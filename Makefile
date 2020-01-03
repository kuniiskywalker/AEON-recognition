build:
	docker-compose build
.PHONY: build

up:
	docker-compose up -d --force-recreate
.PHONY: up

restart:
	docker-compose up -d --force-recreate
.PHONY: restart

logs:
	docker-compose logs
.PHONY: logs
