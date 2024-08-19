import argparse
import sys
import os
from config import configFile

class my_supervisord:
    def __init__(self, args):
        self.config_file = configFile(args)
    
    def print_config(self):
        if self.config_file.is_valid:
            self.config_file.print_config()
        else:
            print("Invalid configuration file. Please fix the warnings and try again.")

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

if __name__ == '__main__':
    main()