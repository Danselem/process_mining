install-python:
	uv python install


init:
	uv init
	uv tool install black

install:
	uv venv
	. .venv/bin/activate
	# uv pip install --all-extras --requirement pyproject.toml
	# uv pip sync requirements.txt
	uv add -r requirements.txt

load:
	uv run src/load_data.py

readcsv:
	uv run src/readcsv.py

readxes:
	uv run src/readxes.py

filter:
	uv run src/filter.py

model:
	uv run src/model.py