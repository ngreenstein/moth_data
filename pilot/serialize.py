import md_utils
import argparse
from . import pilot_config

def serializeDb(outfile):
	pass

def serializeRatings(outfile):
	pass
	
def serializeStimuli(outfile):
	pass

parser = argparse.ArgumentParser(description = "Serializes moth pilot data. Generates a SQL file representing the entire database contents by default, or more focused reports on either ratings or stimuli if requested.")
parser.add_argument("outfile", type = argparse.FileType("w"), help = "The destination file. Should be .sql for the entire database (default), and .csv for ratings or stimuli reports (see below).")
parser.set_defaults(operation = serializeDb)
typeGroup = parser.add_mutually_exclusive_group()
typeGroup.add_argument("--ratings", action = "store_const", const = serializeRatings, dest = "operation", help = "serializes ratings data")
typeGroup.add_argument("--stimuli", action = "store_const", const = serializeStimuli, dest = "operation", help = "serializes stimuli data")

args = parser.parse_args()
args.operation(args.outfile)


# cursor = md_utils.db().cursor()

# cursor.close()