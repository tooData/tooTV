SHELL := /bin/bash
.SHELLFLAGS = -ec
.ONESHELL:
.SILENT:

.EXPORT_ALL_VARIABLES:
REPO_DIRECTORY:=$(shell pwd)
PYTHONPATH:=${PYTHONPATH}:${REPO_DIRECTORY}

.PHONY: help
help:
	echo "❓ Utiliser \`make <target>' où <target> peut être"
	grep -E '^\.PHONY: [a-zA-Z0-9_-]+ .*?## .*$$' $(MAKEFILE_LIST) | \
		awk 'BEGIN {FS = "(: |##)"}; {printf "\033[36m%-30s\033[0m %s\n", $$2, $$3}'

.PHONY: venv  ## 🐍 créé l'environnement de travail
venv:
	virtualenv -p python3.8 venv
	echo "venv" >> .gitignore

.PHONY: dependencies  ## ⏬ installe les dépendances de production
dependencies:
	venv/bin/pip install -r requirements.txt

.PHONY: prepare_sqlite  ## ⏬ crée la base de donnée de travail sqlite
prepare_sqlite:
	venv/bin/python create_db.py