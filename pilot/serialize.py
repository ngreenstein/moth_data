import md_utils
import argparse
from . import pilot_config

def serializeRatings(outfile):
	print "serialize ratings to %s" % outfile
	
def serializeStimuli(outfile):
	print "serialize stimuli to %s" % outfile

# Create parser for command-line interface
parser = argparse.ArgumentParser(description = "Serializes moth pilot data. Generates a CSV file representing either ratings or stimuli.")
# Both actions require an output file
parser.add_argument("outfile", type = argparse.FileType("w"), help = "The destination file. Should be writeable and of type `.csv`.")
# The action taken depends on arguments: `--ratings` flag for ratings and `--stimuli` flag for stimuli
# Action is determined by the value of `operation`, a pointer to the relevant function
# Require exacty one of `--ratings` and `--stimuli`
actionGroup = parser.add_mutually_exclusive_group(required = True)
# Change the `operation` pointer based on the presence of a `--ratings` or `--stimuli` flag
actionGroup.add_argument("--ratings", action = "store_const", const = serializeRatings, dest = "operation", help = "serialize ratings data")
actionGroup.add_argument("--stimuli", action = "store_const", const = serializeStimuli, dest = "operation", help = "serialize stimuli data")

# Kick off the parser
args = parser.parse_args()
# Call the relevant operation, and pass in the specified outfile
args.operation(args.outfile)
