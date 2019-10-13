DataWrangling with Spark
------------------------
`Functional Programming`
	- Spark is written in scala 
	- Functional programming perfect for distributed systems 
	- comes from functions you use in algebra class 
	- functions only rely on the input 
	- in python with  a function you can still access global variables 
	- __pyspark api__ is written using functional programming in mind 
	- __spark__ is written in scala so __pyspark api__ first transilates your code to scala 
	- the way spark handles functions that don't have to rely on external variables is by having the function run on each machine and after each machine finishes 
	- they will combine results together 

`Pure functions in bread factory`
	- if you write a function that preserves input and avoid side effects its called functional programming



`Spark api details`
	- pyspark - can access low level rdd using SparkContext 
	- SparkContext is the main entry, connects the cluster with main application 
	- SparkContext is used to create objects of lower abstractions 
	- to create context we need to SparkConf() object to specify specifices of the application
	```
	from pyspark import SparkContext, SparkConf
	configure = SparkConf().setAppname('name').setMaster('IP address')
	sc = SparkContext(conf=configure)
	```
	- SparkSession - To read from Data frame, SparkContext spark sql equvalent 
	``` 
	import pyspark
	from pyspark import SparkConf
	from pyspark.sql import SparkSession
	spark = SparkSession.builder.appName('name').config('config option','config value').getOrCreate()
	spark.SparkContext.getConf().getAll()
	```
`Imperative programming vs Declarative Programming`
	- imperative programming - Spark DataFrame & Python
	- Declarative programming - sql 
	- Imperative programming - has to declare in details how and what operation need to performed
	- Declarative programming is an abstraction on top of imperative programming
` Spark SQL `
[Spark SQL built in functions](https://spark.apache.org/docs/latest/api/sql/index.html)
[Spark SQL guide](https://spark.apache.org/docs/latest/sql-getting-started.html)

Debugging and Optimization
--------------------------
` _corrupt_record `
	- when you parse a corrupt file it will have a new field - __ _corrupt_record_ __
	``` python
	df.where(df["_corrup_record"].isNotNull()).collect()
	```


` Spark Scripts `

` Submitting Spark Scripts`
	- spark.stop() is need when you want the execution to stop
	- for streaming application stop is not needed 
	- path for the spark submit command line - which spark-submit

``` python 
from pyspark.sql import SparkSession

if __name__ == '__main__':
	spark = SparkSession\
		.builder\
		.appName("LowerSongTitles")
		.getOrCreate()

	log_of_songs = ["intro - xx", "havana"]

distributed_song_log = spark.sparkContext.parallelize(log_of_songs)
print(distributed_song_log)
spark.stop()
```

```python
#which spark-submit
# /usr/bin/spark-submit --master yarn ./scriptname
```
* Storing and Retrieving Data on Cloud
`Reading and Writing Data to HDFS`
	- copy from local to EMR cluster - scp ~/folder/file.txt EMR-cluster:~/
	- creating a new directory in HDFS - hdfs dfs -mkdir /user
	- list of hdfs syntax - hdfs/ hdfs dfs

`Debugging is Hard`

* Data Errors 
	- corrupted records - '_corrup_record=None'
* Debugging your code 
	- Since client is connected to executor and any print statements added to debug run on worker node, Client cannot see the print statement. 
	- use accumilators to debug the code 
``` python
from pyspark.sql import SparkSession
from pyspark.context import SparkContext 

spark.sparkContext.setLogLevel("ERROR")

spark=SparkSession.builder.cofig('spark.ui.port',3000).getOrCreate()
__accumilators__
incorrect_value = SparkContext.accumlator(0,0)
incorrect_value.value 
from pyspark.sql.functions import udf 
correct_ts = df.where(df['co1'].isNull()).withColumn("ts_digit",correct_ts(logs3.ts))
```

`Spark WebUI`
[Spark UI Metrics](https://spark.apache.org/docs/latest/monitoring.html)
	- job - as many actions/collect or writing data into DB  called in the code 
	- Task - smallest 
		- Smallest unit in stage 
		- series of spark transformations that can be run in parallel 
		- 10 part : 10 same tasks to complete stage
	- Stage - 
		- Units of work depend one another 
		- cant be further parallelized 
		- Transform and join : so Transform, Join are seperate stages
* Ports used to communicate
* Protocals - Different Ports because different protocals 
	- SSH -> 22 
	- HTTP/HTML -> 80
	- Spark Master communicates with workers on port 7077
	- Jupyter notebook -> 8888
	- Active Spark jobs -> 4040
	- Web UI -> 8080
* logging 
[Configuring Logging](https://spark.apache.org/docs/latest/configuration.html)
	``` python
	spark.SparkContext.setLogLevel("ERROR")
	```

`Code Optimization`
[Spark Application tuning](https://spark.apache.org/docs/latest/tuning.html)
[Spark_sql_tuning](https://spark.apache.org/docs/latest/sql-performance-tuning.html)

`Follow up`
	- short command to ssh into EMR using config file
	- copy from cluster local to HDFS
	- method names are case sensitive in spark 
	- group by and sum - is sum python or spark function
