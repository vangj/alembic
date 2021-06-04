# Alembic

```bash
# install
pip install alembic

# initialize
alembic init alembic

# create revision
alembic revision -m "create user table"
alembic revision -m "add columns"

# check current
alembic current

# to upgrade
alembic upgrade head

# to downgrade to nothing
alembic downgrade base

# check history
alembic history --verbose
```