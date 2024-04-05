#!/usr/bin/bash
export DB_PATH="demodb.db"
export CONFIG_FILE="conf/appConfig.ini"
python -m flask --app src/app run --port 8080
