# pulling postgres image for the container on the etl pipeline

docker pull postgres:17

# creating the database
docker run --name test-postgres -e POSTGRES_PASSWORD=$PG_PASSWORD -e POSTGRES_USER=$PG_USER -e POSTGRES_DB=$PG_DB -p 5433:5432 -d postgres:17

#

#

#