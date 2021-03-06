import threading

class Timer:

    def __init__(self, interval, task):
        self.interval = interval
        self.task = task
        self.timer = None
        self.start_timer_lock = threading.Lock()

    def __del__(self):
        self.cancel_timer()

    def start_timer(self):

        self.timer = threading.Timer(self.interval, self.start_timer)
        self.timer.daemon = True
        # Lock to resolve racing condition for start_timer and reset_timer
        if self.start_timer_lock.acquire(False):
            if not self.timer.isAlive():
                self.timer.start()
            self.start_timer_lock.release()

        self.task()

    def cancel_timer(self):
        if self.timer is not None:
            self.timer.cancel()
