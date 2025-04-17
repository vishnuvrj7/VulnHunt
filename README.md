# VulnHunt - Vulnerability Scanner

![Security Scanner](https://img.shields.io/badge/Security-Scanner-red)
![Python 3.7+](https://img.shields.io/badge/Python-3.7+-blue)
![License MIT](https://img.shields.io/badge/License-MIT-yellow)

VulnHunt is an advanced vulnerability scanner designed to identify and analyze potential security vulnerabilities in target systems. It offers features such as detailed port scanning, service banner grabbing, HTTP header analysis, and integration with the Vulners API for vulnerability detection.

## 🔍 Features

- **Port Scanning**: Scan specified port ranges to identify open ports.
- **Service Banner Grabbing**: Detect running services and versions (e.g., HTTP, FTP, SSH).
- **HTTP Headers Analysis**: Fetch and analyze HTTP response headers for common security issues.
- **Vulnerability Detection**: Integration with the Vulners API for analyzing services and reporting potential vulnerabilities.
- **Progress Bar**: Displays a real-time progress bar with an estimated time to complete the scan.
- **Secure Configuration**: API keys are securely managed using an .env file.

## 📋 Prerequisites

Before running VulnHunt, ensure the following:

- Python 3.7 or higher
- pip (Python's package manager)

### Install Python 3.7 or Higher

Download and install Python from the official website:

- [Download Python](https://www.python.org/downloads/)

Confirm Python installation:

```bash
python --version
```

## 🔧 Installation

Follow these steps to install and configure VulnHunt:

### 1. Clone the Repository

Clone the VulnHunt repository:

```bash
git clone https://github.com/vishnuvrj7/VulnHunt.git
```

Navigate to the VulnHunt directory:

```bash
cd VulnHunt
```

### 2. Install Dependencies

Install the required Python libraries:

```bash
pip install -r requirements.txt
```

Dependencies include:
- **python-nmap**: For port scanning and banner grabbing
- **requests**: For HTTP requests
- **colorama**: For colored console output
- **tqdm**: For progress bar
- **python-dotenv**: For managing environment variables
- **vulners**: For vulnerability analysis

### 3. Configure the .env File

To use the Vulners API, you need to generate your own API key:

Sign up for Vulners:

Visit [Vulners](https://vulners.com/docs) and create an account.

Once logged in, navigate to the API section and generate an API key.


In the root directory of this project, create a file named .env.

Add the following line to the .env file:

```env
VULNERS_API_KEY=your_api_key_here
```


## 🚀 Usage

### 1. Run the Scanner

Run the scanner using:

```bash
python scanner.py
```

### 2. Input Parameters

You'll be prompted to provide the following:

- **Target**: Domain or IP address (e.g., example.com or 192.168.1.1)
- **Port Range**: Range of ports to scan (default is 1-1024)

Example prompt:

```
Enter the target IP or hostname: localhost
Enter the port range (default is 1-1024): 80-443
```

### 3. Output

The scanner will display:

- Open ports and their services (e.g., HTTP, FTP)
- Detailed vulnerability analysis (if vulnerabilities are found)

Progress is shown using a real-time progress bar with an estimated time to complete.

Example output:

```
Scanning Ports: 100%|███████████████████████████████████████| 1024/1024 [08:44<00:00,  1.95it/s]

Scan Completed! Results:
Port 135: epmap
    Vulnerabilities:
    - CVE-2004-0716
    - Service Detection (FIND_SERVICE2.NASL)

Port 445: microsoft-ds
    Vulnerabilities:
    - CVE-2002-0597
    - MS08-068 Microsoft Windows SMB Relay Code Execution
```


## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature-name`)
3. Commit your changes (`git commit -am 'Add feature'`)
4. Push to the branch (`git push origin feature-name`)
5. Submit a pull request

## 📜 License

This project is licensed under the MIT License. See the LICENSE file for details.

## 👏 Acknowledgements

- **python-nmap**: For port scanning and banner grabbing
- **requests**: For HTTP requests
- **colorama**: For terminal color formatting
- **tqdm**: For progress bar
- **vulners**: For vulnerability analysis
- **python-dotenv**: For environment variable management

---

**Disclaimer**: VulnHunt is intended for educational and ethical purposes. Always obtain proper authorization before scanning systems. Misuse of this tool may violate laws and ethical guidelines. Use responsibly!