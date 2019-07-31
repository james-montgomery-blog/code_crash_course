name := "Import"

version := "0.1"

scalaVersion := "2.11.4"

// rm -r ~/.ivy2/cache

assemblyMergeStrategy in assembly := {
  case PathList("META-INF", xs @ _*) => MergeStrategy.discard
  case x => MergeStrategy.first
}

libraryDependencies ++= {
  val sparkVer = "2.1.0"
  Seq(
    "org.apache.spark" % "spark-core_2.11" % "2.1.0",
    "org.apache.spark" % "spark-sql_2.11" % "2.1.0",
    "gov.nist.math" % "jama" % "1.0.2"
  )
}


