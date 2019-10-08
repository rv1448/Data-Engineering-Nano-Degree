import configparser


# CONFIG
config = configparser.ConfigParser()
config.read('dwh.cfg')

# DROP TABLES
staging_events_table_drop = "DROP TABLE IF EXISTS staging_event_data;"
staging_songs_table_drop = "DROP TABLE IF EXISTS staging_song_data;"
songplay_table_drop = "DROP TABLE IF EXISTS fact_songplay;"
user_table_drop = "DROP TABLE IF EXISTS dim_user;"
song_table_drop = "DROP TABLE IF EXISTS dim_song;"
artist_table_drop = "DROP TABLE IF EXISTS dim_artist;"
time_table_drop = "DROP TABLE IF EXISTS dim_time;"

 
staging_songs_table_create = ("""
CREATE TABLE staging_song_data(
artist_id VARCHAR(50),           
artist_latitude NUMERIC(5,2),     
artist_location VARCHAR(200),      
artist_longitude NUMERIC(5,2),   
artist_name  VARCHAR(200),        
duration FLOAT,           
num_songs INTEGER,          
song_id  VARCHAR(150),           
title VARCHAR(400),              
year INTEGER                
);
""")

staging_events_table_create = ("""
CREATE TABLE staging_event_data (
artist varchar(200),auth varchar(40),firstName varchar(50),gender char(1),
itemInSession INTEGER,lastName varchar(50),length FLOAT,
level varchar(30),location varchar(max),method varchar(30),
page varchar(40),registration BIGINT,
sessionId integer,
song varchar(200),
status integer,
ts BIGINT,
useragent varchar(500),
userId int
);
""")
 

songplay_table_create = ("""
CREATE TABLE fact_songplay(
songplay_id int identity(1,1) NOT NULL PRIMARY KEY, 
start_time timestamp, 
user_id int  NOT NULL, 
level varchar(30), 
song_id VARCHAR(150), 
artist_id VARCHAR(50) NOT NULL, 
session_id int NOT NULL, 
location VARCHAR(200),
user_agent varchar(max)
)distkey(song_id) sortkey(start_time);
""")

user_table_create = ("""
create table dim_user(
user_id int NOT NULL PRIMARY KEY, 
first_name  varchar(50),
lastName varchar(50),
gender char(1),
level varchar(30)
)diststyle all;
""")

song_table_create = ("""
create table dim_song(
song_id VARCHAR(150) NOT NULL PRIMARY KEY, 
title VARCHAR(400),
artist_id VARCHAR(50),
year int,
duration float
)distkey(song_id) ;
""")

artist_table_create = ("""
create table dim_artist(
artist_id VARCHAR(50) NOT NULL PRIMARY KEY, 
artist varchar(200),
location  VARCHAR(200),
lattitude  NUMERIC(5,2), 
longitude NUMERIC(5,2)
)diststyle all;
""")
 
time_table_create = ("""
create table dim_time(
start_time timestamp NOT NULL PRIMARY KEY, 
hour int,
day int,
week int,
month int,
year int,
weekday varchar(50)
)diststyle all;
""")

# STAGING TABLES

staging_events_copy = (
    """ copy staging_event_data from {}
        credentials 'aws_iam_role={}' region 'us-west-2' FORMAT AS JSON {};
""").format(config.get('S3','LOG_DATA'), config.get('IAM_ROLE','ARN'),config.get('S3','LOG_JSONPATH'))
 

staging_songs_copy = (
    """ copy staging_song_data from  {}
        credentials 'aws_iam_role={}' REGION 'us-west-2' FORMAT AS JSON 'auto';
    """).format(config.get('S3','SONG_DATA'),config.get('IAM_ROLE','ARN'))

# FINAL TABLES

songplay_table_insert = ("""
insert into fact_songplay
(start_time,user_id,level,song_id,artist_id,session_id,location,user_agent)
select TIMESTAMP 'epoch' + ts/1000 * interval '1 second' as start_time, 
userid as user_id,level, 
song_id,artist_id,sessionid as session_id,location,useragent as user_agent 
 from 
 staging_event_data  
  join dim_song 
on dim_song.title = staging_event_data.song
where (page = 'NextSong' AND ts IS NOT NULL AND USERID IS NOT NULL);
""")

user_table_insert = ("""
update dim_user
set 
 first_name = staging_event_data.Firstname
,lastName = staging_event_data.lastName
,gender = staging_event_data.Gender
,level = staging_event_data.level
FROM staging_event_data
WHERE dim_user.user_id = staging_event_data.userid;

INSERT INTO dim_user(user_id,first_name,lastName,gender,level)
SELECT userid,firstname,lastName,gender,level
FROM (SELECT userid,firstname,lastName,gender,level, 
row_number() over (partition by userid) as cnt  
FROM staging_event_data 
) dedup
WHERE NOT EXISTS (select 1 FROM dim_user  WHERE dedup.userid = dim_user.user_id)
AND CNT = 1 and dedup.userid IS NOT NULL ;
""")

