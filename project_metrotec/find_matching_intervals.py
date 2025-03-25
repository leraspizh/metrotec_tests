import argparse
import scapy.all as scapy
from collections import deque


def load_pcap(file_path):
    """Загружает pcap файл и возвращает список пакетов"""
    return scapy.rdpcap(file_path)


def find_matching_intervals(pcap1, pcap2, min_matching_packets=2):
    """Ищет интервалы с совпадающими пакетами между двумя pcap файлами"""
    matches = []
    pcap2_queue = deque(pcap2)

    for i, packet1 in enumerate(pcap1):
        matching_count = 0
        matching_packets = []

        # Пробегаемся по пакету из pcap2
        for packet2 in pcap2_queue:
            if packet1 == packet2:  # Совпадение пакетов
                matching_count += 1
                matching_packets.append((i, packet1.time))
                pcap2_queue.popleft()  # Убираем совпавший пакет из очереди
                if matching_count >= min_matching_packets:
                    break

        if matching_count >= min_matching_packets:
            matches.append((matching_count, matching_packets))

    return matches


def print_matching_intervals(matches, interval_numbers=None):
    """Выводит интервалы с совпадающими пакетами и соответствующую информацию"""
    if interval_numbers is None:
        interval_numbers = range(1, len(matches) + 1)

    for idx, (count, packets) in zip(interval_numbers, matches):
        print(f"Интервал {idx}: {count} совпавших пакетов")
        for i, (packet_index, timestamp) in enumerate(packets):
            print(f"\tПакет {i + 1}: Позиция в pcap1 - {packet_index}, Временная метка - {timestamp}")


def main():
    parser = argparse.ArgumentParser(description="Найти совпадающие интервалы пакетов в pcap файлах")
    parser.add_argument('file1', help='Путь до первого pcap файла')
    parser.add_argument('file2', help='Путь до второго pcap файла')
    parser.add_argument('--min-packets', type=int, default=2, help='Минимальное количество совпадающих пакетов')
    parser.add_argument('--intervals', type=int, nargs='*', help='Номера совпадающих интервалов для отображения')

    args = parser.parse_args()

    # Загружаем pcap файлы
    pcap1 = load_pcap(args.file1)
    pcap2 = load_pcap(args.file2)

    # Ищем совпадающие интервалы
    matches = find_matching_intervals(pcap1, pcap2, args.min_packets)

    # Выводим результаты
    print_matching_intervals(matches, args.intervals)


if __name__ == "__main__":
    main()
