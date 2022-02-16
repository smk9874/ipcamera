#!/bin/bash

python3 manage.py makemigrations ipcamera_for_baby
python3 manage.py sqlmigrate ipcamera_for_baby 0003
python3 manage.py migrate
