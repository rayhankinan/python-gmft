install:
	poetry install

download-model:
	poetry run python ./src/download.py

run:
	poetry run streamlit run ./src/app.py