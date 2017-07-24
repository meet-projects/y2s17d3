#!/bin/bash

cd ~/
if [[ -e y2-venv ]]; then
    source ~/y2-venv/bin/activate
else
     sudo apt-get install virtualenv
     virtualenv -p $(which python3) y2-venv
     source ~/y2-venv/bin/activate
     pip install -r requirements.txt
fi
