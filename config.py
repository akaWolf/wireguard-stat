import toml
from dataclasses import dataclass
import os

from utils import current_path

@dataclass(frozen=True)
class Configuration:
    active_cmd: str
    rx_cmd: str
    tx_cmd: str
    up_cmd: str
    down_cmd: str

config_path = os.path.join(current_path(), "config.toml")
config_dict = toml.load(config_path)

config = Configuration(**config_dict)
