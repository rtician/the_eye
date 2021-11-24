DOCKER_COMPOSE=docker-compose -f docker/docker-compose.yaml
APP=$(DOCKER_COMPOSE) run the-eye-app

build:
	$(DOCKER_COMPOSE) up --build

run:
	$(DOCKER_COMPOSE) up

create-migrations:
	$(APP) python3 manage.py makemigrations

run-migrations:
	$(APP) python3 manage.py migrate

tests:
	$(APP) pytest

clean-docker:
	$(DOCKER_COMPOSE) down -v
	docker rmi the-eye-image