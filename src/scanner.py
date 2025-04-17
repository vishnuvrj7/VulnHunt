from utils import detailed_port_scan, print_scan_results
from vulners_integration import analyze_vulnerabilities
import time

def display_banner():
    banner = r"""
    ██    ██ ██    ██ ██      ███    ██ ██   ██ ██    ██ ███    ██ ████████ 
    ██    ██ ██    ██ ██      ████   ██ ██   ██ ██    ██ ████   ██    ██    
    ██    ██ ██    ██ ██      ██ ██  ██ ███████ ██    ██ ██ ██  ██    ██    
     ██  ██  ██    ██ ██      ██  ██ ██ ██   ██ ██    ██ ██  ██ ██    ██    
      ████    ██████  ███████ ██   ████ ██   ██  ██████  ██   ████    ██    

                            ~ VulnHunt ~                          
    """
    print(banner)

def main():
    display_banner()

    target = input("Enter the target IP or hostname: ")
    ports = input("Enter the port range (default is 1-1024): ") or "1-1024"

    print("\nStarting detailed port scan...")
    start_time = time.time()
    results = detailed_port_scan(target, ports)
    end_time = time.time()

    print("\nScan Completed! Results:")
    print_scan_results(results)

    print("\nAnalyzing vulnerabilities using Vulners API...")
    for port, service in results.items():
        vulnerabilities = analyze_vulnerabilities(service)
        if vulnerabilities:
            print(f"\nVulnerabilities for {service} on port {port}:")
            for vuln in vulnerabilities[:5]:  # Display top 5 results
                print(f"- {vuln.get('title', 'No title')} ({vuln.get('id', 'No ID')})")
        else:
            print(f"Could not fetch vulnerabilities for {service} on port {port}.")

    total_time = end_time - start_time
    print(f"\nTotal Scan Time: {total_time:.2f} seconds")

if __name__ == "__main__":
    main()
