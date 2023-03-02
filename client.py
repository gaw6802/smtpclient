import socket

def send_email(sender_email, receiver_email, message):
    SERVER_HOST = '127.0.0.1'
    SERVER_PORT = 1025

    # Create a socket object and connect to the server
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect(SERVER_HOST, SERVER_PORT)

        # Receive the server's greeting messagef
        greeting_message = client_socket.recv(1024).decode()
        print(greeting_message)

        # Send the HELO command
        helo_command = 'HELO server\r\n'
        client_socket.send(helo_command.encode())
        response = client_socket.recv(1024).decode()
        print(response)

        # Send the STARTTLS command
        starttls_command = 'STARTTLS\r\n'
        client_socket.send(starttls_command.encode())
        response = client_socket.recv(1024).decode()
        print(response)

        # Start TLS encryption
        client_socket = socket.ssl(client_socket)

        # Send the AUTH LOGIN command
        auth_command = 'AUTH LOGIN\r\n'
        client_socket.write(auth_command.encode())
        response = client_socket.read(1024).decode()
        print(response)

        # Send the username and password
        username = sender_email.encode() + '\r\n'.encode()
        client_socket.write(username)
        response = client_socket.read(1024).decode()
        print(response)

        password = 'your_password_here'.encode() + '\r\n'.encode()
        client_socket.write(password)
        response = client_socket.read(1024).decode()
        print(response)

        # Send the MAIL FROM command
        mail_from_command = 'MAIL FROM:<{sender_email}>\r\n'
        client_socket.write(mail_from_command.encode())
        response = client_socket.read(1024).decode()
        print(response)

        # Send the RCPT TO command
        rcpt_to_command = 'RCPT TO:<{receiver_email}>\r\n'
        client_socket.write(rcpt_to_command.encode())
        response = client_socket.read(1024).decode()
        print(response)

        # Send the DATA command
        data_command = 'DATA\r\n'
        client_socket.write(data_command.encode())
        response = client_socket.read(1024).decode()
        print(response)

        # Send the email message
        client_socket.write(message.encode())
        response = client_socket.read(1024).decode()
        print(response)

        # Send the QUIT command
        quit_command = 'QUIT\r\n'
        client_socket.write(quit_command.encode())
        response = client_socket.read(1024).decode()
        print(response)

sender_email = 'sender@example.com'
receiver_email = 'receiver@example.com'
message = """\
Subject: Hello from Python SMTP

This is a test email sent using Python SMTP."""



