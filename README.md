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
usage: serialize.py [-h] [--overwrite] outfile

Serializes moth data. Generates a SQL file representing the entire database
contents.

positional arguments:
  outfile      The destination file. Should be writeable and of type `.sql`.

optional arguments:
  -h, --help   show this help message and exit
  --overwrite  Whether to overwrite an existing file. Defaults to no.
</pre>

Example:

```
$ python -m serialize backup.sql
```

#### replace

<pre>
usage: replace.py [-h] [--backup BACKUP] [--overwrite] infile

Replaces the moth database from a `.sql` file created with the `serialize`
script. Backs up the existing database first.

positional arguments:
  infile           The source file. Should be readable and of type `.sql`.

optional arguments:
  -h, --help       show this help message and exit
  --backup BACKUP  The destination for a backup of the existing database.
				   Defaults to `backups/current_date.sql`. Should be writeable
				   and of type `.sql`.
  --overwrite      Whether to overwrite an existing file while backing up.
				   Defaults to no.
</pre>

Example:

```
$ python -m replace newDb.sql --backup backups/oldDb.sql --overwrite
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
