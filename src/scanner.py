import socket
from utils import detailed_port_scan, print_scan_results

def display_banner():
    banner = r"""
    ██    ██ ██    ██ ██      ███    ██ ██   ██ ██    ██ ███    ██ ████████ 
    ██    ██ ██    ██ ██      ████   ██ ██   ██ ██    ██ ████   ██    ██    
    ██    ██ ██    ██ ██      ██ ██  ██ ███████ ██    ██ ██ ██  ██    ██    
     ██  ██  ██    ██ ██      ██  ██ ██ ██   ██ ██    ██ ██  ██ ██    ██    
      ████    ██████  ███████ ██   ████ ██   ██  ██████  ██   ████    ██    

                            ~ VRJ ~                          
    """
    print(banner)

def validate_target(target):
    """
    Validate if the target is reachable.
    """
    try:
        socket.gethostbyname(target)
        return True
    except socket.error:
        return False

def integrate_with_vuln_db(port_results):
    """
    Optionally integrate with a vulnerability database for further analysis.
    Example uses a mock vulnerability database.
    """
    vuln_db = {
        21: "FTP: Potential Anonymous Login Vulnerability",
        22: "SSH: Default Credentials",
        80: "HTTP: Outdated Server Version",
        443: "HTTPS: Weak Cipher Suites"
    }
    
    analysis = []
    for port, service in port_results.items():
        if port in vuln_db:
            analysis.append(f"Port {port} ({service}): {vuln_db[port]}")
    return analysis

def main():
    target = input("Enter the target IP or hostname: ")
    ports = input("Enter the port range (default is 1-1024): ") or "1-1024"
    
    if not validate_target(target):
        print(f"\nError: Target '{target}' is unreachable. Please check the hostname or IP.")
        return
    
    print("\nStarting detailed port scan...")
    try:
        results = detailed_port_scan(target, ports)
        print("\nScan Completed! Results:")
        print_scan_results(results)
        
        # Optional Vulnerability Database Integration
        print("\nAnalyzing results against vulnerability database...")
        vuln_analysis = integrate_with_vuln_db(results)
        if vuln_analysis:
            print("\nPotential Vulnerabilities Found:")
            for item in vuln_analysis:
                print(f"- {item}")
        else:
            print("\nNo known vulnerabilities found for the scanned services.")
    except Exception as e:
        print(f"\nAn error occurred during scanning: {e}")

if __name__ == "__main__":
    display_banner()
    main()
