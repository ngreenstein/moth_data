# Moth Data

## Setup

1. `$ pip install mysql-connector-python`

## General

- To run something specific: from the `moth_data` folder,  
	```
	$ python -m subfolder.file
	```  
	Example:  
	```
	$ python -m pilot.serialize
	```
- To use the database from a Python script:

	```
	import md_utils
	cursor = md_utils.db().cursor()
	# do stuff
	cursor.close()
	```

## Pilot
