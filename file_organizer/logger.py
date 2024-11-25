# logger.py
import logging
import os

# Configure the log file path
LOG_FILE_PATH = os.path.join(os.path.dirname(__file__), 'loggfile.txt')

# Set up logging configuration
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(LOG_FILE_PATH),  # Log to 'logfile.txt'
        logging.StreamHandler()  # Also print logs to the console
    ]
)

def log_success(file, destination):
    """Log a message when a file is successfully moved."""
    logging.info(f"Moved {file} to {destination}")

def log_error(file, error_message):
    """Log an error if there’s an issue with moving the file."""
    logging.error(f"Error moving {file}: {error_message}")
