#This will convert netfilter packet into scapy packets
#command before running this program, "iptables -I INPUT -j NFQUEUE --queue-num 0"

#!usr/bin/env python
import netfilterqueue

def process_packet(packet):
    scapy_packet = scapy.IP(packet.get_payload())
    print(scapy_packet.show())
    #this will forward the all packets
    packet.accept()

queue = netfilterqueue.NetfiltetQueue()
# 0 because we specified 0 queue-num in command, "iptables -I INPUT -j NFQUEUE --queue-num 0"
queue.bind(0,process_packet)
queue.run()