package com.example.nativeimport
import java.util

object NativeImport {
  def main(args: Array[String]): Unit = {

    val myList = new util.ArrayList[Integer](3)

    myList.add(3)
    myList.add(2)
    myList.add(1)

    System.out.println(myList)
  }
}
