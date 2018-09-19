#this will forward and show the  packets of local machine
#command before running this program, "iptables -I INPUT -j NFQUEUE --queue-num 0"
#command before running this program, "iptables -I OUTPUT -j NFQUEUE --queue-num 0"

#!usr/bin/env python
import netfilterqueue

def process_packet(packet):
    print(packet)
    #this will forward the all packets
    packet.accept()

queue = netfilterqueue.NetfiltetQueue()
# 0 because we specified 0 queue-num in command, "iptables -I INPUT -j NFQUEUE --queue-num 0"
queue.bind(0,process_packet)
queue.run()