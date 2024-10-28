.PHONY: install run clean all

all: install run clean

install:
	pip install -r requirements.txt

run:
	streamlit run main.py

clean:
	find . -type d -name "__pycache__" -exec rm -r {} +
	find . -type f -name "*.pyc" -delete
