# Product List API

## Usage
- [Running the application](#starting-the-application)
- [Setup Database](#setup-database)
- [API Documentation](#api-documentation)
- [Running tests with coverage](#running-tests-with-coverage)
<!-- - [Live Application](#live-application) -->


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

<!-- ## Live Application
This API is hosted [here](http://kbucket-api.herokuapp.com) on [heroku](heroku.com) -->

## API Documentation

The api documentation is hosted as the
```
/apidocs
```

## Running tests with coverage
You can also run tests with coverage in root of project by running this command in the terminal
```
sh run_tests.sh
```