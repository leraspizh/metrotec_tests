import unittest
from io import BytesIO
import scapy.all as scapy
from find_matching_intervals import find_matching_intervals


class TestFindMatchingIntervals(unittest.TestCase):

    def setUp(self):
        """Создаем фиктивные pcap файлы"""
        # Пакеты для теста
        self.packet1 = scapy.IP(dst="192.168.0.1") / scapy.TCP(dport=80, sport=12345) / scapy.Raw(load="Test packet 1")
        self.packet2 = scapy.IP(dst="192.168.0.1") / scapy.TCP(dport=80, sport=12345) / scapy.Raw(load="Test packet 2")
        self.packet3 = scapy.IP(dst="192.168.0.1") / scapy.TCP(dport=80, sport=12345) / scapy.Raw(load="Test packet 1")
        self.packet4 = scapy.IP(dst="192.168.0.1") / scapy.TCP(dport=80, sport=12345) / scapy.Raw(load="Test packet 3")

        # Создаем pcap файлы
        self.pcap1 = BytesIO()
        self.pcap2 = BytesIO()
        scapy.wrpcap(self.pcap1, [self.packet1, self.packet2, self.packet3])
        scapy.wrpcap(self.pcap2, [self.packet3, self.packet4, self.packet1])

        self.pcap1.seek(0)
        self.pcap2.seek(0)

    def test_find_matching_intervals(self):
        """Тестируем нахождение совпадающих интервалов"""
        pcap1 = scapy.rdpcap(self.pcap1)
        pcap2 = scapy.rdpcap(self.pcap2)

        matches = find_matching_intervals(pcap1, pcap2, min_matching_packets=2)

        # Проверка на количество совпадающих интервалов
        self.assertEqual(len(matches), 1)
        # Проверка на количество совпавших пакетов в интервале
        self.assertEqual(matches[0][0], 2)
        # Проверка на правильность пакетов
        self.assertEqual(matches[0][1][0], (2, self.packet3.time))
        self.assertEqual(matches[0][1][1], (0, self.packet1.time))


if __name__ == "__main__":
    unittest.main()
