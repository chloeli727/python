#import socket module
from socket import *
import sys
import time

#Get host and port
host = str(sys.argv[1])
port = int(sys.argv[2])

# Create a UDP socket 
clientSocket = socket(AF_INET, SOCK_DGRAM)

# send 100 pings
for i in range(1, 101):
	#clientSocket = socket(AF_INET, SOCK_DGRAM)
	#start time
	start_time = time.time()
	
	# send message
	message = 'ping ' + str(i) + ' ' + str(time.strftime('%a %b %d %H:%M:%S %Y'))
	clientSocket.sendto(message, (host, port))
	
	reply, addr = clientSocket.recvfrom(1024)
	
	if(reply == 'd'):
		while(reply == 'd'):
			start_time = time.time()
			message = 'ping ' + str(i) + ' ' + str(time.strftime('%a %b %d %H:%M:%S %Y'))
			clientSocket.sendto(message, (host, port))
			reply, addr = clientSocket.recvfrom(1024)
			if(reply == 'd'):
				print(str(i) + ' Dropped, resend the message')
			else:
			#calculate RTT
				rec_time = time.time() #receive time
				rtt = rec_time - start_time #rtt
				print(reply)
				print('RTT: ' + str(rtt) + ' seconds\n')
				
	else:
		rec_time = time.time() #receive time
		rtt = rec_time - start_time #rtt
		print(reply)
		print('RTT: ' + str(rtt) + ' seconds\n')
	

clientSocket.close()
sys.exit()
