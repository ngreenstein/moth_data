import md_utils
import argparse, subprocess
from . import pilot_config

# Serialize the entire database into a .sql file
def serializeDb(outfile):
	# Can't do this nicely with the MySQL connector, so just use `subprocess`
	command = "mysqldump -u {} -p{} --databases {} > {}".format(	md_utils.config["db_user"],
																	md_utils.config["db_password"],
																	md_utils.config["db_database"],
																	outfile)
	proc = subprocess.Popen(command, shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
	error = proc.communicate()[1].strip()
	# Ignore MySQL 'errors' given when the operation was successful
	# (e.g. the one about passwords over command line), but print errors if the operation failed.
	if proc.returncode != 0:
		print "The following error occurred while serializing the database:\n%s" % error
	else:
		print "Successfully serialized database to %s" % outfile

def serializeRatings(outfile):
	pass
	
def serializeStimuli(outfile):
	pass

# Create parser for command-line interface
parser = argparse.ArgumentParser(description = "Serializes moth pilot data. Generates a SQL file representing the entire database contents by default, or more focused reports on either ratings or stimuli if requested.")
# All actions require an output file. Kept as string (for mysqldump).
parser.add_argument("outfile", help = "The destination file. Should be .sql for the entire database (default), and .csv for ratings or stimuli reports (see below).")
# The action taken depends on arguments: default is whole db, `--ratings` flag is ratings, and `--stimuli` flag is stimuli
# Action is determined by the value of `operation`, a pointer to the relevant function
# The default value for `operation` is the `serializeDb` function (because the default beavior is to serialize the full db)
parser.set_defaults(operation = serializeDb)
# Only allow *either* `--ratings` *or* `--stimuli`, not both
actionGroup = parser.add_mutually_exclusive_group()
# Change the `operation` pointer based on the presence of a `--ratings` or `--stimuli` flag
actionGroup.add_argument("--ratings", action = "store_const", const = serializeRatings, dest = "operation", help = "serializes ratings data")
actionGroup.add_argument("--stimuli", action = "store_const", const = serializeStimuli, dest = "operation", help = "serializes stimuli data")

# Kick off the parser
args = parser.parse_args()
# Call the relevant operation, and pass in the specified outfile
args.operation(args.outfile)


# cursor = md_utils.db().cursor()

# cursor.close()