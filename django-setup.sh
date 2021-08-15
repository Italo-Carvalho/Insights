#!/bin/bash -x

python manage.py migrate --noinput || exit 1
python manage.py migrate --database=teste --noinput || exit 1
python manage.py shell < default-setup.py
exec "$@"