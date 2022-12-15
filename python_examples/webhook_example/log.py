import logging

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s --- %(message)s',
    level=logging.INFO
)


def info(msg):
    logging.info(msg)


def error(msg):
    logging.error(msg)
