import google.cloud.logging
import logging

# Initialize the Google Cloud Logging client
client = google.cloud.logging.Client()
client.setup_logging()

# Get the Odoo logger
logger = logging.getLogger('odoo')

# Example log message
logger.info('Google Cloud Logging has been configured for Odoo.')
