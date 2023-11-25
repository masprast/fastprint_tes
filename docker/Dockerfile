FROM postgres:16-alpine
COPY init.sql /docker-entrypoint-initdb.d/init.sql
# COPY init.sh /docker-entrypoint-initdb.d/init-user-db.sh
# ENV POSTGRES_DB=backendtes
# ENV POSTGRES_USER=postgresuser
ENV POSTGRES_PASSWORD=backendpass