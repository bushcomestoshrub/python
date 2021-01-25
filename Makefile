
init:
	pip install -r requirements.txt

run:
	python src/application.py

test:
	nosetests tests