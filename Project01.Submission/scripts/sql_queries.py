# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays;"
user_table_drop = "DROP TABLE IF EXISTS users;"
song_table_drop = "DROP TABLE IF EXISTS songs;"
artist_table_drop = "DROP TABLE IF EXISTS artists;"
time_table_drop = "DROP TABLE IF EXISTS time;"



user_table_create = ("""CREATE TABLE IF NOT EXISTS users(user_id int PRIMARY KEY, first_name varchar, last_name varchar, gender varchar, level varchar)
""")

song_table_create = ("""CREATE TABLE IF NOT EXISTS songs(song_id varchar PRIMARY KEY, title varchar, artist_id varchar, year int, duration NUMERIC)
""")

artist_table_create = ("""CREATE TABLE IF NOT EXISTS artists(artist_id varchar PRIMARY KEY, name varchar, location varchar, lattitude float, longitude float)
""")

time_table_create = ("""CREATE TABLE IF NOT EXISTS time(start_time timestamp PRIMARY KEY, hour int, day int, week int, month int, year int , weekday varchar)
""")

songplay_table_create = ("""CREATE TABLE IF NOT EXISTS songplays(songplay_id SERIAL PRIMARY KEY, start_time timestamp, user_id int references users(user_id), level varchar, song_id varchar references songs(song_id), artist_id varchar references artists(artist_id), session_id int, location varchar, user_agent varchar)""")


# INSERT RECORDS


songplay_table_insert = """INSERT INTO songplays(start_time,user_id,level,song_id , artist_id , session_id , location , user_agent ) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"""

user_table_insert = (""" INSERT INTO users(user_id,first_name,last_name,gender,level) VALUES(%s,%s,%s,%s,%s) ON CONFLICT ON CONSTRAINT users_pkey 
DO NOTHING""")
 

song_table_insert = ("""INSERT INTO songs(song_id,title,artist_id,year,duration) VALUES(%s,%s,%s,%s,%s)""")

artist_table_insert = ("""INSERT INTO artists(artist_id,name,location,lattitude,longitude) VALUES(%s,%s,%s,%s,%s) ON CONFLICT ON CONSTRAINT artists_pkey DO NOTHING""")


time_table_insert = ("""INSERT INTO time(start_time , hour, day, week, month, year,weekday)
VALUES(%s,%s,%s,%s,%s,%s,%s) ON CONFLICT ON CONSTRAINT time_pkey DO NOTHING""")


# FIND SONGS

song_select = (""" SELECT songs.song_id, artists.artist_id  FROM songs join artists on songs.artist_id = artists.artist_id where songs.title = %s and artists.name = %s and songs.duration = %s""")

# QUERY LISTS

create_table_queries = [user_table_create, song_table_create, artist_table_create, time_table_create,songplay_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]