import serial.tools.list_ports

def find_scanner():

    ports = serial.tools.list_ports.comports()

    for port in ports:
        if "USB" in port.description or "UART" in port.description:
            return port.device

    return None