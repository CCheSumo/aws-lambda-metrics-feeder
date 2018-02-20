import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

class Sessions(object):

    pending = {}
    completed = 0

    def add(self, key, val):
        self.pending[key] = val
        self.completed += 1

    def delete(self, key):
        del self.pending[key]
