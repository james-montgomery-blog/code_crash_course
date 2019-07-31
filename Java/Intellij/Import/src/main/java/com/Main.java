package com;

import org.apache.spark.api.java.JavaSparkContext;
import org.apache.spark.sql.Dataset;
import org.apache.spark.sql.Row;
import org.apache.spark.sql.SparkSession;

// https://hortonworks.com/tutorial/setting-up-a-spark-development-environment-with-java/

public class Main {

    public static void main(String[] args) {

        SparkSession spark = SparkSession
                .builder()
                .appName("Spark App")
                .master("local[*]").config("spark.driver.bindAddress", "127.0.0.1")
                .getOrCreate();

        JavaSparkContext sc = new JavaSparkContext(spark.sparkContext());
        sc.setLogLevel("WARN");

        String path = "../../../Test_Data/test.csv";

        Dataset<Row> df = Utils.read_csv(path, spark);

        df.show();

    }

}



