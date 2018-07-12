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

### serialize

usage: `serialize.py [-h] [--ratings | --stimuli] outfile`

Serializes moth pilot data. Generates a SQL file representing the entire database contents by default, or more focused reports on either ratings or stimuli if requested.

positional arguments:

- `outfile`: The destination file. Should be .sql for the entire database (default), and .csv for ratings or stimuli reports (see below).

optional arguments:

-   `-h, --help`: show this help message and exit
-   `--ratings`: serialize ratings data
-   `--stimuli`: serialize stimuli data
