import requests
import socket
import json


# Create a TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_address = ('localhost', 8000)
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(1)

print('Server is running and listening for connections...')

while True:
    # Wait for a client connection
    client_socket, client_address = server_socket.accept()
    print(f'Client connected: {client_address}')

    try:
        # Receive data from the client
        data = client_socket.recv(1024)
        if data:
            # Parse the received JSON data
            received_data = json.loads(data.decode('utf-8'))
            print('Received JSON data:')
            url = "http://api.rnd.co.ke/comment"
            payload = json.dumps({"comment": received_data['comment']})
            headers = { 'Content-Type': 'application/json'}
            response = requests.request("POST", url, headers=headers, data=payload)
            response = "Account successfully created"
            
            
              
            

            # Process the received JSON data
            # ...

    except Exception as e:
        print(f'Error occurred: {str(e)}')

    finally:
        # Close the client socket
        client_socket.close()
