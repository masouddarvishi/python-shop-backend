
migrate:
	docker-compose run --rm app sh -c 'python manage.py makemigrations && python manage.py migrate'

