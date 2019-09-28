
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
## accumilators 
incorrect_value = SparkContext.accumlator(0,0)
incorrect_value.value 
from pyspark.sql.functions import udf 
correct_ts = df.where(df['co1'].isNull()).withColumn("ts_digit",correct_ts(logs3.ts))
```

`Spark WebUI`
	- job - as many actions/collect or writing data into DB  called in the code 
	- Task - smallest 
		- Smallest unit in stage 
		- series of spark transformations that can be run in parallel 
		- 10 part : 10 same tasks to complete stage
	- Stage - 
		- Units of work depend one another 
		- cant be further parallelized 
		- Transform and join : so Transform, Join are seperate stages
* Ports used to communicates
* Protocals
	- SSH -> 22 
	- HTTP/HTML -> 80
	- Spark Master communicates with workers on port 7077
	- Jupyter notebook -> 8888
	- Active Spark jobs -> 4040
	- Web UI -> 8080
`Code Optimization`
[Spark Application tuning](https://spark.apache.org/docs/latest/tuning.html)
[Spark_sql_tuning](https://spark.apache.org/docs/latest/sql-performance-tuning.html)

`Follow up`
	- short command to ssh into EMR using config file
	- copy from cluster local to HDFS
	- method names are case sensitive in spark 
	- group by and sum - is sum python or spark function
