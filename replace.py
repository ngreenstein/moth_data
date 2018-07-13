import md_utils, serialize
import argparse, subprocess, datetime

# Back up the database and replace it from a `.sql` file
def replace(infile, backupFile, overwrite = False):

	# Back up the existing database
	backup = serialize.serialize(outfile = backupFile, overwrite = overwrite)

	if not backup:
		print "Database replace cancelled due to failed backup."
		return False
	
	command = "mysql -u {} -p{} {} < {}".format(	md_utils.config["db_user"],
	                                                                md_utils.config["db_password"],
	                                                                md_utils.config["db_database"],
	                                                                infile)
		
	proc = subprocess.Popen(command, shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
	error = proc.communicate()[1].strip()
	
	# Ignore MySQL 'errors' given when the operation was successful
	# (e.g. the one about passwords over command line), but print errors if the operation failed.
	if proc.returncode != 0:
	    print "The following error occurred while replacing the database:\n%s" % error
	else:
	    print "Successfully replaced database from '%s'" % infile

if __name__ == "__main__":
	
	# Set up the parser
	parser = argparse.ArgumentParser(description = "Replaces the moth database from a `.sql` file created with the `serialize` script. Backs up the existing database first.")
	parser.add_argument("infile", help = "The source file. Should be readable and of type `.sql`.")
	parser.add_argument("--backup", default = "backups/db_%s.sql" % datetime.datetime.now().strftime("%m-%d-%Y_%H-%M"), help = "The destination for a backup of the existing database. Defaults to `backups/current_date.sql`. Should be writeable and of type `.sql`.")
	parser.add_argument("--overwrite", action = "store_true", help = "Whether to overwrite an existing file while backing up. Defaults to no.")
	
	# Kick off the parser and execute the replace
	args = parser.parse_args()
	replace(infile = args.infile, backupFile = args.backup, overwrite = args.overwrite)
