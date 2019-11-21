clean:
	@find . -name "*.pyc" -exec rm -rf {} \;
	@find . -name "__pycache__" -delete

migrate:
	@python manage.py migrate

makemigrations:
	@python manage.py makemigrations

run:
	@python manage.py runserver

shell:
	@python manage.py shell
