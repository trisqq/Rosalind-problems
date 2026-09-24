def count_hamming_distance(seq1: str, seq2: str) -> int:
    """Сравнивает две строки равной длины и считает несовпадения.

    Args:
        seq1: первая строка.
        seq2: вторая строка той же длины.

    Returns:
        Количество позиций, в которых символы различаются.
    """
    mismatches = 0
    for i in range(len(seq1)):
        if seq1[i] != seq2[i]:
            mismatches += 1
    return mismatches


def main() -> None:
    """Читает две строки из Mutations.txt, считает расстояние Хэмминга и печатает его.
    """
    with open("Mutations.txt", "r") as f:
        s = f.readline().strip()
        t = f.readline().strip()

    distance = count_hamming_distance(s, t)
    print(distance)


if __name__ == "__main__":
    main()
