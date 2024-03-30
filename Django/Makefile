run:
	docker-compose up -d --build

stop:
	docker-compose down

test:
	python -m coverage run -m pytest .

report:
	coverage run -m

pre-commit:
	pre-commit run --all-files
