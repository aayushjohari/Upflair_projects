import socket
import time

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Define the IP address and port number
ip_address = "127.0.0.1"
port_no = 2525

# Bind the socket to the IP address and port number
complete_address = (ip_address, port_no)
s.bind(complete_address)
print("hey i m listening")

while True:    # Infinite loop
    Data = s.recvfrom(100)
    message = Data[0]
    message = message.decode('ascii')
    sender_address = Data[1]
    sender_ipaddress = sender_address[0]
    sender_port = sender_address[1]

    # Get the current time
    current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    # Create the filename using the sender's IP address
    filename = f"{sender_ipaddress}.txt"
    
    # Write the message and timestamp to the file
    with open(filename, "a") as file:  
        file.write(f"{message} : Sent at(from sender side) -- {current_time}\n")
        file.flush()

    # Print the received message and sender's IP address
    print(f"Received message: {message} from {sender_ipaddress} at {current_time}")

   
    # response_message = f"Received your message: {message} at {current_time}"
    response_message=input("write your response here: ")
    response_message1= response_message.encode('ascii')

    s.sendto(response_message1,sender_address)

    with open(filename, "a") as file:  
        file.write(f"{response_message} : Sent at(from receiver side) - {current_time}\n")
        file.flush()

   


   
