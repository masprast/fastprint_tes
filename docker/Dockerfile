FROM postgres:16-alpine
COPY init.sql /docker-entrypoint-initdb.d/init.sql
ENV POSTGRES_PASSWORD=backendpass