` umbers everyone should know`




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
` Follow Up`
* Difference between select and selectExpr in Spark DataFrame
* 
