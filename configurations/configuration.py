from configparser import ConfigParser, NoOptionError, NoSectionError
import os

def load_conf(section: str, name: str, default=None) -> str:
    config = ConfigParser()
    config.read("settings.ini")
    try:
        output = config.get(section, name)
    except (NoOptionError, NoSectionError):
        output = default
    return output