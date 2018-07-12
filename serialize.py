import md_utils
import argparse, subprocess

# Set up the parser
parser = argparse.ArgumentParser(description = "Serializes moth data. Generates a SQL file representing the entire database contents.")
parser.add_argument("outfile", help = "The destination file. Should be writeable and of type `.sql`.")
outfile = parser.parse_args().outfile

# Serialize the entire database into a .sql file
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
