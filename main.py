import bluetooth

# MAC address of the remote device to connect to
server_mac_address = '28:bd:89:bd:1b:b6'

# Port number to use for the Bluetooth connection
port = 8
# tinker içinde 10 olmalı

# Create a Bluetooth socket and connect to the remote device
sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.connect((server_mac_address, port))

# Send data to the remote device
sock.send('Hello, World!')

# Receive data from the remote device
data = sock.recv(1024)
print('Received:', data)

# Close the Bluetooth socket
sock.close()
