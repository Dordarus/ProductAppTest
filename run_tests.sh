#!/bin/bash

export FLASK_ENV='test'
nosetests --nologcapture --with-coverage --cover-package=app
unset FLASK_ENV