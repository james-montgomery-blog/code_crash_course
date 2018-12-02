package com.example.internalimport
import com.example.helloworld.HelloWorld2
//import com.example.helloworld.{HelloWorld, HelloWorld2}

object InternalImport {
  def main (args: Array[String]): Unit = {
    HelloWorld2.import_test()
  }
}
