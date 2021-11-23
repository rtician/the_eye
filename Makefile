run:
	docker-compose -f docker/docker-compose.yaml up

create-migrations:
	docker-compose run the-eye-app python3 manage.py makemigrations

run-migrations:
	docker-compose run the-eye-app python3 manage.py migrate
