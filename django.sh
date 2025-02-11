#!/bin/bash
echo "Creating Migrations..."
python manage.py makemigrations
echo ====================================

echo "Starting Migrations..."
python manage.py migrate
echo ====================================

# echo "collecting static"
# python manage.py collectstatic
# echo ====================================

echo "Starting Server..."
python manage.py runserver 0.0.0.0:8000