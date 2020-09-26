from multiprocessing import Process, Pipe
from os import getpid
from datetime import datetime


class Proc():

    def __init__(self, name):
        self.name = name

    def __call__(self, f, *args, **kwargs):
        f(self, *args, **kwargs)

    def local_time(self, counter):
        return ' (LAMPORT_TIME={}, LOCAL_TIME={})'.format(counter,
                                                          datetime.now())

    def calc_recv_timestamp(self, recv_time_stamp, counter):
        return max(recv_time_stamp, counter) + 1

    def event(self, pid, counter):
        counter += 1

        x = f'Event in proc '
        y = f'{self.name} ({pid}) '
        z = f'{self.local_time(counter)}!'
        print(x+" "*(25-len(x))+y+" "*(10-len(y))+z)
        return counter

    def send_message(self, pipe, pid, counter):
        counter += 1
        pipe.send(('Empty shell', counter))

        x = f'Msg sent from proc '
        y = f'{self.name} ({pid}) '
        z = f'{self.local_time(counter)}'

        print(x+" "*(25-len(x))+y+" "*(10-len(y))+z)
        return counter

    def recv_message(self, pipe, pid, counter):
        message, timestamp = pipe.recv()
        counter = self.calc_recv_timestamp(timestamp, counter)

        x = f'Message recv at proc '
        y = f'{self.name} ({pid})'
        z = f'{self.local_time(counter)}'
        print(x+" "*(25-len(x))+y+" "*(10-len(y))+z)
        return counter


def process_one(self, pipe12):
    pid = getpid()
    counter = 0
    counter = self.event(pid, counter)
    counter = self.send_message(pipe12, pid, counter)
    counter = self.event(pid, counter)
    counter = self.recv_message(pipe12, pid, counter)
    counter = self.event(pid, counter)


def process_two(self, pipe21, pipe23):
    pid = getpid()
    counter = 0
    counter = self.recv_message(pipe21, pid, counter)
    counter = self.send_message(pipe21, pid, counter)
    counter = self.send_message(pipe23, pid, counter)
    counter = self.recv_message(pipe23, pid, counter)


def process_three(self, pipe32):
    pid = getpid()
    counter = 0
    counter = self.recv_message(pipe32, pid, counter)
    counter = self.send_message(pipe32, pid, counter)


if __name__ == '__main__':
    oneandtwo, twoandone = Pipe()
    twoandthree, threeandtwo = Pipe()

    process1 = Process(target=Proc("1"),
                       args=(process_one, oneandtwo,))
    process2 = Process(target=Proc("2"),
                       args=(process_two, twoandone, twoandthree))
    process3 = Process(target=Proc("3"),
                       args=(process_three, threeandtwo,))

    process1.start()
    process2.start()
    process3.start()

    process1.join()
    process2.join()
    process3.join()
