# Alembic

```bash
# initialize
alembic init alembic

# create revision
alembic revision --autogenerate -m "generate from entities"
alembic upgrade head --sql > migration.sql

# check current
alembic current

# check history
alembic history --verbose
```