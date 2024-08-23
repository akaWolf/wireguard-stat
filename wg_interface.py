import subprocess

from config import config

def is_active():
    out = subprocess.getoutput(config.active_cmd)
    return len(out) != 0

def get_statistics():
    rx = subprocess.getoutput(config.rx_cmd)
    tx = subprocess.getoutput(config.tx_cmd)
    return (int(rx), int(tx))
