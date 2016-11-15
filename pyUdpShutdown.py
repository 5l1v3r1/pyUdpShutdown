import socket
import signal
import sys
import subprocess
import argparse

parser = argparse.ArgumentParser(
    description='Program to remotely shutdown a machine by sending the magic packet via UDP.')

parser.add_argument('--mac', metavar='MAC address', type=str, nargs='?', required=True,
                    help='The MAC address of the machine to shutdown. '
                         'Use either format XX:XX:XX:XX:XX:XX:XX or XX-XX-XX-XX-XX-XX-XX')

parser.add_argument('--port', metavar='Port', type=int, nargs='?', required=True,
                    help='The port to listen to for the magic packet during runtime of the machine.')

args = parser.parse_args()

if '-' in args.mac:
    MAC_ADDRESS = args.mac.split('-')
elif ':' in args.mac:
    MAC_ADDRESS = args.mac.split(':')

mac_bytes = list()
for b in MAC_ADDRESS:
    mac_bytes.append(b.decode('hex'))

mac_bytes = 16 * mac_bytes

ff_bytes = 6 * list('FF'.decode('hex'))
magic_packet = ''.join(ff_bytes + mac_bytes).encode('hex')

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', args.port))


def signal_handler(signal, frame):
    sock.close()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

while True:
    data, addr = sock.recvfrom(1024)
    if data.encode('hex') == magic_packet:
        subprocess.call('shutdown /s /t 0 /f', shell=True)
