`Numbers everyone should know`
 CPU 		0.4ns
 MEMORY		100ns
 STORAGE	16us
 NETWORK	150ms

* loading from storage to memory is 3000 times slower than CPU working on data that's already in memory 

`Big Data Numbers`
* when dealing with large dataset on a local machine 
	- The program loaded 8 GB of data from ssd to memory and processes it
	- the next batch of 8 gb is slower since it has to wait for the data to be loaded from ssd to memory 
	- Context switching which is called thrashing takes longer time 
	- Iterate through chunks on a big file and use the intermediate results to caliculate the final results 

`History of Distributed and Parallel Computing`
* distributed systems/algorithms/programming to computer networks individual and communicate with each other with message passing 
	- each node has there own memory and cpu 
* Parallel is a form of distributed computing 
	- group of processors have a shared memory - OpenMp or OpenCL

`MapReduce`
	- Map
		- Each mapper loads a partition from disk 
		- creates a tuple after all conditions are checked  - this data is unordered 
	- Shuffle 
		- All the records from intermediate files are shuffled, So all the tuples with common key end up on same machine 
	- reduce 
		- Values for given key are combined to produce final key value pair 

`Python MRjob`
```python
%%file wordcount.py
from mrjob.job import MRJob

class MRsongcount(MRjob):

	def mapper(self,_,key):
		yield(key,1)
	def reducer(self,key,value):
		yield(key,sum(value))
if __name__ == '__main__':
	MRsongcount.run()
```


`Spark cluster`
	- local mode 
	 	- everything happens on single machine
	- standalone cluster manager 
	- Yarn from hadoop project 
	- Mesos	open source resource manager 
`Why Data Lake ??`

* Abundance of Unstructured Data
	- Deep Json is hard to put in Tabular format 
	- PDF/Text could be stored as Blobs; But totally Useless unless processed to extract metrics
* The Rise of Big Data Technologies 
	- HDFS - Much lower cost per TB compared to MPP databases 
	- Schema on Read - good for unstructered data 
* New Roles & Advanced Analytics 
	- Single rigid representation of the data 
	- New type of analytics NLP needs to access raw data
	- Graph Processing & Recommender Systems 

`Schema on read - Schema Inference`

``` python
paymentSchema = StructType([
			StructField("payment_id",IntegerType()),
			StructField("customer_id",IntegerType())
			StructField("staff_id",IntegerType())
			])

df =spark.read.csv(path, schema=paymentSchema,sep=";",mode="DROPMALFORMED")
```

` Notes `
	- %%file filename.py will save the code into a file 

` Follow Up`
* Difference between select and selectExpr in Spark DataFrame

