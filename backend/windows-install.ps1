python -m venv './.venv'
./.venv/scripts/activate
pip install -r windows-requirements.txt
./manage.py loaddata app/fixtures/defaults.json
