.PHONY: help

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

install-dev-deps:
	pipenv install --dev

codestyle:
	pipenv run pycodestyle .

unit:
	pipenv run python -m pytest

behave:
	pipenv run behave

test: install-dev-deps codestyle unit behave
