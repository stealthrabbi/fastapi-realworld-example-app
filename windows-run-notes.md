set env:
```
DB_CONNECTION=postgresql://postgres:postgres@localhost:5432/postgres
SECRET_KEY=7881f0a3a3b13ecd781eb58981628dce56c50fac65c4454badd11af1e72cc556
POSTGRES_HOST=db
DEBUG=True
```

Run postgres container:
 `docker-compose up db`


another terminal

`poetry shell`

`uvicorn app.main:app --reload`


navigate to http://localhost:8000/docs



##where are DB models?
-`app/db/queries/tables.py`



## create migration

1. Add table / entity to tables.py
