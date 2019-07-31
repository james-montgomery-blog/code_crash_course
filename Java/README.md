# Java

## History

Java was originally developed by James Gosling at Sun Microsystems (which has since been acquired by Oracle) and released in 1995 as a core component of Sun Microsystems' Java platform. Java is relatively easy to learn, has a nice object oriented framework, and a broad user base.

It's a nice compromise between the performance of C languages and the ease of use of Python or Julia.

## Installation

```
brew install java
brew install maven
```

## HelloWorld

```
javac -d . ./HelloWorld/HelloWorld.java
java HelloWorld
```

```
javac -d . ./HelloWorld/HelloWorld.java
jar -cf HelloWorld.jar HelloWorld.class
java -cp HelloWorld.jar HelloWorld
```

# Intellij Instructions

To create full-fledged java projects you probably want to use an IDE like intellij to help manage the project. It's pretty easy to create or import a maven project into intellij. You can then run and develop code from there. When you are done, it's easy to then package that project in a jar (or fat jar) to move into a production environment. I like fat jars because all of the dependancies are included with the jar.

*Note:* Java dependancies defined in the `pom.xml` file.

## HelloWorld

```
cd Intellij/HelloWorld
mvn package
java -cp target/HelloWorld-1.0-SNAPSHOT.jar com.HelloWorld
```

## Import

```
cd Intellij/Import
mvn clean compile assembly:single
java -cp target/Import-1.0-SNAPSHOT-jar-with-dependencies.jar com.Main
```
