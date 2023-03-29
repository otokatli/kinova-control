#
#   Hello World server in Python
#   Binds REP socket to tcp://*:5555
#   Expects b"Hello" from client, replies with b"World"
#

import time
import zmq
import os
import kinovagen3_pb2


print('Running server...')

gen3 = kinovagen3_pb2.KinovaGen3()

ZMQ_CLIENT_ADDRESS = os.environ["ZMQ_CLIENT_ADDRESS"]

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

while True:
    #  Wait for next request from client
    msg = socket.recv()

    gen3.ParseFromString(msg)

    print(f"Received q1: {gen3.q.q1}")

    #  Do some 'work'
    time.sleep(1)

    # Send reply back to client
    socket.send(b"recieved")
