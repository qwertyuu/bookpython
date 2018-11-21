import sys
import traceback

import pydotenv
from airtable import Airtable
import bibli_sync
import logging
from logging.handlers import TimedRotatingFileHandler
from bibli import Bibli


def make_logger():
    logger = logging.getLogger('Bibli')
    logger.setLevel(logging.DEBUG)
    handler = TimedRotatingFileHandler('logs/bibli.log', when="midnight", interval=1)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s', '%Y-%m-%d %H:%M:%S')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger


def log_except_hook(*exc_info):
    global logger
    text = "".join(traceback.format_exception(*exc_info))
    logger.error("Unhandled exception: %s", text)


def main():
    try:
        my_bibli.login()
        my_bibli.hydrate_books()
    except BaseException as error:
        logger.exception("Exception from hydrate_books")
    else:
        bibli_sync.sync(airtable, my_bibli.book_objects, logger)
    finally:
        my_bibli.close()


sys.excepthook = log_except_hook
env = pydotenv.Environment(check_file_exists=True)
airtable = Airtable(env.get('AIRTABLE_BASE_KEY'), 'books', api_key=env.get('AIRTABLE_API_KEY'))
logger = make_logger()
my_bibli = Bibli(env.get('CARD_NUMBER'), env.get('PASSWORD'), logger)

if __name__ == "__main__":
    main()
