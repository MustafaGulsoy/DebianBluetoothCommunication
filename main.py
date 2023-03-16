import bluetooth

# MAC address of the remote device to connect to
server_mac_address = '00:11:22:33:44:55'

# Port number to use for the Bluetooth connection
port = 1

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
