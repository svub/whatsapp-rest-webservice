#!/bin/bash
pip install virtualenv
virtualenv --no-site-packages --distribute env && source env/bin/activate && pip install -r
python manage.py migrate