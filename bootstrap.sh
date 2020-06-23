#!/bin/bash
if [ ! -d "env" ]; then
  read  -p "Virtual Environment not created, do you want to create it (y/n)?: " follow
    if [ "$follow" == "y" ]
    then
        pip3 install virtualenv
        virtualenv -p python3 env
        source env/bin/activate
        echo "Installing python libraries..."
        pip3 install --no-cache-dir -r ./requirements.txt
    fi
else
  source env/bin/activate
fi

export APP_SETTINGS="config.DevelopmentConfig"
redis-cli shutdown

mongo &
redis-server &
celery -A src.celery worker --loglevel=info &
python app.py