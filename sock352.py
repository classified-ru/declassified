# this pseudo-code shows an example strategy for implementing
# the CS 352 socket library

import binascii
import socket as syssock
import struct
import sys
import random

MAXPKTSIZE = 64000

#Flags
SOCK352_SYN = 0x01
SOCK352_FIN = 0x02
SOCK352_ACK = 0x04
SOCK352_RESET = 0x08
SOCK352_HAS_OPT = 0xA0

# this init function is global to the class and
# defines the UDP ports all messages are sent
# and received from.

def init(UDPportTx,UDPportRx):
   # initialize your UDP socket here
    #source_port = UDPportTx
    #dest_port = UDPportRx

    if UDPportTx < 0 or UDPportTx > 65535: 
        return -1
    if UDPportRx < 0 or UDPportRx > 65535:     
        return -1
    
    if UDPportTx == 0: 
        UDPportTx = 27182
    if UDPportRx == 0:   
        UDPportRx = 27182
        
    # create a UDP/datagram socket
    s = socket()    

    # bind the port to the Rx (receive) port number     
    s.bind(('', UDPportRx))
    return 1    
    
class socket:
    
    def __init__(self): 
        # create any lists/arrays/hashes you need
        conn_list = []
		self.sysock(syssock.AF_INET, syssock.SOCK_DGRAM)
        return
    
    def bind(self,address): #not needed for part1
        return 
	
    def connect(self,address):  # fill in your code here

        #global source_port  
        # example using a variable global to the Python module
        #  create a new sequence number
        sequence_no = random.randint(0,1000)
        #  also set the other fields (e.g sequence #)
        version = 0x1
        flags = SOCK352_SYN
        opt_ptr = 0
        checksum = 0
        protocol = 0
        source_port = 0
        dest_port = 0
        ack_no = sequence_no + 1
        window = 0
        payload_len = 0

        #  create a new packet header with the SYN bit set in the flags (use the Struct.pack method)
        sock352PktHdrData = '!BBBBHHLLQQLL'
        header_len = struct.calcsize(sock352PktHdrData)
        udpPkt_hdr_data = struct.Struct(sock352PktHdrData)
        header = udpPkt_hdr_data.pack(version, flags, opt_ptr, protocol,
                                       header_len, checksum, source_port, 
                                       dest_port, sequence_no, ack_no, window, 
                                       payload_len)
		
        while True:
            try:
                #   add the packet to the outbound queue
                #   set the timeout
                #      wait for the return SYN
                break
            except timeout:
                continue
                #        if there was a timeout, retransmit the SYN packet 
                #   set the outbound and inbound sequence numbers            
        self.socketconnect(address);
        return 1

    def listen(self,backlog):
        pass #null code for part1
        return

    def accept(self):    #MUST IMPLEMENT TIMEOUT
        (clientsocket, address) = (1,1)  # change this to your code 
        # call  __sock352_get_packet() until we get a new conection
        # check the the connection list - did we see a new SYN packet?
        return (clientsocket,address)
    
    def close(self):   # fill in your code here 
        # send a FIN packet (flags with FIN bit set)
        version = 0x1
        flags = SOCK352_FIN
        opt_ptr = 0
        checksum = 0
        protocol = 0
        source_port = 0
        dest_port = 0
        ack_no = 0
        window = 0
        payload_len = 0

        sock352PktHdrData = '!BBBBHHLLQQLL'
        header_len = struct.calcsize(sock352PktHdrData)
        udpPkt_hdr_data = struct.Struct(sock352PktHdrData)
        header = udpPkt_hdr_data.pack(version, flags, opt_ptr, protocol,
                                       header_len, checksum, source_port, 
                                       dest_port, sequence_no, ack_no, window, 
                                       payload_len)
        
        # remove the connection from the list of connections
        return 

    def send(self,buffer):
        #global UDPportTx  # example using a variable global to the Python module 
        # make sure the correct fields are set in the flags
        # make sure the sequence and acknowlegement numbers are correct
        # create a new sock352 header using the struct.pack
        # create a new UDP packet with the header and buffer 
        # send the UDP packet to the destination and transmit port
        # set the timeout
        # wait or check for the ACK or a timeout
        
        bytessent = 0     # fill in your code here
        while bytessent < len(buffer):
                sent = self.sock.send(buffer[bytessent:])
                if sent == 0:
                        raise RuntimeError("socket connection broken")
                bytessent += sent
        return bytessent

    def recv(self,nbytes):    #MUST IMPLEMENT TIMEOUT
        # call __sock352_get_packet() to get packets (polling)
        # check the list of received fragements
        # copy up to bytes_to_receive into a buffer
        # return the buffer if there is some data
                chunks = []
                bytesreceived = 0     # fill in your code here
                while bytesreceived < nbytes:
                                chunks = self.sock.recv(
                                    min(nbytes - bytesreceived, 2048))
                                if chunk == '':
                                        raise RuntimeError("socket connection broken")
                                chunks.append(chunk)
                                bytesreceived += len(chunks)
                return bytesreceived
    
    # this is an internal function that demultiplexes all incomming packets
    # it update lists and data structures used by other methods
    
    def  __sock352_get_packet(self):
    # There is a differenct action for each packet type, based on the flags:
    #  First check if it's a connection set up (SYN bit set in flags)
    #    Create a new fragment list
    #    Send a SYN packet back with the correct sequence number
    #    Wake up any readers wating for a connection via accept() or return 
    #  else
    #      if it is a connection tear down (FIN) 
    #        send a FIN packet, remove fragment list
    #      else if it is a data packet
    #           check the sequence numbers, add to the list of received fragments
    #           send an ACK packet back with the correct sequence number
    #          else if it's nothing it's a malformed packet.
    #              send a reset (RST) packet with the sequence number
        pass
