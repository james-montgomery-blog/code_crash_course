package com

import org.apache.spark.sql.{DataFrame, SparkSession}

// var = variable and val = immutable

object Utils {

  def read_csv(input_path:String, spark:SparkSession) : DataFrame = {


    return spark.read.format("csv").option("header", "true").load(input_path)

  }

}
