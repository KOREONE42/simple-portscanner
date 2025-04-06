
# Port Scanner Script

This is a simple Python script that scans an IP address for open ports within a given range (1 to 65535). The script attempts to connect to each port and reports which ones are open. It uses the `socket` library for networking and `logging` for detailed output.

## Features

- Scans a specified range of ports on a given IP address.
- Logs results for open ports and errors.
- Configurable logging for tracking the scan process.
- Provides real-time feedback on open ports.

## Requirements

- Python 3.x
- `pyfiglet` (for ASCII banner generation)

To install `pyfiglet`, use the following pip command:

```bash
pip install pyfiglet
```

## How to Use

1. **Modify the IP address** in the script (`ip = '192.168.1.6'`) to the target address you wish to scan.

2. **Run the script:**

```bash
python simple_portscan.py
```

3. The script will output the list of open ports on the given IP address or indicate if no ports are open.

## Script Overview

### Functions:

- `probe_port(ip, port)`: Checks if a specific port on the given IP address is open.
- `scan_ports(ip, ports)`: Scans a range of ports and returns a list of open ports.
- `display_open_ports(open_ports)`: Displays the list of open ports.
- `logging`: Configures logging to provide details on the scanning process.

### Logging:

The script logs important actions (such as the start of the scan, open ports, errors) to the console with timestamps.

## Example Output:

```
2025-04-06 12:34:56,123 - INFO - Starting port scan on 192.168.1.6
2025-04-06 12:34:57,234 - INFO - Port 80 is open
2025-04-06 12:34:58,345 - INFO - Port 443 is open
Open Ports are:
[80, 443]
2025-04-06 12:34:59,456 - INFO - Port scan complete
```

## License

This script is provided as-is. Feel free to modify and use it as needed.
