#!/bin/cat

python3 -m venv ./.venv 
source ./.venv/bin/activate
pip install -r requirements.txt
./manage.py loaddata app/fixtures/defaults.json
