package com;

import org.apache.spark.sql.Dataset;
import org.apache.spark.sql.Row;
import org.apache.spark.sql.SparkSession;

public class Utils {

    public static Dataset<Row> read_csv(String input_path, SparkSession spark) {

        return spark.read().option("header", "true").csv(input_path).toDF();

    }

}
