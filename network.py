import socket
import random

def resolve_ip(target_url):
    try:
        return socket.gethostbyname(target_url)
    except socket.gaierror:
        print("\033[91mError: Invalid URL/IP provided.\033[0m")
        return None

def create_packet(size):
    return random._urandom(size)
