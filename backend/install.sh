#!/bin/bash

python3 -m venv ./.venv 

./.venv/bin/pip install --upgrade setuptools
./.venv/bin/pip install Django
#./.venv/bin/pip install mod-wsgi

echo "To activate your shell's python venv, please run the following command (without quotes): 'source ./.venv/bin/activate'"
