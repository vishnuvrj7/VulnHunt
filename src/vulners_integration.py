import os
from dotenv import load_dotenv
from vulners import Vulners

# Load environment variables
load_dotenv()

def analyze_vulnerabilities(service_name):
    api_key = os.getenv("VULNERS_API_KEY")
    if not api_key:
        raise ValueError("Vulners API Key is missing. Please set it in the .env file.")

    try:
        vulners = Vulners(api_key=api_key)
        query = service_name.lower()
        print(f"Analyzing vulnerabilities for {service_name}...")
        
        # Updated to use VulnersApi.find_all()
        results = vulners.find_all(query)
        return results
    except Exception as e:
        print(f"Error fetching vulnerabilities for {service_name}: {e}")
        return None
