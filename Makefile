clean_pycache:
	find . -type d -name __pycache__ -exec rm -r {} \+

migrate_db:
	venv/bin/python manage.py makemigrations
	venv/bin/python manage.py migrate	

restart_db:
	rm db.sqlite3
	make migrate_db
	venv/bin/python manage.py createsuperuser

run:
	venv/bin/python manage.py runserver 0.0.0.0:8000

create-venv:
	python3 -m venv venv

install-requirements:
	venv/bin/python3 -m pip install --upgrade pip
	venv/bin/pip install -r requirements.txt
