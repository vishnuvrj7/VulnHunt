from utils import detailed_port_scan, print_scan_results

def main():
    target = input("Enter the target IP or hostname: ")
    ports = input("Enter the port range (default is 1-1024): ") or "1-1024"
    
    print("\nStarting detailed port scan...")
    results = detailed_port_scan(target, ports)
    
    print("\nScan Completed! Results:")
    print_scan_results(results)


if __name__ == "__main__":
    main()
