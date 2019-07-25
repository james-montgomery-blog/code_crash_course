# Code Sandbox

This repository is full of very simple sample code that I originally wrote as I was learning various coding languages. This is not meant as a tutorial for learning how to use these languages, but I hope this simple code is helpful for someone looking for stripped down simple examples of how to get started in these languages. I sometimes use this repository as a reference for getting new software engineering (SE) and machine learning engineering (MLE) teammates up to speed on whatever language a particular project is built in.

<!-- TOC -->

Table of Contents
- [Code Sandbox](#code-sandbox)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Languages](#languages)
- [License](#license)

<!-- /TOC -->

## Getting Started

These instructions will help you get this code up and running on your local development environment.

### Prerequisites

For these languages you will need the necessary package for running the code. For compiled languages you will also need the appropriate [compiler](https://en.wikipedia.org/wiki/Compiler). Below is a list of the languages, package managers, and IDEs. Installation guides are included with the example code for each [language](#languages), with the exception of Homebrew and the IDEs. Homebrew installation is covered in the [installation](#installation) section. For IDE installation simply follow the IDE links below and follow the installation instructions. I strongly recommend using the IDEs for anyone contemplating seriously using these languages for production grade code.

*Languages*
* [C](https://en.wikipedia.org/wiki/C_(programming_language))
* [C++](https://en.wikipedia.org/wiki/C%2B%2B)
* [Java](https://www.java.com/en/)
* [Scala](https://www.scala-lang.org/)
* [Python](https://www.anaconda.com/download/#macos) 
* [Julia](https://julialang.org/)
* [R](https://www.r-project.org/)
* [Octave](https://www.gnu.org/software/octave/)
* [JavaScript](https://www.w3schools.com/js/)

*Package Managers*
* [Maven](https://maven.apache.org/)
* [Sbt](https://www.scala-sbt.org/)
* [Conda](https://docs.conda.io/en/latest/)
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

### Languages

* [C](./C/README.md)
* [C++](./C++/README.md)
* [Java](./Java/README.md)
* [Scala](./Scala/README.md)
* [Python](./Python/README.md)
* [Julia](./Julia/README.md)
* [R](./R/README.md)
* [Octave](./Octave/README.md)
* [JavaScript](./JavaScript/README.md)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
