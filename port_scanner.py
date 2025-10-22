import socket

target = "192.168.56.103"  # Replace with your target VM IP
ports = [21, 22, 23, 80, 443, 445, 3306]

print(f"[*] Scanning {target}...")

for port in ports:
    try:
        s = socket.socket()
        s.settimeout(1)
        s.connect((target, port))
        print(f"[+] Port {port} is OPEN")
        s.close()
    except:
        print(f"[-] Port {port} is closed or filtered")
