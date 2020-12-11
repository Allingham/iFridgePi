import RPi.GPIO as GPIO
import time
from socket import *

udp_ip = "255.255.255.255"
udp_port = 9050

L1 = 12
L2 = 16
L3 = 20
L4 = 21

C1 = 6
C2 = 13
C3 = 19
C4 = 26

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(L1, GPIO.OUT)
GPIO.setup(L2, GPIO.OUT)
GPIO.setup(L3, GPIO.OUT)
GPIO.setup(L4, GPIO.OUT)

GPIO.setup(C1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

broad = socket(AF_INET, SOCK_DGRAM)
broad.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)


def send_char(to_send):
    broad.sendto(to_send, ('<broadcast>', udp_port))


def read_line(line, characters):
    GPIO.output(line, GPIO.HIGH)
    if GPIO.input(C1) == 1:
        print(characters[0])
        send_char(characters[0])
    if GPIO.input(C2) == 1:
        print(characters[1])
        send_char(characters[1])
    if GPIO.input(C3) == 1:
        print(characters[2])
        send_char(characters[2])
    if GPIO.input(C4) == 1:
        print(characters[3])
        send_char(characters[3])
    GPIO.output(line, GPIO.LOW)


try:
    while True:
        read_line(L1, ["1", "2", "3", "A"])
        read_line(L2, ["4", "5", "6", "B"])
        read_line(L3, ["7", "8", "9", "C"])
        read_line(L4, ["*", "0", "#", "D"])
        time.sleep(0.20)

except KeyboardInterrupt:
    print("\nProgram is stopped")
