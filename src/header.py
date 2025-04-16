import requests

def check_http_headers(url):
    print(f"Checking HTTP headers for {url}...")
    try:
        response = requests.get(url, timeout=5)
        headers = response.headers
        missing_headers = []
        
        required_headers = [
            "X-Content-Type-Options", 
            "Strict-Transport-Security", 
            "Content-Security-Policy"
        ]
        
        for header in required_headers:
            if header not in headers:
                missing_headers.append(header)
        
        if missing_headers:
            print(f"Missing headers: {missing_headers}")
        else:
            print("All recommended headers are present.")
    
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    target_url = input("Enter target URL (e.g., http://example.com): ")
    check_http_headers(target_url)
