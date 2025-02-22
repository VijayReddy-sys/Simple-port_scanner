# Simple Port Scanner

## Description
This is a simple Python-based port scanner that scans a target host for open ports within a specified range. It uses Python's `socket` module to check whether a port is open or closed.

## Features
- Scans a target IP address or hostname
- Allows specifying a custom port range
- Identifies open ports

## Prerequisites
Ensure you have Python installed on your system. This script is compatible with Python 3.

## Installation
1. Clone the repository or download the script:
   ```bash
   git clone https://github.com/yourusername/port-scanner.git
   cd port-scanner
   ```
2. Ensure Python is installed:
   ```bash
   python --version
   ```

## Usage
Run the script using Python:
```bash
python port_scanner.py
```
Then, enter the target IP/hostname and port range when prompted.

## Example
```
Enter target IP address or hostname: 192.168.1.1
Enter starting port: 20
Enter ending port: 100
Open ports on 192.168.1.1 :
22
80
```

## Notes
- Running the script against external networks without permission may violate laws and regulations.
- Scanning a large range of ports may take longer.

## License
This project is licensed under the MIT License.

