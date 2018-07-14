import md_utils
import argparse, csv
from . import pilot_config

def serializeRatings(outfile):
	# Run the query
	waves = ",".join(map(lambda item: "'%s'" % item, pilot_config["waves"])) # Convert the list of waves into something like "'1.0', '1.1'"
	query = open("pilot/ratings.sql", "r").read() % waves # Avoid escaping issues by preparing query by hand
	cursor = md_utils.db().cursor()
	cursor.execute(query)
	
	# Save the CSV
	writer = csv.writer(outfile)
	writer.writerow([col[0] for col in cursor.description]) # Header row
	writer.writerows(cursor.fetchall())
	
	# Clean up
	cursor.close()
	outfile.close()
	
	
def serializeStimuli(outfile):
	print "serialize stimuli to %s" % outfile

if __name__ == "__main__":

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
