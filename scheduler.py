import threading
import time


class Updater(threading.Thread):
    def __init__(self, callback_func, callback_args, wait_minutes=10, *args, **kwargs):
        super(Updater, self).__init__(*args, **kwargs)
        self.interval = wait_minutes*60
        self.running = True

        self.callback_func = callback_func
        self.callback_args = callback_args

    def stop(self):
        self.running = False
    
    def run(self):
        while self.running:
            self.callback_func(*self.callback_args)
            time.sleep(self.interval)

        