import argparse
import random
from shutil import move
import time

from pythonosc import udp_client

def main():
    moveController = MoveController()

    while (True):
        text = input()
        if text == "h":
            moveController.moveLeft()
        elif text == "j":
            moveController.moveBack()
        elif text == "k":
            moveController.moveForward()
        elif text == "l":
            moveController.moveRight()
        else:
            break
        

class MoveController:
    address = "127.0.0.1"
    port = 9000
    inputVertical = "/input/Vertical"
    inputHorizontal = "/input/Horizontal"

    def __init__( self ) :
        parser = argparse.ArgumentParser()
        parser.add_argument("--ip", default=MoveController.address, help="The ip of the OSC server")
        parser.add_argument("--port", type=int, default=MoveController.port, help="The port the OSC server is listening on")
        args = parser.parse_args()
        self.client = udp_client.SimpleUDPClient(args.ip, args.port)

    def moveForward(self):
        self.client.send_message(MoveController.inputVertical, 0.5)
        time.sleep(0.5) 
        self.client.send_message(MoveController.inputVertical, 0.0)

    def moveBack(self):
        self.client.send_message(MoveController.inputVertical, -0.5)
        time.sleep(0.5) 
        self.client.send_message(MoveController.inputVertical, 0.0)

    def moveRight(self):
        self.client.send_message(MoveController.inputHorizontal, 0.5)
        time.sleep(0.5) 
        self.client.send_message(MoveController.inputHorizontal, 0.0)

    def moveLeft(self):
        self.client.send_message(MoveController.inputHorizontal, -0.5)
        time.sleep(0.5) 
        self.client.send_message(MoveController.inputHorizontal, 0.0)


if __name__ == "__main__":
    main()