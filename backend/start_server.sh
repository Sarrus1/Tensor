#!/bin/bash

cd /home/server/tensor

echo "========= Migrate database"
python3 manage.py migrate --no-input
echo "========= DONE ============"

echo "========= Collect static files"
python3 manage.py collectstatic --no-input --clear
echo "========= DONE ============"

echo "========= Starting server ========="
/usr/local/bin/gunicorn Tensor.wsgi:application --log-level info --log-file=- --name tensor -b 0.0.0.0:8000 --reload