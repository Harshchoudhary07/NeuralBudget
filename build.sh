#!/usr/bin/env bash
# exit on error
set -o errexit

# Install Python dependencies
pip install --upgrade pip
pip install -r requirement.txt

# Run database migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --no-input
