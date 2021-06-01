create-project:
	docker-compose run --rm app sh -c ' django-admin startproject config .'

start-app:
	docker-compose run --rm app sh -c 'python manage.py startapp ${name}'

migrate:
	docker-compose run --rm app sh -c 'python manage.py flush && python manage.py makemigrations && python manage.py migrate'

super-user:
	docker-compose run --rm app sh -c 'python manage.py createsuperuser'

test:
	docker-compose run --rm app sh -c 'python manage.py test ${name}'
