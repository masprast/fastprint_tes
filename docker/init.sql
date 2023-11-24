-- CREATE ROLE backenduser WITH LOGIN PASSWORD 'backendpass';
CREATE USER backenduser;
CREATE DATABASE backendtes;
GRANT ALL PRIVILEGES ON DATABASE backendtes TO backenduser;