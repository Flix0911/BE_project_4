#!/usr/bin/env bash

# exit when the command fails
set -o errexit

# Install dependencies
pip install -r requirements.txt

# Run migration
python manage.py migrate