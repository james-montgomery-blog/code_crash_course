# Python

## History

Python is an interpreted, high-level, general-purpose programming language. Created by Guido van Rossum and first released in 1991, Python's design philosophy emphasizes code readability with its notable use of significant whitespace. Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects.

Python is very easy to pick up and can be very readable/maintainable if written with best practices in mind. Like other modern programming languages, Python also supports several programming paradigm. It supports object oriented and structured programming fully. Also, its language features support various concepts in functional and aspect-oriented programming. At the same time, Python also features a dynamic type system and automatic memory management. The programming paradigms and language features help you to use Python for developing large and complex software applications.

Python has a robust built in library and a vibrant community supporting it by creating new libraries to expand its functionality. Python can also be used as the glue between multiple other programming languages (part of python's original use!).

## Installation

You can simply install the Anaconda python distribution, the Pip package manager, and the Conda package manager together [Here](https://www.anaconda.com/download/#macos).

I recommend using conda virtual environments to manage dependancies for python projects. You can find a quick start guid [Here](../Environments/Conda/README.md).

## Hello World

```
python /HelloWorld/HelloWorld.py
```

## Import

The example code is uses static typing which is specific to python 3.

```
pip install -r ./Import/requirements.txt
```

```
python ./Import/main.py
```

## OLS

Install requirements:

```
pip install -r ./OLS/requirements.txt
```

Run the program:

```
python ./OLS/ols_example
```

Install test requirements:

```
pip install -r ./OLS/requirements_test.txt
```

Run tests:

```
cd OLS
nosetests --with-coverage --cover-package=ols_example
```

Run linter:

```
cd OLS
pylint ols_example --disable=invalid-name
```

Install library:

```
cd OLS
pip install .
```
