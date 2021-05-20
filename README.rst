
===========
FLASK Etude
===========

This repository is my personal interpretation of
`Flask Rest API - Zero to Yoda Series' Articles <https://dev.to/paurakhsharma/series/3672>`__

Requisites
----------

In order to install (and execute) this repository, you require:

* `Anaconda <https://www.anaconda.com/products/individual>`__
* `Poetry <https://python-poetry.org/>`__
* `Docker <https://www.docker.com/>`__ and `Docker Compose <https://docs.docker.com/compose/>`__

Install
-------

Start a MongoDB instance
~~~~~~~~~~~~~~~~~~~~~~~~

Create an ``.env`` file in this project directory in which define those variables::

  MONGODB_ROOT_USER=root
  MONGODB_ROOT_PASS=<password>
  MONGOEXPRESS_USER=flask
  MONGOEXPRESS_PASS=<password>
  APP_USER=flask
  APP_PASS=<password>
  JWT_SECRET_KEY=<secret key>

Next start *MongoDB* using ``docker-compose``::

  $ docker-compose up -d

In order to connect to your local *MongoDB* docker instance and create user::

  $ docker-compose run --rm --user mongodb mongo sh -c 'mongo --host mongo --username="${MONGO_INITDB_ROOT_USERNAME}" --password="${MONGO_INITDB_ROOT_PASSWORD}"'

Create a user for ``movie-bag`` database with ``readWrite`` permissions::

  use admin
  db.createUser({user: "flask", pwd: "<password>", roles: [{role: "readWrite", db: "movie-bag"}]})

Install python requirements
~~~~~~~~~~~~~~~~~~~~~~~~~~~

You need to install required packages in a new conda environment::

  $ conda env create -f environment.yml
  $ conda activate FLASKetude
  $ poetry install
