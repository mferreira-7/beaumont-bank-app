# beaumont-bank

Fictional mini bank built with Python, FastAPI, PostgreSQL and React. Double-entry ledger, idempotent transfers, concurrency-safe. Fake data only.

**Status:** In progress (setting up the API and database)

**Live demo:** [beaumont-bank-app](https://beaumont-bank-app.onrender.com/)

## Tech stack

Python, FastAPI, SQLAlchemy, PostgreSQL (Neon), React

## Run locally

Requires Python 3.14 and a PostgreSQL database (for example a free Neon project).

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Create a `.env` file in the project root:

```
DATABASE_URL=your-postgres-connection-string
```

Start the dev server:

```bash
fastapi dev app/main.py
```

Then open `/health`, `/health/db` and `/docs`.

## Note

This is a fictional bank for portfolio purposes. All data is fake, and no real banking or card data is used.
