# Scala

## History

Scala combines object-oriented and functional programming in one concise, high-level language. Scala's static types help avoid bugs in complex applications, and its JVM and JavaScript runtimes let you build high-performance systems with easy access to huge ecosystems of libraries.

Scala is perfect for building data pipelines!

## Installation

```
brew install scala
brew install sbt
```

## HelloWorld

```
scalac -d . ./HelloWorld/HelloWorld.scala
scala HelloWorld

```

```
scalac -d HelloWorld.jar ./HelloWorld/HelloWorld.scala
scala -cp HelloWorld.jar HelloWorld
```

# Intellij Instructions

To create full-fledged scala projects you probably want to use an IDE like intellij to help manage the project. It's pretty easy to create or import a sbt project into intellij. You can then run and develop code from there. When you are done, it's easy to then package that project in a fat jar to move into a production environment.

## HelloWorld

```
cd Intellij/HelloWorld
sbt package
scala -cp target/scala-2.13/helloworld_2.13-0.1.jar com.HelloWorld
```

You can also create a fat jar!

```
echo -e 'addSbtPlugin("com.eed3si9n" % "sbt-assembly" % "0.14.6")' > project/plugins.sbt
sbt assembly
scala -cp target/scala-2.13/HelloWorld-assembly-0.1.jar com.HelloWorld
```
