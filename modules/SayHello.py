from ctypes.wintypes import tagRECT


class SayHello:
    def __init__(self, target="World"):
        self.target = target

    def say(self):
        print(f"Hellom {self.target}!!")


if __name__ == '__main__' :
    app = SayHello()
    app.say()
    app = SayHello("Someone")
    app.say()