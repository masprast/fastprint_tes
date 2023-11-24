FROM postgres:16-alpine
COPY init.sql /docker-entrypoint-initdb.d
ENV POSTGRES_DB=backendtes
ENV POSTGRES_USER=postgresuser
ENV POSTGRES_PASSWORD=password