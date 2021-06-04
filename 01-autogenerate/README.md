# Alembic

```bash
# initialize
alembic init alembic

# create revision
alembic revision --autogenerate -m "Added user table"
alembic upgrade head

alembic revision --autogenerate -m "Added first and last names"
alembic upgrade head

# check current
alembic current

# check history
alembic history --verbose
```