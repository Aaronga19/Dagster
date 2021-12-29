from database.settings import settings

environment_vars_schedule = {
    'DAGSTER_PG_USERNAME': settings.dagster_pg_username,
    'DAGSTER_PG_PASSWORD': settings.dagster_pg_password,
    'DAGSTER_PG_HOST': settings.dagster_pg_host,
    'DAGSTER_PG_DB': settings.dagster_pg_db,
    'DAGSTER_PG_PORT': settings.dagster_pg_port,
}