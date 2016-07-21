#!/bin/bash
pip install -r ./requirements.txt
git config --local user.email $1
crontab -l > mycron
CWD="$(pwd)"
echo "0 0 * * * python $CWD/spoofer.py" >> mycron
crontab mycron
rm mycron