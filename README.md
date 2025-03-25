# pcap Matching Interval Finder

Этот проект представляет собой утилиту для поиска совпадающих интервалов пакетов между двумя pcap файлами. Она работает с данными захвата сети, ищет последовательности совпадающих пакетов и выводит информацию о совпавших интервалах.

## Установка

1. Установите зависимости:
    ```bash
    pip install -r requirements.txt
    ```

2. Для создания pcap файлов:
    ```bash
    python generate_pcap.py
    ```

3. Для поиска совпадающих интервалов:
    ```bash
    python find_matching_intervals.py file1.pcap file2.pcap --min-packets 3 --intervals 1 2
    ```

4. Для запуска тестов:
    ```bash
    python -m unittest test_find_matching_intervals.py
    ```

## Описание

### Файлы

- **generate_pcap.py** - Генерация тестовых pcap файлов.
- **find_matching_intervals.py** - Поиск совпадающих интервалов пакетов в двух pcap файлах.
- **test_find_matching_intervals.py** - Тесты для функции поиска совпадений.

### Параметры

- `--min-packets` (по умолчанию 2) — Минимальное количество совпадающих пакетов в интервале.
- `--intervals` — Номера интервалов для отображения (если не указаны, выводятся все интервалы).

## Пример

1. Генерация pcap файлов:
    ```bash
    python generate_pcap.py
    ```

2. Поиск совпадающих интервалов с минимум 3 совпавшими пакетами:
    ```bash
    python find_matching_intervals.py file1.pcap file2.pcap --min-packets 3 --intervals 1 2
    ```

3. Запуск тестов:
    ```bash
    python -m unittest test_find_matching_intervals.py
    ```

## Тестирование

Проект использует `unittest` для тестирования. Для запуска тестов используйте команду:

```bash
python -m unittest test_find_matching_intervals.py
