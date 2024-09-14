#Network Packet Analyzer
import scapy.all as scapy

def sniff_packets(packet):
    if packet.haslayer(scapy.IP):
        src_ip = packet[scapy.IP].src
        dst_ip = packet[scapy.IP].dst


        if packet.haslayer(scapy.Raw):
            payload = packet[scapy.Raw].load
        else:
            payload = None

        print(f"Packet from {src_ip} to {dst_ip}")

        if payload:
            print(f"Payload: {payload}")
	        

            with open("captured_packets.txt", "a") as f:
                f.write(f"Packet from {src_ip} to {dst_ip}\n")
                if payload:
                    f.write(f"Payload: {payload}\n")
                f.write("\n")


print("Packet sniffing started...")


try:
    scapy.sniff(iface="eth0", store=False, prn=sniff_packets)
except KeyboardInterrupt:
    print("Packets sniffing stopped")
