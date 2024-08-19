import configparser
import os

class configFile:
    def __init__(self, args):
        self.args = args
        self.sections = {
            "rpcinterface:supervisor",
            "inet_http_server",
            "supervisord",
            "supervisorctl",
            "unix_http_server"
        }
        self.programSection = {
            "command",
            "numprocs",
            "process_name",
            "umask",
            "directory",
            "autostart",
            "autorestart",
            "exitcodes",
            "startretries",
            "startsecs",
            "stopsignal",
            "stopwaitsecs",
            "stdout_logfile",
            "stderr_logfile",
            "environment"
        }
        self.config = configparser.ConfigParser()
        if not os.path.exists(self.args.config_file):
            raise FileNotFoundError(f"Configuration file not found: {self.args.config_file}")
        self.config.read(self.args.config_file)
        self.is_valid = self.validate_config()

    def validate_config(self):
        is_valid = True
        for section in self.config.sections():
            if section not in self.sections and not section.startswith("program:"):
                print(f"Warning: Unknown section '{section}' in configuration file.")
                is_valid = False
            if section.startswith("program:"):
                program_name = section.split(":", 1)[1]
                print(f"Validating program section: {program_name}")
                for key in self.config[section]:
                    if key not in self.programSection:
                        print(f"Warning: Unknown key '{key}' in section '{section}'.")
                        is_valid = False
        return is_valid

    def print_config(self):
        for section in self.config.sections():
            print(f'[{section}]')
            for key, value in self.config.items(section):
                print(f'{key} = {value}')
            print()

__all__ = ['configFile']