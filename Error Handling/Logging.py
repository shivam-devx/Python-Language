""" 
     Logging records events that happen while your program runs
     It's better than just using print() because 
        You can set levels (info , debug, warning, error, critical)
        logs can be saved to a file for later analysis
        you can format logs with timestams, module names , ets 
    common level:
        debug -> detail info (for developers)
        info -> general events(program started, finished)
        warning -> something unexpected but not fatal \
        Error -> serious problem , progrma may not work 
        critical -> very serious error, program may crash 
    
"""

# Example: 

import logging

logging.basicConfig(level=logging.INFO)
logging.debug("This is a debug message")

logging.info("Program started")
logging.warning("This is a warning")
logging.error("An error occurred")
logging.critical("Critical issue!")
print("\n")
# output:

# INFO:root:Program started
# WARNING:root:This is a warning
# ERROR:root:An error occurred
# CRITICAL:root:Critical issue!

# Another example:

import logging 

logging.basicConfig(filename="app.log", level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")


logging.info("Application started")
logging.debug("Debugging details here")
logging.error("Something went wrong")