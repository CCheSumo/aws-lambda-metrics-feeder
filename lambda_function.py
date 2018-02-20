import time
import logging

from config import Config
from feeder import Feeder

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    id = context.aws_request_id
    logger.info('started lambda_handler with id %s' % id)
    feeder = Feeder(event['url'])
    while not feeder.done():
        time.sleep(Config.sleep_interval)
    return "finished lambda_handler with id %s" % id
