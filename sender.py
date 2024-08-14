import socket 

# socket.SOCK_DGRAM --> protocal (UDP/TCP)
sck = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
target_ip = '127.0.0.1'
target_port = 6969
target_address = (target_ip,target_port)

condition = True
while condition:
    message = input("Enter your message here  :")
    message_encrypted = message.encode("ascii")
    sck.sendto(message_encrypted , target_address)
    print("YOUR message is sent....")

    permission = input("Do u want to quit the program ? press(Y/N) :")
    if permission =='Y' or permission =='y':
     condition = False