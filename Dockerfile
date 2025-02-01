# Stage 1
FROM python:3.10-alpine AS builder

RUN mkdir /app

WORKDIR /app

COPY requirements.txt .

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN pip install --upgrade pip
COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

# Stage 2
FROM python:3.10-alpine
# RUN useradd -m -r backend && \
#     mkdir /app & \
#     chown -R backend /app
RUN mkdir /app

COPY --from=builder /usr/local/lib/python3.10/site-packages/ /usr/local/lib/python3.10
COPY --from=builder /usr/local/bin /usr/local/bin

WORKDIR /app
COPY --chown=backend:backend . .

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

USER backend

EXPOSE 8000
ENTRYPOINT ["/app/django.sh"]