import sys
import socket
import logging
import pyfiglet

# IP address to scan
ip = '192.168.1.6'

# List to store open ports
open_ports = []

# Range of ports to scan (from 1 to 65535)
ports = range(1, 65535)

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def probe_port(ip, port, result=1):
    """
    Probes a single port on the given IP address to check if it is open.

    Args:
        ip (str): The IP address to scan.
        port (int): The port to check for openness.
        result (int): Default is 1, which indicates a closed port. If the port is open, result is set to 0.

    Returns:
        int: 0 if the port is open, otherwise returns 1.
    """
    try:
        # Create a socket object
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Set the timeout to 0.5 seconds for faster response
        sock.settimeout(0.5)
        
        # Try to connect to the given port
        r = sock.connect_ex((ip, port))
        
        # If connection is successful, mark the port as open
        if r == 0:
            result = r
            
        # Close the socket after the connection attempt
        sock.close()
    
    except Exception as e:
        # Log any exception that occurs during the socket connection
        logger.error(f"Error probing port {port}: {e}")
    
    return result

def scan_ports(ip, ports):
    """
    Scans a range of ports on the given IP address and identifies open ports.

    Args:
        ip (str): The IP address to scan.
        ports (range): The range of ports to scan.

    Returns:
        list: A list of open ports.
    """
    open_ports = []

    # Iterate over the given ports and probe each one
    for port in ports:
        # Flush the standard output buffer to show live results
        sys.stdout.flush()

        # Check if the port is open
        response = probe_port(ip, port)
        
        if response == 0:  # Port is open
            open_ports.append(port)
            # Log that the port is open
            logger.info(f"Port {port} is open")
    
    return open_ports

def display_open_ports(open_ports):
    """
    Displays the list of open ports.

    Args:
        open_ports (list): A list of open ports.
    """
    if open_ports:
        logger.info("Open Ports are:")
        print("Open Ports are: ")
        print(sorted(open_ports))  # Sort and print the list of open ports
    else:
        logger.info("No open ports found")
        print("Looks like no ports are open :(")

# Run the port scan and display the results
logger.info(f"Starting port scan on {ip}")
open_ports = scan_ports(ip, ports)
display_open_ports(open_ports)
logger.info("Port scan complete")
