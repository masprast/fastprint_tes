# Stage 1
FROM python:3.10-alpine AS builder

RUN mkdir /app

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# RUN pip install --upgrade pip
COPY requirements.txt /app/
RUN apk update && apk upgrade
RUN apk add --no-cache build-base python3-dev libpq postgresql-libs \
    gcc musl-dev postgresql-dev libpq-dev

RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install --no-cache-dir -r requirements.txt

# Stage 2
FROM python:3.10-alpine

RUN addgroup -S backendgroup && adduser -S backend -G backendgroup && \
    mkdir /app && \
    chown -R backend /app

RUN apk add libpq-dev

USER backend

COPY --from=builder /usr/local/lib/python3.10 /usr/local/lib/python3.10
COPY --from=builder /usr/local/bin /usr/local/bin
RUN ls -d /usr/lib/python3.10

ENV PYTHONPATH /usr/lib/python3.10/site-packages
WORKDIR /app
COPY --chown=backend:backendgroup . .

RUN chmod +x django.sh
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1


EXPOSE 8000

ENTRYPOINT ["sh","./django.sh"]