import socket
import os
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip = os.popen("ip -4 route show default").read().split()[8]#socket.gethostbyname(socket.gethostname())#socket.getfqdn()#socket.gethostbyname(socket.gethostname())
port = 5056

print(ip)

s.bind((ip, port))
s.listen(1)
print(f"Connect to port {port} on {ip}")
name = ""
connected = False
while True:
	if(not connected):
		clientsocket, address = s.accept()
		print(f"Connection from {address} has been established!")
		connected = True
		clientsocket.send(bytes("Welcome to the server!","utf-8"))
		
	prompt = clientsocket.recv(1024)
	name = clientsocket.recv(1024).decode("utf-8")
	
	print("Working...")
	os.system("python ImageGen.py "+prompt.decode("utf-8") +" " + name)
	
	if (os.path.isfile(f"./processed_images/{name}.png")):
		try:
			with open(f"./processed_images/{name}.png", "rb") as file:
				size = 2048
				image_data = file.read(size)
				while image_data:
					clientsocket.send(image_data)
					image_data = file.read(size)
				file.close()
				clientsocket.close()
				connected = False
			print("Image sent sucessfully")
			
		except Exception as e:
			print(f"Error sending Image: {e}")
			s.close()
		finally:
			name=""
		
