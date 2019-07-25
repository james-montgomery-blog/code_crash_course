import org.apache.spark.sql.Dataset;
import org.apache.spark.sql.Row;
import org.apache.spark.sql.SparkSession;
import org.apache.spark.sql.types.StructType;


// https://hortonworks.com/tutorial/setting-up-a-spark-development-environment-with-java/

public class Main {

    public static void main(String[] args) {

        SparkSession spark = SparkSession
                .builder()
                .appName("SparkSessionZipsExample")
                .master("local[*]").config("spark.driver.bindAddress", "127.0.0.1")
                .getOrCreate();

        StructType schema = new StructType()
                .add("Numbers", "string")
                .add("Dates", "string")
                .add("Fruits", "string");

        String path = "/Users/jamesmontgomery/Desktop/Code_Sandbox/ReadCSV/test.csv";

//        Dataset<Row> df = spark.read()
//                //.option("mode", "DROPMALFORMED")
//                .schema(schema)
//                .csv(path);
//
//        df.show();

        Dataset<Row> df2 = spark.read().csv(path).toDF("Numbers", "Dates", "Fruit");


        df2.show();
    }

}
