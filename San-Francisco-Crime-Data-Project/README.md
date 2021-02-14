
## Project Overview

In this project, I was provided with a real-world dataset, extracted from Kaggle, on San Francisco crime incidents, and I provided statistical analyses of the data using Apache Spark Structured Streaming. I used knowledge I've learned to create a Kafka server to produce data, and ingest data through Spark Structured Streaming.

## Development Environment

If you wish to develop your project locally, you will need to set up your environment properly as described below:

Spark 2.4.3
Scala 2.11.x
Java 1.8.x
Kafka build with Scala 2.11.x
Python 3.6.x or 3.7.x

Environment Setup (Only Necessary if You Want to Work on the Project Locally on Your Own Machine)

For Macs or Linux:

1. Download Spark from https://spark.apache.org/downloads.html. Choose "Prebuilt for Apache Hadoop 2.7 and later."
2. Unpack Spark in one of your folders (I usually put all my dev requirements in /home/users/user/dev).
3. Download binary for Kafka from this location https://kafka.apache.org/downloads, with Scala 2.11, version 2.3.0. Unzip in your local directory where you unzipped your Spark binary as well. Exploring the Kafka folder, you’ll see the scripts to execute in bin folders, and config files under config folder. You’ll need to modify zookeeper.properties and server.properties.
4. Download Scala from the official site, or for Mac users, you can also use brew install scala, but make sure you download version 2.11.x.
5. Run below to verify correct versions:
java -version
scala -version
6. Make sure your ~/.bash_profile looks like below (might be different depending on your directory):
export SPARK_HOME=/Users/dev/spark-2.4.3-bin-hadoop2.7
export JAVA_HOME=/Library/Java/JavaVirtualMachines/jdk1.8.0_181.jdk/Contents/Home
export SCALA_HOME=/usr/local/scala/
export PATH=$JAVA_HOME/bin:$SPARK_HOME/bin:$SCALA_HOME/bin:$PATH

### How to run the project

Initialize infrastructure (environment and kafka)

Open console and run ./start.sh to setup environment.

Run

$ cd config
$ /usr/bin/zookeeper-server-start zookeeper.properties
to initialize zookeeper.

Open new console and run
$ cd config
$ /usr/bin/kafka-server-start server.properties
to initialize kafka.

### Start Kafka producer

Open new console and run python kafka_server.py to start kafka producer.
Open new console and run python consumer_server.py to test kafka producer with a kafka consumer.

### Start spark streaming

Open new console and run

$ spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.11:2.3.4 --master local[*] data_str




### How did changing values on the SparkSession property parameters affect the throughput and latency of the data?

Parameters in SparkSession property allows increased and decrease throughput for exmaple "maxOffsetsPerTrigger" limits the offsets processed per trigger interval to a maximum number by default it's unlimited.

### What were the 2-3 most efficient SparkSession property key/value pairs? Through testing multiple variations on values, how can you tell these were the most optimal?

I achived optimal resutls with "maxOffsetsPerTrigger" = 10 and "maxOffsetsPerTrigger" = 10. Furthermore, I could increase amount of memory by setting spark.executor.memory: and improve executor parallelism by setting spark.default.parallelism: on executors. 
