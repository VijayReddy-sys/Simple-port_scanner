import socket

def port_scanner(target, port_range):
    """
    Scans a target host for open ports within a specified range.

    Args:
        target (str): The target host IP address or hostname.
        port_range (tuple): A tuple containing the start and end ports to scan.

    Returns:
        list: A list of open ports on the target host.
    """

    open_ports = []
    for port in range(port_range[0], port_range[1] + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((target, port))
        if result == 0:
            open_ports.append(port)
        sock.close()

    return open_ports

if __name__ == "__main__":
    target = input("Enter target IP address or hostname: ")
    start_port = int(input("Enter starting port: "))
    end_port = int(input("Enter ending port: "))

    open_ports = port_scanner(target, (start_port, end_port))

    if len(open_ports) > 0:
        print("Open ports on", target, ":")
        for port in open_ports:
            print(port)
    else:
        print("No open ports found on", target)