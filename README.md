# Data Structures and Algorithms practice
Practicing data structure and algorithms, mostly in python for now

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![CodeFactor](https://www.codefactor.io/repository/github/amolgawai/data_struct_and_algo/badge)](https://www.codefactor.io/repository/github/amolgawai/data_struct_and_algo)
[![pytest](https://github.com/amolgawai/data_struct_and_algo/workflows/Python%20test/badge.svg)](https://github.com/amolgawai/data_struct_and_algo/actions)
![](./coverage.svg)

## Environment setup
### Recommended - using poetry and pyenv
  - Install [poetry](https://github.com/python-poetry/poetry)
  - Setup python virtual environment using [pyenv](https://github.com/pyenv/pyenv) for python 3.7.9 (refer pyproject.toml for exact version)
  - Activate the virtual environment
  - run `poetry install`
### Alternate - use your favorite virtual environment
  * use the requirements.txt which was generated from poetry in your favorite environment
  * use the requirements-dev.txt for adding testing and other development tools

## Tests and code coverage
  * run `python -m pytest` at root tor un all tests
  * run `pytest --cov` at root to run all tests and get coverage
  * run `coverage run -m pyest` at the root of project to generate coverage
  * run `coverage report` to see coverage
  * run `coverage html` to generate a detailed html report that shows line coverage
  * run `ptw --runner "pytest --picked --testmon"` to watch for changes and run respective tests

## Learning Resources
  * [Dynamic Programming course - freecodecamp](https://youtu.be/oBt53YbR9Kk)
  * [Coursera - Algorithms Part1](https://www.coursera.org/learn/algorithms-part1/home/welcome)
  * [William Fiset - You Tube Data Structures Playlist](https://www.youtube.com/playlist?list=PLDV1Zeh2NRsB6SWUrDFW2RmDotAfPbeHu)
  * [coderbyte - Algorithm in one week](https://coderbyte.com/starter-course/algorithms-and-data-structures)
  * [Leetcode study guide](https://leetcode.com/discuss/general-discussion/494279/comprehensive-data-structure-and-algorithm-study-guide) -> find in pdf form [here](./references/CI_DSA_study_guide.pdf)
  * [Grokking Algorithms - Book](https://www.manning.com/books/grokking-algorithms)
