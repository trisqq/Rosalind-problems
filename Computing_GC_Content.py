def calculate_gc(sequence: str) -> float:
    """Считает процент оснований G и C в переданной строке.

    Args:
        sequence: строка ДНК, состоящая из символов A, C, G, T.

    Returns:
        Процент оснований G и C. Для пустой строки возвращает 0.0.
    """
    if not sequence:
        return 0.0
    g_count = sequence.count("G")
    c_count = sequence.count("C")
    return ((g_count + c_count) / len(sequence)) * 100


def parse_fasta(file_path: str) -> dict[str, str]:
    """Считывает файл и склеивает строки нуклеотидов для каждого заголовка.

    Args:
        file_path: путь к файлу в формате FASTA.

    Returns:
        Словарь {идентификатор: последовательность}.
    """
    sequences: dict[str, str] = {}
    current_id = ""

    with open(file_path, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            if line.startswith(">"):
                current_id = line[1:]
                sequences[current_id] = ""
            else:
                sequences[current_id] += line

    return sequences


def main() -> None:
    """Читает input.txt, находит последовательность с максимальным GC-составом
    и выводит её идентификатор и GC-состав с точностью до 6 знаков.
    """
    sequences = parse_fasta("GC.txt")

    best_id = ""
    max_gc = -1.0

    for seq_id, seq in sequences.items():
        gc_value = calculate_gc(seq)
        if gc_value > max_gc:
            max_gc = gc_value
            best_id = seq_id

    print(best_id)
    print(f"{max_gc:.6f}")


if __name__ == "__main__":
    main()
