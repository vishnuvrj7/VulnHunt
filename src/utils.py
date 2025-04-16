import nmap

def detailed_port_scan(target, ports="1-1024"):
    """
    Perform a detailed port scan using nmap.
    
    Args:
        target (str): The IP or hostname to scan.
        ports (str): Port range to scan (default is 1-1024).
        
    Returns:
        dict: A dictionary containing open ports and service details.
    """
    scanner = nmap.PortScanner()
    scan_result = {}

    try:
        # Perform scan
        scanner.scan(target, ports, arguments="-sV")
        
        # Parse results
        for host in scanner.all_hosts():
            scan_result[host] = []
            for port in scanner[host]['tcp']:
                port_data = {
                    "port": port,
                    "state": scanner[host]['tcp'][port]['state'],
                    "service": scanner[host]['tcp'][port]['name'],
                    "version": scanner[host]['tcp'][port]['version']
                }
                scan_result[host].append(port_data)
    
    except Exception as e:
        print(f"Error during scanning: {e}")

    return scan_result


def print_scan_results(scan_results):
    """
    Print the results of the nmap scan in a readable format.

    Args:
        scan_results (dict): Scan results from the detailed_port_scan function.
    """
    for host, ports in scan_results.items():
        print(f"\nHost: {host}")
        print("Open Ports:")
        for port_info in ports:
            print(f"  - Port {port_info['port']} ({port_info['service']}): {port_info['state']} ({port_info['version']})")
