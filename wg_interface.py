import subprocess

def is_active():
    out = subprocess.getoutput("cat /proc/net/dev | grep wg0")
    return len(out) != 0

def get_statistics():
    rx = subprocess.getoutput(r"cat /proc/net/dev | grep -oP 'wg0'':\s*\K\d+'")
    tx = subprocess.getoutput(r"cat /proc/net/dev | grep -oP 'wg0'':\s*(\d+\s+){8}\K\d+'")
    return (int(rx), int(tx))
