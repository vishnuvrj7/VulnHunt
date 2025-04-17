import socket
from tqdm import tqdm
from time import sleep

def detailed_port_scan(target, port_range):
    open_ports = {}
    start_port, end_port = map(int, port_range.split('-'))
    
    with tqdm(total=end_port - start_port + 1, desc="Scanning Ports", unit="port") as pbar:
        for port in range(start_port, end_port + 1):
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(0.5)
                result = s.connect_ex((target, port))
                if result == 0:
                    try:
                        service_name = socket.getservbyport(port)
                        open_ports[port] = service_name
                    except OSError:
                        open_ports[port] = "Unknown"
                pbar.update(1)
                sleep(0.01)  # Simulating delay for better progress visibility
    return open_ports

def print_scan_results(results):
    for port, service in results.items():
        print(f"Port {port}: {service}")
