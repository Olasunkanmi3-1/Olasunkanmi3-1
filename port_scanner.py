import socket
import threading
import argparse

# Function to scan a single port
def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"[+] Port {port} is open")
        sock.close()
    except Exception as e:
        print(f"[-] Error scanning port {port}: {e}")

# Function to scan a range of ports
def run_scanner(ip, start_port, end_port):
    threads = []
    for port in range(start_port, end_port + 1):
        t = threading.Thread(target=scan_port, args=(ip, port))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()

# Parse command-line arguments
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple Python Port Scanner")
    parser.add_argument("-t", "--target", required=True, help="Target IP address")
    parser.add_argument("-p", "--ports", required=True, help="Port range (e.g., 1-100)")
    args = parser.parse_args()

    ip = args.target
    port_range = args.ports.split("-")
    start_port = int(port_range[0])
    end_port = int(port_range[1])

    print(f"[*] Scanning {ip} from port {start_port} to {end_port}...")
    run_scanner(ip, start_port, end_port)
