import logging


logger = logging.getLogger('Logger')
logger.setLevel(logging.DEBUG)


cli_handler = logging.StreamHandler()
cli_handler.setLevel(logging.DEBUG)
cli_formatter = logging.Formatter(
    fmt='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%H:%M:%S'
)
cli_handler.setFormatter(cli_formatter)


file_handler = logging.FileHandler(filename='artifacts/playwright_tests.log', mode='w')
file_handler.setLevel(logging.INFO)
file_formatter = logging.Formatter(
    fmt='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d at %H:%M:%S'
)
file_handler.setFormatter(file_formatter)


logger.addHandler(cli_handler)
logger.addHandler(file_handler)
