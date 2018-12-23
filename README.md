# Code Sandbox

This sandbox is full of very simple sample code that I originally wrote as I was learning various coding languages. This is not meant as a tutorial for learning how to use these various languages, but I hope this simple code is helpful for someone looking for stripped down simple examples of how to get started in these languages.

## Getting Started

These instructions will get you get the code her up and running on your local development environment.

### Prerequisites

For these languages you will at least need the necessary package for running the code. For compiled languages you will also need the appropriate compiler. If you don't have these already installed, please see the installation section of the page.

* [Scala](https://www.scala-lang.org/) & [Sbt](https://www.scala-sbt.org/)
* [Java](https://www.java.com/en/) & [Maven](https://maven.apache.org/)
* [R](https://www.r-project.org/)
* [Python](https://www.anaconda.com/download/#macos) (Anaconda Recommended)
* [Intellij](https://www.jetbrains.com/idea/) (Optional)
* [PyCharm](https://www.jetbrains.com/pycharm/) (Optional)
* [Rstudio](https://www.rstudio.com/) (Optional)
* [Homebrew](https://brew.sh/) (Optional)

### Installing

I typically develop on Mac OS or on Linux (Redhat/Ubuntu). These installation guidelines are what I used to get this code working on my Mac (little modification is need to get this working on linux).

We'll start by installing homebrew, a very useful package manager.

```
mkdir homebrew && curl -L https://github.com/Homebrew/brew/tarball/master | tar xz --strip 1 -C homebrew
```

Next we'll install scala and java as well as their respective package managers.

```
brew install scala
brew install sbt

brew install java
brew install maven
```

I recommend working with scala and java using the Jetbrains intellij IDE: [Download Here](https://www.jetbrains.com/idea/).

We can now install R.

```
brew install r
brew install Caskroom/cask/xquartz
```

I recommend working with R using the Rstudio IDE: [Download Here](https://www.rstudio.com/)

You will also need a distribution of python. I recomend using Anaconda: [Download Here](https://www.anaconda.com/download/#macos).

I recommend working with python using the Jetbrains PyCharm IDE: [Download Here](https://www.jetbrains.com/pycharm/). I also recommend getting familiar with virtual environments and jupyter notebooks.

### Running Code

I leave it up to you to get acquainted with each IDE. Below is a b are bones refresher on how to execute code in the languages in this repository.

**Scala**
```
scalac file.scala
scala file
```

**Java**
```
javac file.java
java file
```

**C**
```
gcc file.c
./a.out
```

**C++**
```
g++ file.cpp
./a.out
```

**Python**
```
python file.py
```

**R**
```
Rscript file.R
```

**JavaScript**
```
node file.js
```
I recommend running js code in a browser rather than through the terminal.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
