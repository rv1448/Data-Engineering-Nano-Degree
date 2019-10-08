`Data Validation`
	- The process of ensuring the data is present, correct and meaningful
`DAG and Data Pipelines`
	- Data pipelines well expressed by DAG 
	- Users as __NODES__
	- Edges as __RELATIONSHIP__
	- DAG have edges with specific direction 
	- NO cycles exist 
`Apache Airflow`
* Airflow DAG
	```python
	import datetime 
	import logging 

	from airflow import DAG
	from airflow.operators.python_operator import PythonOperator
	def greet():
		logging.info("hello world!")

	dag = DAG(
		'lesson1:demo',
		start_date=datetime.datetime.now())
	gree_task = PythonOperator(
	task_id="greet_task",
	python_callable=greet
	dag=dag
	)
	```
* How it works ?? 
	- __SCHEDULER__ for orchestrating execution of jobs on trigger or schedule basis 
	- __QUEUE__ holds state of task and DAGS
	- __WORKER__ take data of the queue and executes individual tasks 
	- __DB__ holds connection and credentials 
	- __ORDER_OF_OPERATIONS__
		- The airflow scheduler starts DAG based on the time or external triggers 
		- Once a DAG is started, schedular looks at the steps and finds steps by looking at their dependencies 
		- The Scheduler places runnable steps in the queue 
		- workers picks the tasks and runs them 
`Buiding a Data Pipeline `
	```python 
	from airflow import DAG

	divvy_dag = DAG(
	description="Analysis bikeshare data"
	start_date = datetime(2019,2,4)
	schedule_interval='@daily'
	)
	from airflow.operators.python_operator import PythonOperator 
	def  hello_world():
		print("hello world!")

	task = PythonOperator(
		task_id = 'hello_world'
		python_callable=hello_world
		dag=divvy_dag)

	```
* Task Dependencies
	```python
	import datetime 
	import logging 

	from airflow import DAG
	from airflow.operators.python_operator import PythonOpertor
	
	def hello_world():
		logging.info("Hello world!")
	def addition():
		logging.info(f"2+2 = {}".format(2+2))
	def multiply():
                logging.info(f"2*2 = {}".format(2*2))
	def subtraction():
	                logging.info(f"2-2 = {}".format(2-2))
	def division():
	                logging.info(f"2/2 = {}".format(2/2))

	dag = DAG(
	"lesson1:exercise3",
	schedule_interval='@hourly',
	start_date=datetime.datetime.now()-datetime.timedelta(days=1)
	)
	
	addition_task = PythonOperator(
			task_id="addition",
			python_callable=addition,
			dag=dag 
			)	
	```
`Airflow Hooks`i
* Connections can be accessed in code via hooks. Hooks provide a reusable interface to external systems and databases. 
* with hooks, you dont have to worry about how and where to store these connection string and secrets in your code

	``` python 
	from airflow import DAG 
	from airflow.hooks.postgres_hook import PostgreHook
	from airflow.operators.python_operator import PythonOperator 


	def load():
		db_hook = PostgresHook('demo')
		df = db_hook.get_pandas_df('select * from rides')
		print(f"Successfully used postgrehook to return {len(df)} records")
	```
	
` Context Variables `	
[Complete Details](https://blog.godatadriven.com/zen-of-python-and-apache-airflow)
[AirFLow  Documentation](https://airflow.apache.org/macros.html)

