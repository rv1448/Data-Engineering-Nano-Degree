import os
import configparser
from datetime import datetime
from pyspark.sql import SparkSession
from pyspark.sql.functions import udf, col
from pyspark.sql.functions import year, month, dayofmonth, hour, weekofyear, date_format
from pyspark.sql.types import StructType, StructField
from pyspark.sql.types import  IntegerType,StringType,DecimalType,LongType,DoubleType
from pyspark.sql.types import TimestampType
from pyspark.sql.functions import to_timestamp
from pyspark.sql.functions import monotonically_increasing_id 
from pyspark.sql.window import Window
from pyspark.sql import functions as F 

config = configparser.ConfigParser()
config.read('dl.cfg')

os.environ['AWS_ACCESS_KEY_ID']=config['AWS_ACCESS_KEY_ID']
os.environ['AWS_SECRET_ACCESS_KEY']=config['AWS_SECRET_ACCESS_KEY']


def create_spark_session():
    spark = SparkSession \
        .builder \
        .config("spark.jars.packages", "org.apache.hadoop:hadoop-aws:2.7.0") \
        .getOrCreate()
    ## Additional parameters for fast data upload 
    spark.conf.set("spark.hadoop.fs.s3a.multiobjectdelete.enable","false")
    spark.conf.set("spark.hadoop.fs.s3a.fast.upload","true")  
    spark.conf.set("spark.sql.parquet.filterPushdown", "true")  
    spark.conf.set("spark.sql.parquet.mergeSchema", "false")  
    spark.conf.set("spark.hadoop.mapreduce.fileoutputcommitter.algorithm.version", "2")
    
    return spark


def process_song_data(spark, input_data, output_data):
     """
        Description:
        This function loads song_data from S3 and processes it by extracting the songs and artist tables
        and then again loaded back to S3
        
        Parameters:
            spark       : Spark Session
            input_data  : location of song_data json files with the songs metadata
            output_data : S3 bucket were dimensional tables in parquet format will be stored
    """ 
        
    # get filepath to song data file
    song_data = input_data+'*/*/*/*.json'
    
    #schema of the json 
    song_schema = StructType([
    StructField('artist_id',StringType()),  
    StructField('artist_latitude',DoubleType()),
    StructField('artist_location',StringType()),
    StructField('artist_longitude',DoubleType()),
    StructField('artist_name',StringType()),
    StructField('duration',DoubleType()),
    StructField('num_songs' ,IntegerType()),
    StructField('song_id',StringType()),
    StructField('title',StringType()),
    StructField('year',IntegerType())   
    ])
    
    
  
    # read song data file
    df = spark.read.json(song_data,schema=song_schema)
    
    # Song and artist columns needed 
    dim_song_columns = ['song_id','artist_id','duration','title','year']
    dim_artist_columns = ['artist_id', 'artist_name', 'artist_location', 'artist_latitude', 'artist_longitude']

    # extract columns to create songs table
    songs_table = df.selectExpr(*dim_song_columns).dropDuplicates() 

    
    # write songs table to parquet files partitioned by year and artist
    songs_table.write.parquet(output+'dimsong')

    # extract columns to create artists table
    artists_table = df.selectExpr(*dim_artist_columns).dropDuplicates()
    
    # write artists table to parquet files
    artists_table.write.parquet(output+'dimartist')


def process_log_data(spark, input_data, output_data):
    """
        Description:
        This function loads log_data from S3 and processes it by extracting the songs and artist tables
        and then again loaded back to S3
        
        Parameters:
            spark       : Spark Session
            input_data  : location of song_data json files with the songs metadata
            output_data : S3 bucket were dimensional tables in parquet format will be stored
    """
    # get filepath to log data file
    log_data =input_data+'/*/*/*.json'
    
    #log schema of the json 
    log_schema = StructType([
    StructField('artist',StringType()),
    StructField('auth',StringType()),
    StructField('firstName',StringType()),
    StructField('gender',StringType()),
    StructField('itemInSession',IntegerType()),
    StructField('lastName',StringType()),
    StructField('length',DoubleType()),
    StructField('level',StringType()),
    StructField('location',StringType()),
    StructField('method',StringType()),
    StructField('page',StringType()),
    StructField('registration',StringType()),
    StructField('sessionId',IntegerType()),    
    StructField('song',StringType()),
    StructField('status',IntegerType()),
    StructField('ts',LongType()),
    StructField('userAgent',StringType()),
    StructField('userId',StringType())
    ])
    # read log data file
    df = spark.read.json(log_data,schema=log_schema)
    
    # filter by actions for song plays
    df = df.where(col('page') == 'NextSong')
    
    # dim user columns 
    dim_user_columns = ['userid','firstname','lastName','gender','level']
    
    # extract columns for users table    
    user_table = df.selectExpr(*dim_user_columns).dropDuplicates().filter(col('userid').isNotNull()) 
    
    # write users table to parquet files
    user_table.write.parquet(output+'dimuser')
 
    


    # extract columns to create time table
     
    df.selectExpr("cast(ts/1000 as timestamp) as time").alias('time').createOrReplaceTempView("time_table")
    time_table = spark.sql("select DISTINCT time, hour(time) as hour, day(time) as day,weekofyear(time) as week,\
          month(time) as month,year(time) as year,date_format(time, 'EEEE') as weekday  FROM time_table")


    
    # write time table to parquet files partitioned by year and month
    time_table.write.parquet(output+'dimtime')

    
    # read in song data to use for songplays table
    song_df = spark.read.parquet(output_data+'dimsong')

    # extract columns from joined song and log datasets to create songplays table 
    songplays_table = df_log.where(col('page') == 'NextSong')\
.join(dim_song,df_log.song  == song_df.title)\
.selectExpr("cast(ts/1000 as timestamp) as time",'monotonically_increasing_id() as songplay_id','userId as user_id','level','song_id','artist_id','sessionId as session_id','location','userAgent as user_agent')  
    # write songplays table to parquet files partitioned by year and month
    songplays_table.write.parquet(output+'songplay_table')


def main():
    spark = create_spark_session()
    input_data = "s3a://udacity-dend/"
    output_data = "'s3a://udacity-dend-submission/"
        


    process_song_data(spark, input_data, output_data)    
    process_log_data(spark, input_data, output_data)


if __name__ == "__main__":
    main()
