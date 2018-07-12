import mysql.connector, atexit
from mysql.connector import errorcode

# Public Variables

config = {
	"db_user": "moth_radio",
	"db_password": "password", # DON'T COMMIT PASSWORDS
	"db_database": "moth_radio"
}

# Private Variables

_db = None

# Public Methods

def db():
	global _db
	if _db: return _db
	try:
		db = mysql.connector.connect(	user = config["db_user"],
										password = config["db_password"],
										host = "localhost",
										database = config["database"])
		_db = db
		return _db
	except mysql.connector.Error as error:
		if error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
			print "Database credentials incorrect; update config in md_utils."
		else:
			print error
	
# Private Methods

def _closeDb():
	if _db: db().close()
	
# Cleanup

atexit.register(_closeDb)
