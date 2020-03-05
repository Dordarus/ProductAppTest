# Product List API

## Usage
- [Running the application](#starting-the-application)
- [Setup Database](#setup-database)
- [API Documentation](#api-documentation)
- [Running tests with coverage](#running-tests-with-coverage)
- [Docker container](#docker-container)


## Starting the application
In order to run the application set the environment
variable below.
```
export FLASK_ENV=development
```
Then run the command below to start the application.
```
flask run
```

## Setup Database

### Init database
```
flask db init
```
### Create migrations
```
flask db migrate
```
### Apply the migration
```
flask db upgrade
```
### Seed database
Seed with `test.json` data
```
flask seed run
```

## API Documentation

The api documentation is hosted as the
```
/apidocs
```

## Running tests with coverage
It set `FLASK_ENV` to `test`

You can also run tests with coverage in root of project by running this command in the terminal
```
sh run_tests.sh
```

## Docker container

### Build Docker image
```
make build
```
### Run the container
It set `FLASK_ENV` to `production`
```
make run
```
### Stop container
```
make stop
```