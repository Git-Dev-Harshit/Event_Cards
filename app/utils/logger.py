import logging
import os
from datetime import datetime
from logging.handlers import TimedRotatingFileHandler

def setup_logger():
    # Ensure logs directory exists
    logs_dir = os.path.join(os.getcwd(), "logs")
    if not os.path.exists(logs_dir):
        os.makedirs(logs_dir)

    # Create a log file named with the current date
    log_file = os.path.join(logs_dir, f"{datetime.now().strftime('%Y-%m-%d')}.log")

    # Configure log format
    log_format = "%(asctime)s - %(levelname)s - %(message)s"

    # Create a timed rotating file handler
    handler = TimedRotatingFileHandler(log_file, when="midnight", interval=1, backupCount=7)
    handler.suffix = "%Y-%m-%d"  # Ensure files are rotated datewise

    formatter = logging.Formatter(log_format)
    handler.setFormatter(formatter)

    # Set up a logger instance
    logger = logging.getLogger("flask_logger")
    logger.setLevel(logging.INFO)
    logger.addHandler(handler)

    return logger

# Initialize the logger
logger = setup_logger()
