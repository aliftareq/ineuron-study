import logging

# initializing logger
logging.basicConfig(filename="newfile.log", format="%(asctime)s %(levelname)s %(message)s")

logger = logging.getLogger()

# setting logger level
logger.setLevel(logging.DEBUG)

# calling GUI module
logging.info("Calling GUICode file")

# calling GUI module
from GUI import GUIcode

a = GUIcode

logging.info("Returned from file")

# code for command prompt script execution
