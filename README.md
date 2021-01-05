# Data Structures and Algorithms practice
Practicing data structure and algorithms, mostly in python for now

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## Environment setup
### Recommended - using poetry and pyenv
  - Install [poetry](https://github.com/python-poetry/poetry)
  - Setup python virtual environment using [pyenv](https://github.com/pyenv/pyenv) for python 3.7.9 (refer pyproject.toml for exact version)
  - Activate the virtual environment
  - run `poetry install`
### Alternate - use your favorite virtual environment
  * use the requirements.txt which was generated from poetry in your favorite environment

## Tests and code coverage
  * run `python -m pytest` at root torun all tests
  * run `coverage run -m pyest` at the root of project to generate coverage
  * run `coverage report` to see coverage
  * run `coverage html` to generate a detailed html report that shows line coverage

## Learning Resources
  * [Dynamic Programming course - freecodecamp](https://youtu.be/oBt53YbR9Kk)
  * [Coursera - Algorithms Part1](https://www.coursera.org/learn/algorithms-part1/home/welcome)
  * [coderbyte - Algorithm in one week](https://coderbyte.com/starter-course/algorithms-and-data-structures)
