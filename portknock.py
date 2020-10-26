import socket
import time
import interactive
from paramiko import SSHClient, AutoAddPolicy
from knock_secrets import *

def knock(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((host, port))
        s.close()
    except ConnectionRefusedError:
        pass

def knock_open():        
    for port in KNOCK_PORTS:
        knock(IP, port)
    time.sleep(1)

def knock_close():
    for port in KNOCK_PORTS[::-1]:
        knock(IP, port)

def client_connect():
    client = SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(AutoAddPolicy())
    client.connect(IP, username=USERNAME, password=PASSWORD)
    channel = client.invoke_shell()
    print(repr(client.get_transport()))
    interactive.interactive_shell(channel)
    channel.close()
    client.close()

def run():
    knock_open()
    client_connect()
    knock_close()

if __name__ == "__main__":
    run()