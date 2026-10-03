import socket
import sys
from datetime import datetime

def scan_port(host, port, timeout=0.5):
    """Проверяет, открыт ли TCP-порт."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout)
    result = sock.connect_ex((host, port))
    sock.close()
    return result == 0  # 0 означает успех

def scan_ports(host, ports, timeout=0.5):
    open_ports = []
    for port in ports:
        if scan_port(host, port, timeout):
            open_ports.append(port)
            print(f"Порт {port} открыт")
    return open_ports



ip = input("ведите ip для проверки порта:")    

# сканер
target = ip
ports_range = range(20, 1025)  # сканируем с 20 по 1024

start = datetime.now()
open_list = scan_ports(target, ports_range)
end = datetime.now()

print(f"Открытые порты: {open_list}")
print(f"Время сканирования: {end - start}")