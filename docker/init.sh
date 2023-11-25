#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
	CREATE USER backenduser WITH PASSWORD 'backendpass';
	CREATE DATABASE backendtes;
	GRANT ALL PRIVILEGES ON DATABASE backendtes TO backenduser;
EOSQL