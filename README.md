### pyUdpShutdown

This Python program can be used to remotely shutdown a running machine by sending the magic packet to it. Therefore, it has to be run with administrator privileges. It currently only supports Windows machines but can be easily adapted to shutdown any OS.

```
usage: pyUdpShutdown.py [-h] --mac [MAC address] --port [Port]

Program to remotely shutdown a machine by sending the magic packet via UDP.

optional arguments:
  -h, --help           show this help message and exit
  --mac [MAC address]  The MAC address of the machine to shutdown. Use either
                       format XX:XX:XX:XX:XX:XX:XX or XX-XX-XX-XX-XX-XX-XX
  --port [Port]        The port to listen to for the magic packet during
                       runtime of the machine.
```
