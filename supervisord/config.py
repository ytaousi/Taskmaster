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
        self.config = configparser.ConfigParser(allow_no_value=True, strict=False)
        if not os.path.exists(self.args.config_file):
            raise FileNotFoundError(f"Configuration file not found: {self.args.config_file}")
        try:
            with open(self.args.config_file, 'r') as f:
                self.raw_config = f.read()
        except Exception as e:
            print(f"Error reading configuration file: {e}")
            self.is_valid = False
            return
        self.is_valid = self.validate_config()

    def validate_config(self):
        is_valid = True
        config_lines = self.raw_config.splitlines()
        section = None
        seen_keys = {}

        for line in config_lines:
            line = line.strip()
            if not line or line.startswith(';') or line.startswith('#'):
                continue

            if line.startswith('[') and line.endswith(']'):
                section = line[1:-1]
                seen_keys[section] = set()
                continue

            if section and '=' in line:
                key = line.split('=', 1)[0].strip()
                if key in seen_keys[section]:
                    print(f"Error: Duplicate key '{key}' found in section '{section}'.")
                    is_valid = False
                seen_keys[section].add(key)

                if section.startswith("program:") and key not in self.programSection:
                    print(f"Warning: Unknown key '{key}' in section '{section}'.")
                    is_valid = False

            if section and section not in self.sections and not section.startswith("program:"):
                print(f"Warning: Unknown section '{section}' in configuration file.")
                is_valid = False

        return is_valid

    def print_config(self):
        for section in self.config.sections():
            print(f'[{section}]')
            for key, value in self.config.items(section):
                print(f'{key} = {value}')
            print()

__all__ = ['configFile']