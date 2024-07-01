import logging

def configure_logging(app):
    logging.basicConfig(level=logging.DEBUG)
    app.logger.setLevel(logging.DEBUG)
