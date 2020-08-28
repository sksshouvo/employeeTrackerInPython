import sched, time

class scheduleCLass:
    def __init__(self):
        self.s = sched.scheduler(time.time, time.sleep)    
    
    def print_time(self, a='default'):
        print("From print_time", time.time(), a)
    def print_some_times(self):
        print(time.time())
        self.s.enter(10, 1, self.print_some_times)
        # s.enter(5, 2, print_time, argument=('positional',))
        # s.enter(5, 1, print_time, kwargs={'a': 'keyword'})
        self.s.run()
        print(time.time())