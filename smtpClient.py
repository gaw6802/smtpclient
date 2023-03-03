from socket import *


def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope
    # mailserver = "smtp.gmail.com"
    # port = 587

    # Create socket called clientSocket and establish a TCP connection with mailserver and port

    client_Socket = socket(AF_INET, SOCK_STREAM)
    #print("Socket is created")

    client_Socket.connect((mailserver, port))

    recv = client_Socket.recv(1024)

    #recv = client_Socket.recv(1024).decode()
    # print(recv)  # You can use these #print statement to validate return codes from the server.
    # if recv[:3] != '220':
    # print('220 reply not received from server.')

    # Send HELO command and #print server response.
    heloCommand = 'HELO\r\n'
    client_Socket.send(heloCommand.encode())
    recv1 = client_Socket.recv(1024).decode()
    # print(recv1)
    if recv1[:3] != '250':
        print('250 reply not received from server.')

    # Send MAIL FROM command and handle server response.
    # Fill in start
    mail_from_command = 'MAIL FROM:\r\n'
    client_Socket.send(mail_from_command.encode())
    response = client_Socket.recv(1024).decode()
    # print(response)
    # Fill in end

    # Send RCPT TO command and handle server response.
    # Fill in start
    rcpt_to_command = 'RCPT TO:\r\n'
    client_Socket.sendall(rcpt_to_command.encode())
    response = client_Socket.recv(1024).decode()
    # print(response)
    # Fill in end

    # Send DATA command and handle server response.
    # Fill in start
    dataCommand = 'DATA\r\n'
    client_Socket.send(dataCommand.encode())
    recv4 = client_Socket.recv(1024).decode()
    # print (recv4)
    if recv4[:3] != '354':
        print ('354 reply not received from server.')
    # Fill in end

    # Send message data.
    client_Socket.send(msg.encode())

    # Message ends with a single period, send message end and handle server response.
    # Fill in start
    client_Socket.send(endmsg.encode())
    response = client_Socket.recv(1024).decode()
    # print(response)
    # Fill in end

    # Send QUIT command and handle server response.
    # Fill in start
    quit_command = 'QUIT\r\n'
    client_Socket.sendall(quit_command.encode())
    response = client_Socket.recv(1024).decode()
    # print(response)
    # Fill in end

    client_Socket.close()

if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')
