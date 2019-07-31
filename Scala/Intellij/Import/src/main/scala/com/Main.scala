package com

import org.apache.spark.sql.SparkSession

object Main {

  def main(args: Array[String]) {

    val spark = SparkSession
      .builder()
      .appName("SparkSessionZipsExample")
      .master("local[*]").config("spark.driver.bindAddress", "127.0.0.1")
      .getOrCreate()

    spark.sparkContext.setLogLevel("WARN")

    val input_path = "../../../Test_Data/test.csv"

    val df = Utils.read_csv(input_path, spark)

    df.show()

  }

}
