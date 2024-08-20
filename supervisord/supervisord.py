import argparse
import sys
import os
from config import configFile
import socket

class my_supervisord:
    def __init__(self, args):
        self.config_file = configFile(args)
        #self.pid = subprocess.call(["lsof", "-t -i:9001 -sTCP:LISTEN"])
        self.pid = os.getpid()

    def print_config(self):
        if self.config_file.is_valid:
            self.config_file.print_config()
        else:
            print("Invalid configuration file. Please fix the warnings and try again.")
    def getPid(self):
        return self.pid

def main():
    parser = argparse.ArgumentParser(description='Supervisord')
    default_config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'config.ini')
    parser.add_argument('-c', '--config_file', type=str, default=default_config_path, help='Path to the configuration file')
    args = parser.parse_args()
    
    try:
        supervisor = my_supervisord(args)
        supervisor.print_config()
    except FileNotFoundError as e:
        print(e, file=sys.stderr)
        sys.exit(1)
    
    serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serv.bind(('0.0.0.0', 9002))
    serv.listen(5)
    while True:
        conn, addr = serv.accept()
        from_client = ''
        while True:
            data = conn.recv(4096)
            if not data: break
            from_client += data.decode('utf8')
            print (f'From client: {from_client}')
            conn.send("I am SERVER\n".encode())
        conn.close()
        print ('client disconnected and shutdown')

__all__ = ['my_supervisord']

if __name__ == '__main__':
    main()