song_table_insert = ("""

UPDATE dim_song 
set duration= staging_song_data.duration
,artist_id=staging_song_data.artist_id
,title=staging_song_data.title
,year=staging_song_data.year
FROM  staging_song_data
WHERE dim_song.song_id = staging_song_data. song_id;  

INSERT INTO dim_song
(song_id,artist_id,duration,title,year)
SELECT song_id,artist_id,duration,title,year
FROM
(
SELECT song_id,artist_id,duration,title,year, row_number() over(partition by song_id) as cnt
FROM staging_song_data
) dedup
WHERE cnt = 1 
AND NOT EXISTS (SELECT 1 FROM dim_song where dedup.song_id = dim_song.song_id);

""")

artist_table_insert = ("""
update dim_artist
set artist = artist_name 
,location = artist_location
,lattitude = artist_latitude 
,longitude = artist_longitude 
FROM staging_song_data
WHERE staging_song_data.artist_id = dim_artist.artist_id;

INSERT INTO dim_artist(artist_id,artist,location,lattitude,longitude)
select artist_id,artist, location, lattitude , longitude
from 
(
select artist_id,artist_name as artist,artist_location as location,artist_latitude as lattitude ,artist_longitude as longitude,
row_number() over(partition by artist_id order by year desc) as cnt 
FROM staging_song_data 
 ) dedup 
 where cnt = 1 
 and not exists (select 1 from dim_artist where dedup.artist_id =dim_artist.artist_id);
""")

time_table_insert = ("""

update dim_time 
set hour = EXTRACT(hr from DEDUP.start_time)  
, day = EXTRACT(d from DEDUP.start_time)  
, week = EXTRACT(w from DEDUP.start_time)   
, month = EXTRACT(mon from DEDUP.start_time)   
, year = EXTRACT(year from DEDUP.start_time)    
, WEEKDAY = CASE WHEN EXTRACT(weekday from DEDUP.start_time) = 0 THEN 'SUNDAY'
WHEN EXTRACT(weekday from DEDUP.start_time) = 1 THEN 'MONDAY'
WHEN EXTRACT(weekday from DEDUP.start_time) = 2 THEN 'TUESDAY'
WHEN EXTRACT(weekday from DEDUP.start_time) = 3 THEN 'WEDNESDAY'
WHEN EXTRACT(weekday from DEDUP.start_time) = 4 THEN 'THURSDAY'
WHEN EXTRACT(weekday from DEDUP.start_time) = 5 THEN 'FRIDAY'
WHEN EXTRACT(weekday from DEDUP.start_time) = 6 THEN 'SATURDAY' END  
FROM ( SELECT DISTINCT
  TIMESTAMP 'epoch' + ts/1000 *INTERVAL '1 second' AS start_time  
from staging_event_data 
 ) DEDUP
WHERE (dim_time.start_time = DEDUP.start_time);

INSERT INTO dim_time 
(start_time,hour,day,week,month,year,WEEKDAY)
SELECT start_time 
, EXTRACT(hr from start_time) AS hour
, EXTRACT(d from start_time) AS day
, EXTRACT(w from start_time) AS week
, EXTRACT(mon from start_time) AS month
, EXTRACT(year from start_time) AS year 
, CASE WHEN EXTRACT(weekday from start_time) = 0 THEN 'SUNDAY'
WHEN EXTRACT(weekday from start_time) = 1 THEN 'MONDAY'
WHEN EXTRACT(weekday from start_time) = 2 THEN 'TUESDAY'
WHEN EXTRACT(weekday from start_time) = 3 THEN 'WEDNESDAY'
WHEN EXTRACT(weekday from start_time) = 4 THEN 'THURSDAY'
WHEN EXTRACT(weekday from start_time) = 5 THEN 'FRIDAY'
WHEN EXTRACT(weekday from start_time) = 6 THEN 'SATURDAY' END WEEKDAY
FROM ( SELECT DISTINCT
  TIMESTAMP 'epoch' + ts/1000 *INTERVAL '1 second' AS start_time  
from staging_event_data 
 ) DEDUP
 WHERE NOT EXISTS (SELECT 1 FROM dim_time WHERE DEDUP.start_time = dim_time.start_time);
""")



# QUERY LISTS
create_table_queries = [staging_events_table_create, staging_songs_table_create, songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [ staging_events_table_drop, staging_songs_table_drop,songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]


copy_table_queries = [staging_events_copy, staging_songs_copy]
insert_table_queries = [ user_table_insert, song_table_insert, artist_table_insert, time_table_insert,songplay_table_insert]

