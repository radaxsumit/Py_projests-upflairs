import socket 
from datetime import datetime

# socket.SOCK_DGRAM --> protocal (UDP/TCP)
sck = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
ip_addresh = "127.0.0.1"
port_number =6969

#the range of fiven port number is "0 to 65353"  but "0 to 1023" are reserved prot number we can't use them
complete_address=(ip_addresh , port_number)
sck.bind(complete_address)
print("Typing....")

while True:
    Data = sck.recvfrom(1000)
    Message = Data[0].decode('ascii')
    sender_ip_address = Data[1][0]

    with open(sender_ip_address + '.txt' , 'w') as file:
        present_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S') #combining the message with current date & time
        Message_with_datetime = f"your current date & time is : {present_datetime} : your message is : {Message}"
        file.write(Message_with_datetime)
        file.write("\n")
        print(Message) 
        
print(Data)