from status import Status

class Pet:
    def __init__(self, name):
        self.name = name
        self.status = Status()

    def feed(self):
        self.status.feed()

    def play(self):
        self.status.play()

    def sleep(self):
        self.status.sleep()

    def get_status(self):
        return self.status.get_status()
