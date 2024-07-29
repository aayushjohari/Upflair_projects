import socket
import time

#socket.AF_INET ---> THROUGH THE INTERNET
#SOCKET.SOCK_DGRAM --> PROTOCOL

s= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
target_ip= "127.0.0.1"

target_port=2525

target_address = (target_ip,target_port)

condition=True
while condition:
 message= input("pls enter your message : ")
 message_encrypted = message.encode('ascii')

 s.sendto(message_encrypted , target_address)
 print("your message is sent....")

 current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
 
 filename = f"{target_ip}.txt"
    
    # Write the message and timestamp to the file
 with open(filename, "a") as file:  
   file.write(f"{message} : Received at(receiver's side)-- {current_time}\n")
   file.flush()


 response , server_address = s.recvfrom(100)
 response = response.decode('ascii')
 

 print(f"Received response: {response} from {server_address} at {current_time}")

 with open(filename, "a") as file:  
     file.write(f"{response} : Received at(sender's side) - {current_time}\n")
     file.flush()


 permission = input("Do you want to continue ? Press: (Y/N) : ")

 if permission.upper() == 'N':
  condition = False

s.close()