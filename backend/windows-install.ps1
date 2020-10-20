python3 -m venv './.venv'
source ./.venv/scripts/activate
pip install -r windows-requirements.txt
./manage.py loaddata app/fixtures/defaults.json
