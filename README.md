# Python REST API

A simple CRUD API using sqlite for the backend. It also demonstrates JWT creation and 
verification and usage of 3rd party APIs. See the swagger for details.

Use Python 3.12 or higher

### To run locally:
* `pip install -r local_requirements.txt`
* `python -m flask --app src/app run --port 8080` or `./run.sh`

Unit checks can be executed by running pytest (e.g. `python -m pytest`) or `./test.sh`

If you aren't using the scripts you need to set `export CONFIG_FILE="conf/appConfig.ini"`

Note: it is not recommended to use Werkzeug in production, a production server such as gunicorn should be used.

However, gunicorn does not work in windows.

To build and run the docker image:
* `docker build -t python-rest-api .`
* `docker run --name python-rest-api -p 127.0.0.1:8080:8080 python-rest-api`

If you have helm and kubernetes setup locally:

To set up a registry and push the image:

* `docker run -d -p 5000:5000 --restart=always --name registry registry:2`
* `docker build -t localhost:5000/python-rest-api .`
* `docker push localhost:5000/python-rest-api`

Install:
`helm install python-rest-api-chart rest-api/ --values rest-api/values.yaml`

Run `./podforward.sh` if you want to be able to use localhost:8080 to reach it.

#### Swagger
YAML is in `swagger/swagger_server/swagger`.
Best way to view swagger is to build the docker image as specified in the README.md in the `swagger` directory.
You can then use `http://localhost:8080/ui/`

## Contributing
Feel free to open a pull request if you have a suggestion.