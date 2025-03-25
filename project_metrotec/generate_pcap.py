import scapy.all as scapy


def create_pcap(filename):
    packet1 = scapy.IP(dst="192.168.0.1") / scapy.TCP(dport=80, sport=12345) / scapy.Raw(load="Test packet 1")
    packet2 = scapy.IP(dst="192.168.0.1") / scapy.TCP(dport=80, sport=12345) / scapy.Raw(load="Test packet 2")
    packet3 = scapy.IP(dst="192.168.0.1") / scapy.TCP(dport=80, sport=12345) / scapy.Raw(load="Test packet 1")
    packet4 = scapy.IP(dst="192.168.0.1") / scapy.TCP(dport=80, sport=12345) / scapy.Raw(load="Test packet 3")

    scapy.wrpcap(filename, [packet1, packet2, packet3, packet4])

create_pcap("file1.pcap")
create_pcap("file2.pcap")

print("PCAP файлы успешно созданы!")
