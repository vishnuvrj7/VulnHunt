# VulnHunt - Vulnerability Scanner

![VulnHunt Logo](https://img.shields.io/badge/VulnHunt-Security%20Scanner-red)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)

**VulnHunt** is an advanced vulnerability scanner that helps identify and assess potential security vulnerabilities in target systems. It provides detailed information about open ports, services, HTTP headers, and banners to aid in security analysis.

## 🔍 Features

- **Port Scanning**: Scan a specified range of ports to identify open ports on a target
- **Service Banner Grabbing**: Detect the services and versions running on open ports (e.g., HTTP, FTP, SSH)
- **HTTP Headers Analysis**: Fetch HTTP response headers and analyze them for common security issues
- **Progress Bar**: Displays a progress bar for scan tasks, with an estimate of time to complete
- **Scan Report**: Generates a detailed report on potential vulnerabilities based on the findings

## 📋 Prerequisites

Before running **VulnHunt**, you need to have the following installed:

- **Python 3.7** or higher
- **pip** (Python's package manager)

### Install Python 3.7 or Higher

You can download and install Python from the official website:

- [Download Python](https://www.python.org/downloads/)

Once installed, confirm Python is available by running:

```bash
python --version
```

## 🔧 Installation

Follow these steps to get VulnHunt up and running:

### 1. Clone the Repository

First, clone the VulnHunt repository to your local machine using Git:

```bash
git clone https://github.com/yourusername/VulnHunt.git
```

This will create a folder named `VulnHunt` with the code in it.

### 2. Install Dependencies

Navigate to the VulnHunt directory:

```bash
cd VulnHunt
```

Install the required Python libraries by using the requirements.txt file:

```bash
pip install -r requirements.txt
```

This command will install all the necessary dependencies for VulnHunt, including:

- **python-nmap**: For performing detailed port scans and banner grabbing
- **requests**: For HTTP requests and fetching HTTP headers
- **colorama**: For adding color to console output
- **tqdm**: For displaying a progress bar during the scan

### 3. Set Up the Configuration (Optional)

You may need to customize certain configurations like the scan range or timeout settings. These can typically be adjusted directly within the code if necessary.

If you need any specific configurations, look into the `config.py` file or edit the default parameters in `scanner.py`.

## 🚀 Usage

### 1. Run the Vulnerability Scanner

To start the vulnerability scan, run the following command:

```bash
python scanner.py
```

### 2. Scan Settings

Upon running the scanner, you'll be prompted to enter the following details:

- **Target**: The domain or IP address of the target you want to scan (e.g., example.com or 192.168.1.1)
- **Port Range**: Specify the range of ports you want to scan. The default is 1-1024, but you can choose a custom range (e.g., 80-443 for HTTP and HTTPS)
- **HTTP Headers Analysis**: Choose whether you want the scanner to fetch and analyze HTTP headers (enter y or n)
- **Scan Level**: You can set the intensity of the scan (e.g., a broader range or more detailed scans)

Here's an example of how the prompt might look:

```
Enter target IP/domain: example.com
Enter port range (default 1-1024): 80-443
Enable HTTP header analysis (y/n): y
```

### 3. Output and Results

Once the scan completes, VulnHunt will provide detailed output, including:

- A list of open ports and the services running on them (HTTP, FTP, SSH, etc.)
- HTTP header information (if selected)
- Potential vulnerabilities based on service versions and security configurations

The scanner also shows a progress bar that updates in real-time as the scan progresses, along with an estimated time to complete.

Example output:

```
[+] Scanning 192.168.1.1 on ports 80-443
[+] Open Port: 80 (HTTP)
    - Service: Apache 2.4.41
    - Banner: Apache/2.4.41 (Unix)
[+] HTTP Headers Analysis:
    - X-Content-Type-Options: nosniff
    - Strict-Transport-Security: max-age=31536000; includeSubDomains
    ...
```

### 4. Generating Reports

You can also generate a detailed report after a scan is completed. The report will include information such as:

- Detected open ports
- Banner information
- HTTP headers analysis results
- Potential vulnerabilities

Example:
```
python scanner.py
# Enter target IP/domain: example.com
# Enter port range (default 1-1024): 80-443
# Enable HTTP header analysis (y/n): y
```

## 🤝 Contributing

We welcome contributions to VulnHunt! If you would like to add a feature, improve documentation, or fix a bug, follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature-name`)
3. Commit your changes (`git commit -am 'Add feature'`)
4. Push to the branch (`git push origin feature-name`)
5. Create a pull request

We'll review your changes and merge them into the main project.

## 📜 License

VulnHunt is licensed under the MIT License. See the LICENSE file for more details.

## 👏 Acknowledgements

- **python-nmap**: Port scanning and service detection library
- **requests**: HTTP requests library
- **colorama**: Library for colored terminal output
- **tqdm**: Library for progress bars

---

**Note**: VulnHunt is a tool for ethical hackers, penetration testers, and anyone interested in learning about vulnerabilities in web applications and networks. Use it responsibly, and always get permission before scanning any systems.