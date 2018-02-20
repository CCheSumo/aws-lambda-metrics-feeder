import time
import logging
import zlib
from botocore.vendored import requests
from config import Config
from timer import Timer
from sessions import Sessions

logger = logging.getLogger()
logger.setLevel(logging.INFO)

class Feeder(object):

    def __init__(self, url):
        self.timer = Timer(Config.request_interval, self.task)
        self.sessions = Sessions()
        self.url = url
        self.start()

    def __del__(self):
        self.stop()

    def start(self):
        self.timer.start_timer()

    def stop(self):
        self.timer.cancel_timer()

    def done(self):
        return Config.number_requests == self.sessions.completed and (not self.sessions.pending)

    def encode(self, body):
        return zlib.compress(body.encode('utf-8'))

    def task(self):
        if self.sessions.completed < Config.number_requests:
            self.send()
        else:
            self.stop()

    def send(self):
        timestamp = time.time()
        body = "metric=metrics-sla  %d " % self.sessions.completed + str(int(timestamp))
        logger.debug("sending request %s ", body)
        self.sessions.add(timestamp, body)
        response = requests.post(self.url, data=self.encode(body), headers=Config.headers)
        self.sessions.delete(timestamp)
        logger.debug("finishing request %s with %s", body, str(response))
