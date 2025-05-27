.PHONY: up down shell run migrate logs worker beat ps

# Start containers in detached mode and rebuild images
up:
	docker-compose up -d --build

# Stop and remove containers
down:
	docker-compose down

# Open a bash shell inside the Django container
shell:
	docker exec -it $(shell docker-compose ps -q app) bash

# Run Django development server
run:
	docker-compose exec app python manage.py runserver 0.0.0.0:8000

# Run Django migrations
migrate:
	docker-compose exec app python manage.py migrate

# Tail logs for all containers
logs:
	docker-compose logs -f

# Run Celery worker
worker:
	docker-compose exec app celery -A app worker --loglevel=info

# Run Celery beat scheduler
beat:
	docker-compose exec app celery -A app beat --loglevel=info

# Show container status
ps:
	docker-compose ps
