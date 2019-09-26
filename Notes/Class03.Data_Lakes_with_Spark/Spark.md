
` Spark Scripts `

` Submitting Spark Scripts`
* 
``` python 
from pyspark.sql import SparkSession

if __name__ == '__main__':
	spark = SparkSession\
		.builder\
		.appName("LowerSongTitles")
		.getOrCreate()

	log_of_songs = [
	"intro - xx"
	, "havana"
	]
distributed_song_log = spark.sparkContext.parallelize(log_of_songs)
print(distributed_song_log)
spark.stop()
```

```python
#which spark-submit
# /usr/bin/spark-submit --master yarn ./scriptname
```

