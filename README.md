# Code Sandbox

This repository is full of very simple sample code that I originally wrote as I was learning various coding languages. This is not meant as a tutorial for learning how to use these languages, but I hope this simple code is helpful for someone looking for stripped down simple examples of how to get started in these languages. I sometimes use this repository as a reference for getting new software engineering (SE) and machine learning engineering (MLE) teammates up to speed on whatever language a particular project is built in.

<!-- TOC -->

Table of Contents
- [Code Sandbox](#code-sandbox)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Tutorials](#tutorials)
- [Environments](#environments)
- [License](#license)

<!-- /TOC -->

## Getting Started

These instructions will help you get this code up and running on your local development environment.

### Prerequisites

For these languages you will need the necessary package for running the code. For compiled languages you will also need the appropriate [compiler](https://en.wikipedia.org/wiki/Compiler). Below is a list of the languages, package managers, and IDEs. Installation guides are included with the example code for each [language](#languages), with the exception of Homebrew and the IDEs. Homebrew installation is covered in the [installation](#installation) section. For IDE installation simply follow the IDE links below and follow the installation instructions. I strongly recommend using the IDEs for anyone contemplating seriously using these languages for production grade code.

*Languages*
* [C](https://en.wikipedia.org/wiki/C_(programming_language))
* [C++](https://en.wikipedia.org/wiki/C%2B%2B)
* [Fortran](https://en.wikipedia.org/wiki/Fortran)
* [Java](https://www.java.com/en/)
* [Scala](https://www.scala-lang.org/)
* [Python](https://www.anaconda.com/download/#macos)
* [Julia](https://julialang.org/)
* [R](https://www.r-project.org/)
* [Octave](https://www.gnu.org/software/octave/)
* [JavaScript](https://www.w3schools.com/js/)

<!--
https://doc.rust-lang.org/book/ch01-02-hello-world.html
https://elixir-lang.org/crash-course.html
https://gobyexample.com/hello-world
-->

*Package Managers*
* [Maven](https://maven.apache.org/)
* [Sbt](https://www.scala-sbt.org/)
* [Conda](https://docs.conda.io/en/latest/)
* [Pypi](https://pypi.org/)
* [Homebrew](https://brew.sh/)

*Integrated Development Environments (IDEs)*
* [Intellij](https://www.jetbrains.com/idea/)
* [PyCharm](https://www.jetbrains.com/pycharm/)
* [Rstudio](https://www.rstudio.com/)
* [Juno](https://junolab.org/) / [Atom](https://atom.io/)

### Installation

I typically develop on Mac OS or on Linux (Redhat/Ubuntu). These installation guidelines are what I used to get this code working on my Mac (little modification is needed to get this working on linux). Language specific installation instructions are included with each language page.

The code below will install Homebrew on Mac. Brew also supplies a linux version.

```
mkdir homebrew && curl -L https://github.com/Homebrew/brew/tarball/master | tar xz --strip 1 -C homebrew
```

### Tutorials

<!--
Code Essentials
* Importing Functionality
* Unit Testing
* Formating / Typing Testing
-->

* [C](./C/README.md)
* [C++](./C++/README.md)
* [Fortran](./Fortran/README.md)
* [Java](./Java/README.md)
* [Scala](./Scala/README.md)
* [Python](./Python/README.md)
* [Julia](./Julia/README.md)
* [R](./R/README.md)
* [Octave](./Octave/README.md)
* [JavaScript](./JavaScript/README.md)

*Note:* It's worth noting that many of these languages can be called from or integrated into Python. Python is a great language for nicely stitching together various languages. Just look at packages like numerical python (numpy)!

## Environments

It can be hell managing multiple dependancies for a project. For example, you might need two different versions of a package installed for two different projects. I cover two examples of how to manage environments without resorting to using a [virtual machine](https://en.wikipedia.org/wiki/Virtual_machine) or (Lord forbid) manually handling package installations/Paths.

The [Conda environment](./Environments/Conda/README.md) example is meant for use with python, julia, and/or R.

The [Docker container](./Environments/Docker/README.md) example is generalizable to other languages, but I use python in the example.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Other Resources

* [Rosetta Code](https://rosettacode.org/wiki/Rosetta_Code)
* [Duo Coder](https://jasonpark.me/DuoCoder/public/)
* [Wikibooks Algorithms](https://en.wikibooks.org/wiki/Algorithm_Implementation)

## Acknowledgements

A big thank you to David Harrington for his help writing the examples in C. I am a statistician at heart and the help of my software engineering friends went far to making this repository possible.


<!--
Future Examples
https://darrenjw.wordpress.com/2011/07/16/gibbs-sampler-in-various-languages-revisited/
-->
