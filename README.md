# changes-test

[![Build Status](https://secure.travis-ci.org/michaeljoseph/changes-test.png)](http://travis-ci.org/michaeljoseph/changes-test)
[![Stories in Ready](https://badge.waffle.io/michaeljoseph/changes-test.png?label=ready)](https://waffle.io/michaeljoseph/changes-test) [![pypi version](https://badge.fury.io/py/changes-test.png)](http://badge.fury.io/py/changes-test)
[![# of downloads](https://pypip.in/d/changes-test/badge.png)](https://crate.io/packages/changes-test?version=latest)
[![code coverage](https://coveralls.io/repos/michaeljoseph/changes-test/badge.png?branch=master)](https://coveralls.io/r/michaeljoseph/changes-test?branch=master)

## Overview

Testing changes start

* features
* and stuff 

## Usage

Install `changes-test`:

    pip install changes-test

Then execute the sample cli:

   changes-test

## Documentation

[API Documentation](http://changes-test.rtfd.org)

## Testing

Install development requirements:

    pip install -r requirements.txt

Tests can then be run with:

    nosetests

Lint the project with:

    flake8 changes-test tests

## API documentation

Generate the documentation with:

    cd docs && PYTHONPATH=.. make singlehtml

To monitor changes to Python files and execute flake8 and nosetests
automatically, execute the following from the root project directory:

    stir
