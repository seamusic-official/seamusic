install:
	pip install -r requirements/dev.txt

build:
	docker-compose -f docker-compose.$(for).yml build

start:
	docker-compose -f docker-compose.$(for).yml up --force-recreate --remove-orphans

up:
	docker-compose -f docker-compose.$(for).yml up --force-recreate --remove-orphans -d

stop:
	docker-compose stop

rm:
	docker-compose rm
	rm -rf db/

test:
	docker-compose -f docker-compose.test.yml up --force-recreate -remove-orphans -d
	python -m alembic upgrade head
	python -m pytest
	docker-compose stop

lint:
	python -m flake8
	python -m mypy -p src
