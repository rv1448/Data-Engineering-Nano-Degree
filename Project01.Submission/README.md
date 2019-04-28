## PROJECT ONE SUBMISSION

### Introduction
__Sparkify__, a new startup company with a music streaming app, it wants to analyze how the music streaming app is performing with the users. It collects user activity of the songs in JSON format and song data is also JSON formt. 

### Problem Description

Create a ETL data model in __POSTGRE__ that can be used to analyze user questions on how songs are performing. The Analytics team want to do analysis on the user data and perform query's to measure the app and song activity.

* User Activity JSON record 
``` json 
{"artist":"A Fine Frenzy","auth":"Logged In","firstName":"Anabelle","gender":"F","itemInSession":0,"lastName":"Simpson","length":267.91138,"level":"free","location":"Philadelphia-Camden-Wilmington, PA-NJ-DE-MD","method":"PUT","page":"NextSong","registration":1541044398796.0,"sessionId":256,"song":"Almost Lover (Album Version)","status":200,"ts":1541377992796,"userAgent":"\"Mozilla\/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit\/537.36 (KHTML, like Gecko) Chrome\/36.0.1985.125 Safari\/537.36\"","userId":"69"}
```
* Song Metadata JSON record
``` json 
{"num_songs": 1, "artist_id": "AREVWGE1187B9B890A", "artist_latitude": -13.442, "artist_longitude": -41.9952, "artist_location": "Noci (BA)", "artist_name": "Bitter End", "song_id": "SOFCHDR12AB01866EF", "title": "Living Hell", "duration": 282.43546, "year": 0}
```
* Song Details
 <ol>
<li>artist_id, artist_name </li>   __Artist details__ <br>
<li>artist_latitude, artist_longitude, artist_location</li>  __Location__ <br>
<li>duration, num_songs </li> __song details__<br>
<li>song_id, title, year </li>  __song details__<br>
 
Discuss the purpose of this database in the context of the startup, Sparkify, and their analytical goals.
State and justify your database schema design and ETL pipeline.
[Optional] Provide example queries and results for song play analysis.
 
 
 
    
