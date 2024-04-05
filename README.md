# python-rest-api

Use Python 3.12 or higher

To run locally:
`pip install -r local_requirements.txt`
`python -m flask --app src/app run --port 8080` or `./run.sh`

Unit checks can be executed by running pytest (e.g. `python -m pytest`) or `./test.sh`

If you aren't using the scripts you need to set `export CONFIG_FILE="conf/appConfig.ini"`

Note: it is not recommended to use Werkzeug in production, a production server such as gunicorn should be used.
However, gunicorn does not work in windows.

To build and run the docker image:
`docker build -t python-rest-api .`
`docker run --name python-rest-api -p 127.0.0.1:8080:8080 python-rest-api`