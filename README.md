# Moth Data

## Setup

1. `$ pip install mysql-connector-python`
1. Add database credentials to `md_utils`

## Development

- To run something specific: from the `moth_data` folder,  
	```$ python -m script
	```  
	Example:  
	```$ python -m serialize
	```   
	In a submodule: from the `moth_data` folder,  
	```
	$ python -m submodule.script
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

## Modules

### (main)

#### serialize

<pre>
usage: serialize.py [-h] outfile

Serializes moth data. Generates a SQL file representing the entire database
contents.

positional arguments:
  outfile     The destination file. Should be writeable and of type `.sql`.

optional arguments:
  -h, --help  show this help message and exit
</pre>

Example:

```
$ python -m serialize backup.sql
```

### pilot

#### pilot.serialize

<pre>
usage: serialize.py [-h] (--ratings | --stimuli) outfile

Serializes moth pilot data. Generates a CSV file representing either ratings or stimuli.

positional arguments:
  outfile     The destination file. Should be writeable and of type `.csv`.

optional arguments:
  -h, --help  show this help message and exit
  --ratings   serialize ratings data
  --stimuli   serialize stimuli data
</pre>

Example:

```
$ python -m pilot.serialize --ratings backup.csv
```
