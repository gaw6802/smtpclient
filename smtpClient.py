from socket import *


def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope
    # mailserver = "smtp.gmail.com"
    # port = 587

    # Create socket called clientSocket and establish a TCP connection with mailserver and port

    clientSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    clientSocket.connect((mailserver, port))
    #recv = clientSocket.recv(1024)

    recv = clientSocket.recv(1024).decode()
    # print(recv) # You can use these print statement to validate return codes from the server.
    # if recv[:3] != '220':
    #    print('220 reply not received from server.')

    # Send HELO command and print server response.
    #heloCommand = 'Helo'
    #clientSocket.send(heloCommand.encode())
    #recv1 = clientSocket.recv(1024).decode()
    #print(recv1)
    #if recv1[:3] != '250':
     #   print('250 reply not received from server.')

    # Send MAIL FROM command and handle server response.
    # Fill in start
    mailFromCommand = ""
    # Fill in end

    # Send RCPT TO command and handle server response.
    # Fill in start
    # Fill in end

    # Send DATA command and handle server response.
    # Fill in start
    dataCommand = 'DATA\r\n'
    clientSocket.write(dataCommand)
    recv4 = clientSocket.read(1024)
    print (recv4)
    if recv4[:3] != '354':
        print ('354 reply not received from server.')
    # Fill in end

    # Send message data.
    ssl_clientSocket.write(msg)

    # Message ends with a single period, send message end and handle server response.
    # Fill in start
    # Fill in end

    # Send QUIT command and handle server response.
    # Fill in start

    clientSocket.close()
    # Fill in end


#if __name__ == '__main__':
#  smtp_client(1025, '127.0.0.1')