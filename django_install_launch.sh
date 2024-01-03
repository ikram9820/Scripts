#!/bin/bash -ex

sudo yum -y install python3-pip
wget https://github.com/ikram9820/bookishpdf/archive/main.zip
unzip main.zip
cd  bookishpdf-main
pip3 install -r requirements.txt

export DJANGO_SETTINGS_MODULE='config.settings.prod'
export DJANGO_ALLOWED_HOSTS='*'
export SECRET_KEY=')xz#jeu93f63q0_m(ns_(0&w3^f-mah#z6g10$r3923+5mmj@l'

export DB_HOST=db-bookishpdf.crm2ysiw004h.ap-south-1.rds.amazonaws.com
export DB_USER='postgres'
export DB_PASSWORD=VduN8uKqEbF1XXSMhKNf
export DB_NAME=db_bookishpdf

export AWS_ACCESS_KEY_ID=''
export AWS_SECRET_ACCESS_KEY=''

python3 manage.py migrate
gunicorn -b 0.0.0.0:8000 config.wsgi