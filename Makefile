install:
	pip install --upgrade pip && pip install -r requirement.txt

format:
	black *.py

lint:
	ruff check *.py
	
test:
	python -m pytest --nbval -cov test.py 

all: install format lint test