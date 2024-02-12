# Backlog-Bandits

Travel Planner is a comprehensive travel planning system that empowers users to create customized itineraries with ease.It aims to be the ultimate travel planning companion, transforming trip planning from a chore into an exciting adventure.

Group Members:
- Anita Ershadi
- Dhruvi Rajeshlal Patel
- Khusboo Ketan Patel
- Sagar Hedaoo
- Saurabh Agrawal

## installation steps:
- install poetry here: https://python-poetry.org/docs/#installing-with-pipx
- run `poetry install`
- `poetry run pre-commit install`
- For formatting and linting run `poetry run pre-commit` before committing
- Recommended: install ide extensions – Mypy, black, flake8
- for starting server run 'poetry run start'
- `psql postgres` & `CREATE ROLE postgres WITH LOGIN SUPERUSER CREATEROLE CREATEDB REPLICATION BYPASSRLS PASSWORD postgres;`
- `CREATE DATABASE explorehub;`

## TablePlus Setup:
- for setting up the database: download: https://tableplus.com/download
- open table plus and click on '+'
- click on PostgreSQL
- Name: anything you want: example: ExploreHub
- User: "postgres"
- Password: "postgres"
- Host/Socket: "localhost"
- Database:"explorehub"
- Port: 5000

## API Documentation;
write in browser: 
http://localhost:8000/docs