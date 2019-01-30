import subprocess as sp


class Session(object):
    def __init__(self):
        self.running = True


if __name__ == '__main__':
    while Session.running:
        print("\n"*3)
        tmp = sp.call('clear', shell=True)
        Session.running = False
