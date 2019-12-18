import sys
from threading import Thread
import grpc

import users_pb2_grpc as users_service
import users_types_pb2 as users_messages

import secrets
import string

count = 0
# add ip rotator with different threads
# ddos with botnet
# currently 5 threaded with big data chunks...


class zero(Thread):
    def run(self):
        global count
        while True:
            channel = grpc.insecure_channel('localhost:50051')
            try:
                grpc.channel_ready_future(channel).result(timeout=10)
            except grpc.FutureTimeoutError:
                sys.exit('Error connecting to server')
            else:
                stub = users_service.UsersStub(channel)
                metadata = [('ip', '127.0.0.1')]
                # replace with file big file --or maybe not consider because of i/o
                data = ''.join(secrets.choice(string.ascii_uppercase + string.digits)
                               for i in range(1024))
                response = stub.CreateUser(
                    users_messages.CreateUserRequest(username=data),
                    metadata=metadata,
                )
                if response:
                    count += 1
                    print(str(count), '\n')


class one(Thread):
    def run(self):
        global count
        while(True):
            channel = grpc.insecure_channel('localhost:50051')
            try:
                grpc.channel_ready_future(channel).result(timeout=10)
            except grpc.FutureTimeoutError:
                sys.exit('Error connecting to server')
            else:
                stub = users_service.UsersStub(channel)
                metadata = [('ip', '127.0.0.1')]
                # replace with file big file
                data = ''.join(secrets.choice(string.ascii_uppercase + string.digits)
                               for i in range(2048))
                response = stub.CreateUser(
                    users_messages.CreateUserRequest(username=data),
                    metadata=metadata,
                )
                if response:
                    count += 1
                    print(str(count))


class two(Thread):
    def run(self):
        global count
        while True:
            channel = grpc.insecure_channel('localhost:50051')
            try:
                grpc.channel_ready_future(channel).result(timeout=10)
            except grpc.FutureTimeoutError:
                sys.exit('Error connecting to server')
            else:
                stub = users_service.UsersStub(channel)
                metadata = [('ip', '127.0.0.1')]
                # replace with file big file
                data = ''.join(secrets.choice(string.ascii_uppercase + string.digits)
                               for i in range(4096))
                response = stub.CreateUser(
                    users_messages.CreateUserRequest(username=data),
                    metadata=metadata,
                )
                if response:
                    count += 1
                    print(str(count))


class three(Thread):
    def run(self):
        global count
        while True:
            channel = grpc.insecure_channel('localhost:50051')
            try:
                grpc.channel_ready_future(channel).result(timeout=10)
            except grpc.FutureTimeoutError:
                sys.exit('Error connecting to server')
            else:
                stub = users_service.UsersStub(channel)
                metadata = [('ip', '127.0.0.1')]
                # replace with file big file
                data = ''.join(secrets.choice(string.ascii_uppercase + string.digits)
                               for i in range(1024*1024))
                response = stub.CreateUser(
                    users_messages.CreateUserRequest(username=data),
                    metadata=metadata,
                )
                if response:
                    count += 1
                    print(str(count))


class four(Thread):
    def run(self):
        global count
        while True:
            channel = grpc.insecure_channel('localhost:50051')
            try:
                grpc.channel_ready_future(channel).result(timeout=10)
            except grpc.FutureTimeoutError:
                sys.exit('Error connecting to server')
            else:
                stub = users_service.UsersStub(channel)
                metadata = [('ip', '127.0.0.1')]
                # replace with file big file
                data = ''.join(secrets.choice(string.ascii_uppercase + string.digits)
                               for i in range(256))
                response = stub.CreateUser(
                    users_messages.CreateUserRequest(username=data),
                    metadata=metadata,
                )
                if response:
                    count += 1
                    print(str(count))


if __name__ == '__main__':
    zero_ = zero()
    one_ = one()
    two_ = two()
    three_ = three()
    four_ = four()

    zero_.start()
    one_.start()
    two_.start()
    three_.start()
    four_.start()
