setup:
	python3 -m venv ~/.myrepo

install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	#python -m pytest test_gcli.py
	python -m pytest -vv --cov=gcli test_gcli.py
	#python -m pytest --nbval notebook.ipynb


lint:
	pylint --disable=R,C gcli.py hello-click.py

all: install lint test