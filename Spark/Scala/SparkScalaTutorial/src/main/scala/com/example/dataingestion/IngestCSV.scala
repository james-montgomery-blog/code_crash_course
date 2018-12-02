package com.example.dataingestion

import org.apache.spark.sql.SparkSession

// var = variable and val = immutable

object IngestCSV {

  def main(args: Array[String]) {

    val spark = SparkSession
      .builder()
      .appName("SparkSessionZipsExample")
      .master("local[*]").config("spark.driver.bindAddress", "127.0.0.1")
      .getOrCreate()

    val path = "/Users/jamesmontgomery/Desktop/Code_Sandbox/ReadCSV/test.csv"
    val df = spark.read.format("csv").option("header", "true").load(path)

    val df2 = df.select(
      df("Numbers")cast("float"),
      df("Dates").cast("String"),
      df("Fruit").cast("String")
    )

    df2.show()

  }

}
