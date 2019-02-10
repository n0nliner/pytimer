from threading import Thread
import time as t


class Timer:
    def __init__(self, limit=None, start=True):
        self.time = 0
        self.limit = 9 if limit == None else limit
        if start : Thread(target=self.generator, args=[]).start()

    def generator(self):
        for i in range(self.limit):
            t.sleep(1)
            self.time += 1
            if self.time == self.limit+1:
                exit()


# timer1 = Timer(10)
# t.sleep(10)
# print(timer1.time)


class timeline(Timer):
    def __init__(self, limit=None, start=True):
        super(timeline, self).__init__(limit, start)
        self.timeline = {}

    def add(self, add_it):
        self.timeline.update({self.time:add_it})
        return self.timeline

    def delite(self, key):
        del self.timeline[key]
        return self.timeline



# timeline1 = timeline(15)
# while not timeline1.time == 4:
#     t.sleep(1)
#     print(timeline1.time)
