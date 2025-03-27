alias e := export

export:
    @poetry export -o requirements.txt --without-hashes

format:
    ruff format .; ruff check . --fix

lint:
    ruff check .; ruff check . --diff