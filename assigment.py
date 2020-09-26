from multiprocessing import Process, Pipe
from os import getpid
from datetime import datetime


class Proc():

    def __init__(self, name, id_):
        self.name = name
        self.id = id_

    def __call__(self, f, *args, **kwargs):
        f(self, *args, **kwargs)

    def local_time(self, counter):
        return f'{counter}'

    def calc_recv_timestamp(self, recv_time_stamp, counter):
        counter[self.id] += 1
        for i in range(len(counter)):
            counter[i] = max(recv_time_stamp[i], counter[i])
        return counter

    def event(self, pid, counter):
        z0 = f'{self.local_time(counter)}'
        counter[self.id] += 1
        x = f'Event in proc '
        y = f'{self.name} '
        z = f'{self.local_time(counter)}'
        print(x+" "*(25-len(x))+y+" "*0*(10-len(y))+z0+" -> "+z)
        return counter

    def send_message(self, pipe, pid, counter):
        z0 = f'{self.local_time(counter)}'
        counter[self.id] += 1
        pipe.send(('Oh hi Mark', counter))

        x = f'Msg sent from proc '
        y = f'{self.name} '
        z = f'{self.local_time(counter)}'

        print(x+" "*(25-len(x))+y+" "*0*(10-len(y))+z0+" -> "+z)
        return counter

    def recv_message(self, pipe, pid, counter):
        z0 = f'{self.local_time(counter)}'
        message, timestamp = pipe.recv()
        counter = self.calc_recv_timestamp(timestamp, counter)

        x = f'Message recv at proc '
        y = f'{self.name} '
        z = f'{self.local_time(counter)}'
        print(x+" "*(25-len(x))+y+" "*0*(10-len(y))+z0+" -> "+z)
        return counter


def process_one(self, pipe12):
    pid = getpid()
    counter = [0, 0, 0]
    counter = self.send_message(pipe12, pid, counter)
    counter = self.send_message(pipe12, pid, counter)
    counter = self.event(pid, counter)
    counter = self.recv_message(pipe12, pid, counter)
    counter = self.event(pid, counter)
    counter = self.event(pid, counter)
    counter = self.recv_message(pipe12, pid, counter)
    print(f'Final state: {self.name} {counter}')


def process_two(self, pipe21, pipe23):
    pid = getpid()
    counter = [0, 0, 0]
    counter = self.recv_message(pipe21, pid, counter)
    counter = self.recv_message(pipe21, pid, counter)
    counter = self.send_message(pipe21, pid, counter)
    counter = self.recv_message(pipe23, pid, counter)
    counter = self.event(pid, counter)
    counter = self.send_message(pipe21, pid, counter)
    counter = self.send_message(pipe23, pid, counter)
    counter = self.send_message(pipe23, pid, counter)
    print(f'Final state: {self.name} {counter}')


def process_three(self, pipe32):
    pid = getpid()
    counter = [0, 0, 0]
    counter = self.send_message(pipe32, pid, counter)
    counter = self.recv_message(pipe32, pid, counter)
    counter = self.event(pid, counter)
    counter = self.recv_message(pipe32, pid, counter)
    print(f'Final state: {self.name} {counter}')


if __name__ == '__main__':
    oneandtwo, twoandone = Pipe()
    twoandthree, threeandtwo = Pipe()

    process1 = Process(target=Proc("A", 0),
                       args=(process_one, oneandtwo,))
    process2 = Process(target=Proc("B", 1),
                       args=(process_two, twoandone, twoandthree))
    process3 = Process(target=Proc("C", 2),
                       args=(process_three, threeandtwo,))

    process1.start()
    process2.start()
    process3.start()

    process1.join()
    process2.join()
    process3.join()
